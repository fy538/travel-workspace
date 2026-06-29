#!/usr/bin/env python3
"""Per-persona QA spine — the ``make qa-persona PERSONA=<x>`` orchestrator.

Walks ONE dogfood persona through their entire seeded world and assembles a
single QA report spanning three lanes:

  1. Content gates  (A2)  — travel-agent/scripts/dogfood_coherence_export.py
  2. Journey cert   (B2)  — travel-agent/scripts/dogfood_journey_persona_cert.py
  3. Visual walk    (A1)  — travel-app/scripts/polish-qa/surfaces.mjs

Token-free orchestration. This script makes NO live LLM calls of its own — it
shells the content + journey steps (which run DB-backed under AI_MODE=replay)
and reads the visual surface registry. The visual lane produces a capture PLAN
(ordered deep-links per surface) + a verdict scaffold note; real screenshots
need a Mac simulator, so we scaffold rather than fake.

Usage:
    python scripts/qa_persona.py --persona mara
    python scripts/qa_persona.py --persona elif --gate
    python scripts/qa_persona.py --persona elif --repo-root /path/to/workspace

Output: <travel-agent>/tools/dogfood/persona-qa/<persona>.md

Exit codes:
    --gate  : non-zero iff the Overall Verdict is FAIL.
    default : always 0 (informational).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

import yaml

# ── Layout ──────────────────────────────────────────────────────────────────

# Default repo-root = the workspace this script lives in (scripts/qa_persona.py).
_DEFAULT_REPO_ROOT = Path(__file__).resolve().parent.parent

# The five cities the A2 content-gate (and B2 trips) understand. cross-city /
# profile-consolidation packs have no per-city gate, so they are excluded here.
_GATE_CITIES = {"lisbon", "rome", "istanbul", "tokyo", "brooklyn"}

# Visual surface KEY → the screenshot-mode route name. The deep-link is
# guide://dev/screenshot-mode?persona=<x>&to=<route>; the surface key is the
# canonical destination route name in the polish-qa registry.
_AI_MODE = "replay"


# ── Persona → (city, pack) resolution ───────────────────────────────────────


def _load_yaml(path: Path) -> dict:
    with path.open() as fh:
        return yaml.safe_load(fh) or {}


def resolve_persona_cities(agent_root: Path, persona: str) -> list[dict]:
    """Resolve a persona to an ordered list of {city, pack, scenario} dicts.

    Authoritative source is scenarios.yaml (explicit persona + packs), since a
    pack's ``persona`` field is the content OWNER, not the trip protagonist
    (e.g. lisbon-phase1.persona == elif, but S4 makes mara the organizer). We
    take every backend-real scenario whose ``persona`` == slug, expand its
    packs to cities, and keep only gateable cities — de-duplicated in
    first-seen order.
    """
    packs_path = agent_root / "tools" / "dogfood" / "content" / "packs.yaml"
    scen_path = agent_root / "tools" / "dogfood" / "content" / "scenarios.yaml"
    if not packs_path.exists() or not scen_path.exists():
        return []

    packs = _load_yaml(packs_path).get("packs", {})
    scenarios = _load_yaml(scen_path).get("scenarios", {})

    seen: set[str] = set()
    out: list[dict] = []
    for scen_key, scen in scenarios.items():
        if scen.get("persona") != persona:
            continue
        if scen.get("lane") != "backend_real":
            continue
        for pack_key in scen.get("packs", []):
            city = packs.get(pack_key, {}).get("city")
            if city in _GATE_CITIES and city not in seen:
                seen.add(city)
                out.append({"city": city, "pack": pack_key, "scenario": scen_key})
    return out


# ── Content lane (A2) ───────────────────────────────────────────────────────

# A "## Content Gates" line looks like:  - 🟡 **gate_name** — detail text
_GATE_LINE_RE = re.compile(r"^- (\S+)\s+\*\*(?P<name>[^*]+)\*\*\s+—\s+(?P<detail>.*)$")
_GATE_EMOJI_STATUS = {"✅": "pass", "🟡": "warn", "🔴": "fail", "⤵️": "skip"}


def _parse_content_gates(report_md: str) -> list[dict]:
    """Pull the gate rows out of the '## Content Gates' section of a report."""
    gates: list[dict] = []
    in_section = False
    for raw in report_md.splitlines():
        line = raw.rstrip()
        if line.startswith("## Content Gates"):
            in_section = True
            continue
        if in_section:
            if line.startswith("## "):  # next section ends ours
                break
            m = _GATE_LINE_RE.match(line)
            if not m:
                continue
            emoji = line[2:].split(" ", 1)[0]
            status = _GATE_EMOJI_STATUS.get(emoji, "unknown")
            gates.append(
                {
                    "name": m.group("name").strip(),
                    "status": status,
                    "detail": m.group("detail").strip(),
                }
            )
    return gates


def run_content_lane(agent_root: Path, city_pairs: list[dict]) -> dict:
    """Run the A2 content-gate command per city and aggregate gate results.

    Returns {"cities": [...], "counts": {pass,warn,fail,skip}, "any_fail": bool}.
    """
    reports_dir = agent_root / "tools" / "dogfood" / "coherence-reports"
    env = {**os.environ, "AI_MODE": _AI_MODE, "PYTHONPATH": "."}

    cities: list[dict] = []
    counts = {"pass": 0, "warn": 0, "fail": 0, "skip": 0}

    for pair in city_pairs:
        city = pair["city"]
        cmd = [
            sys.executable,
            "scripts/dogfood_coherence_export.py",
            "--gate",
            "--pack",
            city,
        ]
        entry: dict = {"city": city, "pack": pair["pack"], "gates": []}
        try:
            proc = subprocess.run(
                cmd,
                cwd=str(agent_root),
                env=env,
                capture_output=True,
                text=True,
                timeout=600,
            )
            entry["exit_code"] = proc.returncode
        except FileNotFoundError:
            entry["error"] = "content-gate script not found"
            entry["exit_code"] = None
            cities.append(entry)
            continue
        except subprocess.SubprocessError as exc:  # timeout etc.
            entry["error"] = f"content-gate run errored: {exc}"
            entry["exit_code"] = None
            cities.append(entry)
            continue

        report_path = reports_dir / f"{city}.md"
        if report_path.exists():
            gates = _parse_content_gates(report_path.read_text())
            entry["gates"] = gates
            for g in gates:
                counts[g["status"]] = counts.get(g["status"], 0) + 1
        else:
            entry["error"] = (
                f"report not regenerated at {report_path} "
                f"(exit {entry['exit_code']}); stderr: {proc.stderr.strip()[:200]}"
            )
        cities.append(entry)

    any_fail = any(
        (c.get("exit_code") not in (0, None))
        or any(g["status"] == "fail" for g in c.get("gates", []))
        for c in cities
    )
    return {"cities": cities, "counts": counts, "any_fail": any_fail}


# ── Journey lane (B2) — defensive ───────────────────────────────────────────


def run_journey_lane(agent_root: Path, persona: str) -> dict:
    """Run the B2 certifier defensively.

    Contract:
        AI_MODE=replay PYTHONPATH=. python scripts/dogfood_journey_persona_cert.py \
            --persona <slug> --journey all --json
        → stdout JSON {"persona":..,"journeys":[{"id","status","trip","reason"}],
                       "summary":{"pass","fail","skip"}}, exit non-zero iff any FAIL.

    If the script is missing OR errors OR emits unparseable JSON, return a
    "pending" result and DO NOT crash — the rest of the spine must still work.
    """
    script = agent_root / "scripts" / "dogfood_journey_persona_cert.py"
    if not script.exists():
        return {
            "status": "pending",
            "reason": "certifier not available (scripts/dogfood_journey_persona_cert.py missing)",
            "journeys": [],
            "summary": {"pass": 0, "fail": 0, "skip": 0},
        }

    cmd = [
        sys.executable,
        "scripts/dogfood_journey_persona_cert.py",
        "--persona",
        persona,
        "--journey",
        "all",
        "--json",
    ]
    env = {**os.environ, "AI_MODE": _AI_MODE, "PYTHONPATH": "."}
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(agent_root),
            env=env,
            capture_output=True,
            text=True,
            timeout=900,
        )
    except subprocess.SubprocessError as exc:
        return {
            "status": "pending",
            "reason": f"certifier errored: {exc}",
            "journeys": [],
            "summary": {"pass": 0, "fail": 0, "skip": 0},
        }

    try:
        data = json.loads(proc.stdout)
    except (json.JSONDecodeError, ValueError):
        return {
            "status": "pending",
            "reason": (
                f"certifier produced unparseable output (exit {proc.returncode}); "
                f"stderr: {proc.stderr.strip()[:200]}"
            ),
            "journeys": [],
            "summary": {"pass": 0, "fail": 0, "skip": 0},
        }

    journeys = data.get("journeys", [])
    summary = data.get("summary") or {
        "pass": sum(1 for j in journeys if j.get("status") == "pass"),
        "fail": sum(1 for j in journeys if j.get("status") == "fail"),
        "skip": sum(1 for j in journeys if j.get("status") == "skip"),
    }
    any_fail = (proc.returncode not in (0, None)) or summary.get("fail", 0) > 0
    return {
        "status": "fail" if any_fail else "pass",
        "exit_code": proc.returncode,
        "journeys": journeys,
        "summary": summary,
        "any_fail": any_fail,
    }


# ── Visual lane (A1) — walk-plan scaffold ───────────────────────────────────


def run_visual_lane(app_root: Path, persona: str) -> dict:
    """Build the per-persona visual WALK PLAN from surfaces.mjs.

    Lists surfaces whose capture persona == this persona (or 'default', the
    shared baseline), emitting an ordered list of
    guide://dev/screenshot-mode?persona=<x>&to=<route> deep-links plus the
    expected[] assertions per surface. Marked scaffold — capture+verdict run on
    a Mac simulator (this environment has none).
    """
    surfaces_mjs = app_root / "scripts" / "polish-qa" / "surfaces.mjs"
    if not surfaces_mjs.exists():
        return {
            "available": False,
            "reason": f"surface registry not found at {surfaces_mjs}",
            "stops": [],
        }

    # Use node to import the ESM module and emit a flat capture list as JSON.
    node_script = (
        "import { SURFACES } from %s;"
        "const out=[];"
        "for (const [key,s] of Object.entries(SURFACES)){"
        "  for (const c of (s.captures||[])){"
        "    out.push({surface:key,title:s.title,persona:c.persona,label:c.label,"
        "              screenshot:c.screenshot,expected:c.expected||[]});"
        "  }"
        "}"
        "process.stdout.write(JSON.stringify(out));"
    ) % json.dumps(str(surfaces_mjs))

    try:
        proc = subprocess.run(
            ["node", "--input-type=module", "-e", node_script],
            cwd=str(app_root),
            capture_output=True,
            text=True,
            timeout=120,
        )
        captures = json.loads(proc.stdout)
    except (FileNotFoundError, subprocess.SubprocessError, json.JSONDecodeError) as exc:
        return {
            "available": False,
            "reason": f"could not read surface registry via node: {exc}",
            "stops": [],
        }

    stops: list[dict] = []
    for c in captures:
        cap_persona = c.get("persona")
        if cap_persona not in (persona, "default"):
            continue
        route = c["surface"]
        deeplink = (
            f"guide://dev/screenshot-mode?persona={cap_persona}&to={route}"
        )
        stops.append(
            {
                "surface": route,
                "title": c.get("title", route),
                "persona": cap_persona,
                "label": c.get("label", ""),
                "screenshot": c.get("screenshot", ""),
                "deeplink": deeplink,
                "shared": cap_persona == "default",
                "expected": c.get("expected", []),
            }
        )
    return {"available": True, "stops": stops}


# ── Overall verdict ─────────────────────────────────────────────────────────


def derive_overall(content: dict, journey: dict) -> str:
    """fail if any content-gate FAIL or any journey FAIL; mixed if warns/skips
    (or a pending journey); pass otherwise."""
    if content.get("any_fail") or journey.get("any_fail"):
        return "fail"
    counts = content.get("counts", {})
    has_warn_skip = counts.get("warn", 0) > 0 or counts.get("skip", 0) > 0
    j_summary = journey.get("summary", {})
    has_j_skip = j_summary.get("skip", 0) > 0
    pending = journey.get("status") == "pending"
    if has_warn_skip or has_j_skip or pending:
        return "mixed"
    return "pass"


# ── Report assembly ─────────────────────────────────────────────────────────

_OVERALL_EMOJI = {"pass": "✅", "mixed": "🟡", "fail": "🔴"}
_GATE_RENDER_EMOJI = {"pass": "✅", "warn": "🟡", "fail": "🔴", "skip": "⤵️", "unknown": "❔"}
_JOURNEY_EMOJI = {"pass": "✅", "fail": "🔴", "skip": "⤵️", "pending": "⏳"}


def _resolve_stamp(agent_root: Path, override: str | None) -> str:
    """Derive a date stamp WITHOUT datetime.now() — match how the A2 report
    stamps. We reuse the freshest existing coherence report's '— <date>' header
    so the persona report carries the same run date. Falls back to a passed-in
    override, then to a stable placeholder."""
    if override:
        return override
    reports_dir = agent_root / "tools" / "dogfood" / "coherence-reports"
    stamp_re = re.compile(r"Coherence Report — (\d{4}-\d{2}-\d{2})")
    candidates: list[str] = []
    if reports_dir.exists():
        for md in reports_dir.glob("*.md"):
            m = stamp_re.search(md.read_text())
            if m:
                candidates.append(m.group(1))
    if candidates:
        return max(candidates)  # freshest by ISO ordering
    return "unstamped"


def assemble_report(
    persona: str,
    stamp: str,
    city_pairs: list[dict],
    content: dict,
    journey: dict,
    visual: dict,
    overall: str,
) -> str:
    L: list[str] = []
    L.append(f"# Persona QA — {persona} — {stamp}")
    L.append("")
    L.append(
        f"Single-pass QA spine: content gates + journey certification + visual "
        f"walk plan for the **{persona}** dogfood world. Token-free "
        f"(AI_MODE={_AI_MODE}, no live LLM calls)."
    )
    L.append("")
    cities = ", ".join(p["city"] for p in city_pairs) or "_(none resolved)_"
    L.append(f"- Persona: `{persona}`")
    L.append(f"- Cities / trips: {cities}")
    L.append(f"- Overall Verdict: {_OVERALL_EMOJI.get(overall, '❔')} **{overall.upper()}**")
    L.append("")

    # ── 1. Content gates ────────────────────────────────────────────────────
    L.append("## 1. Content Gates")
    L.append("")
    c = content.get("counts", {})
    L.append(
        f"Aggregate across {len(content.get('cities', []))} city pack(s): "
        f"{c.get('fail', 0)} fail / {c.get('warn', 0)} warn / "
        f"{c.get('pass', 0)} pass / {c.get('skip', 0)} skip."
    )
    L.append("")
    for ce in content.get("cities", []):
        city = ce["city"]
        L.append(f"### {city} (`{ce['pack']}`)")
        if ce.get("error"):
            L.append(f"- ⚠️ {ce['error']}")
            L.append("")
            continue
        L.append(f"- content-gate exit code: `{ce.get('exit_code')}`")
        if not ce.get("gates"):
            L.append("- _(no gate rows parsed)_")
        for g in ce.get("gates", []):
            emoji = _GATE_RENDER_EMOJI.get(g["status"], "❔")
            L.append(f"- {emoji} **{g['name']}** — {g['detail']}")
        L.append("")

    # ── 2. Journeys ─────────────────────────────────────────────────────────
    L.append("## 2. Fullstack Journeys")
    L.append("")
    if journey.get("status") == "pending":
        L.append(f"⏳ **pending** — {journey.get('reason', 'certifier not available')}")
        L.append("")
        L.append(
            "_The B2 journey certifier (`scripts/dogfood_journey_persona_cert.py`) "
            "was not runnable at this pass. Re-run once it lands; the orchestrator "
            "calls it as `--persona "
            f"{persona} --journey all --json` and parses the JSON contract._"
        )
        L.append("")
    else:
        js = journey.get("summary", {})
        L.append(
            f"Summary: {js.get('pass', 0)} pass / {js.get('fail', 0)} fail / "
            f"{js.get('skip', 0)} skip (exit `{journey.get('exit_code')}`)."
        )
        L.append("")
        if journey.get("journeys"):
            L.append("| Journey | Status | Trip | Reason |")
            L.append("| --- | --- | --- | --- |")
            for j in journey["journeys"]:
                emoji = _JOURNEY_EMOJI.get(j.get("status"), "❔")
                reason = (j.get("reason") or "").replace("|", "\\|")
                L.append(
                    f"| {j.get('id', '?')} | {emoji} {j.get('status', '?')} "
                    f"| {j.get('trip', '—')} | {reason} |"
                )
        else:
            L.append("_(certifier returned no journey rows)_")
        L.append("")

    # ── 3. Visual walk plan ─────────────────────────────────────────────────
    L.append("## 3. Visual Walk Plan")
    L.append("")
    L.append(
        "_Scaffold — run capture + verdict on a Mac simulator._ Real screenshots "
        "need a device/simulator; this lane emits the ordered deep-link walk and "
        "the expected[] assertions a vision agent fills in afterward "
        "(`travel-app/scripts/polish-qa/verdict.mjs scaffold|validate|commit`)."
    )
    L.append("")
    if not visual.get("available"):
        L.append(f"- ⚠️ {visual.get('reason', 'surface registry unavailable')}")
        L.append("")
    else:
        stops = visual.get("stops", [])
        own = [s for s in stops if not s["shared"]]
        shared = [s for s in stops if s["shared"]]
        L.append(
            f"{len(stops)} surface stop(s): {len(own)} persona-specific, "
            f"{len(shared)} shared (`default`) baseline."
        )
        L.append("")
        for i, s in enumerate(stops, 1):
            tag = " _(shared default)_" if s["shared"] else ""
            L.append(f"### {i}. {s['surface']} — {s['label']}{tag}")
            L.append(f"- Deep-link: `{s['deeplink']}`")
            if s.get("screenshot"):
                L.append(f"- Screenshot: `{s['screenshot']}.png`")
            if s.get("expected"):
                L.append("- Expected:")
                for e in s["expected"]:
                    L.append(f"  - [ ] {e}")
            L.append("")

    # ── Verdict rationale ───────────────────────────────────────────────────
    L.append("## Overall Verdict")
    L.append("")
    L.append(f"{_OVERALL_EMOJI.get(overall, '❔')} **{overall.upper()}**")
    L.append("")
    L.append(
        "- **fail** if any content-gate FAIL or any journey FAIL.\n"
        "- **mixed** if any warns/skips (content or journey) or the journey "
        "lane is pending.\n"
        "- **pass** otherwise."
    )
    L.append("")
    L.append(
        f"_Generated {stamp} | content {c.get('fail', 0)}F/{c.get('warn', 0)}W/"
        f"{c.get('pass', 0)}P/{c.get('skip', 0)}S | "
        f"journey {journey.get('status', '?')} | "
        f"visual {'scaffold' if visual.get('available') else 'unavailable'}_"
    )
    L.append("")
    return "\n".join(L)


# ── Main ────────────────────────────────────────────────────────────────────


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--persona", required=True, help="Dogfood persona slug (e.g. mara, elif).")
    parser.add_argument(
        "--gate",
        action="store_true",
        help="Exit non-zero if the Overall Verdict is FAIL. Without --gate, informational (exit 0).",
    )
    parser.add_argument(
        "--repo-root",
        default=None,
        help="Workspace root containing travel-agent/ and travel-app/ (default: this script's workspace).",
    )
    parser.add_argument(
        "--stamp",
        default=None,
        help="Override the date stamp (ISO). Default derives from existing coherence reports (no datetime.now()).",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve() if args.repo_root else _DEFAULT_REPO_ROOT
    agent_root = repo_root / "travel-agent"
    app_root = repo_root / "travel-app"
    persona = args.persona

    if not agent_root.exists():
        print(f"✗ travel-agent not found at {agent_root}", file=sys.stderr)
        return 2

    city_pairs = resolve_persona_cities(agent_root, persona)
    if not city_pairs:
        print(
            f"⚠️  No gateable backend-real cities resolved for persona '{persona}'. "
            f"Report will still be assembled (content section empty).",
            file=sys.stderr,
        )

    print(f"→ persona={persona}  cities={[p['city'] for p in city_pairs]}", file=sys.stderr)

    content = run_content_lane(agent_root, city_pairs)
    journey = run_journey_lane(agent_root, persona)
    visual = run_visual_lane(app_root, persona)
    overall = derive_overall(content, journey)
    stamp = _resolve_stamp(agent_root, args.stamp)

    report = assemble_report(persona, stamp, city_pairs, content, journey, visual, overall)

    out_dir = agent_root / "tools" / "dogfood" / "persona-qa"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{persona}.md"
    out_path.write_text(report)

    print(f"→ content: {content['counts']}  |  journey: {journey.get('status')}  "
          f"|  visual: {'scaffold' if visual.get('available') else 'unavailable'}", file=sys.stderr)
    print(f"→ Overall Verdict: {overall.upper()}", file=sys.stderr)
    print(f"→ report: {out_path}", file=sys.stderr)

    if args.gate and overall == "fail":
        print(f"\n=== QA-PERSONA GATE: {persona} FAILED (Overall={overall}) ===", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
