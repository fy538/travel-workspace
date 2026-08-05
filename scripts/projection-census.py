#!/usr/bin/env python3
"""projection-census — every projection variant the three roots can emit,
and whether anything actually renders it.

The home-surface audit (docs/working/home-surface-section-card-audit-2026-08-05.md)
was hand-assembled, and hand-assembled inventories have been wrong twice in
one day before (the crown receipt audit was revised twice because it
contradicted work that already existed). This derives the same census from
the code, so a design board built on it cannot draw a state no producer can
emit — the "data fiction" failure mode.

For every variant on every axis it answers three independent questions:

  DECLARED   — is it in the union / enum? (the type says it may exist)
  PRODUCED   — does a backend producer construct it? (it can reach a client)
  DISPATCHED — does a frontend renderer branch on it? (it has a shape)

and buckets the result:

  LIVE        declared + produced + dispatched. A real, visible variant.
  INVISIBLE   produced but nothing branches on it. Backend work the user
              cannot see — collapses into whatever the generic path draws.
              This is the bucket that needs drawings most.
  CAPACITY    declared, no producer. Contract room, not product. Do NOT
              spend a drawing here without ruling it near-term first.
  ORPHAN      dispatched but nothing produces it. Dead renderer, or a
              producer that was removed and left the branch behind.

Dispatch means VISUAL dispatch: only files under each root's renderer
directories count. Type unions (schema.gen.ts), fixtures, personas, tests
and dev galleries are excluded — a persona carrying kind="weather" proves a
fixture exists, not that a renderer draws it differently.

Read-only. Touches no database and no network.

Usage:
  python3 scripts/projection-census.py                # table to stdout
  python3 scripts/projection-census.py --json OUT     # board input
  python3 scripts/projection-census.py --surface trips
  python3 scripts/projection-census.py --substrate    # the drawing list
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent
AGENT = WORKSPACE / "travel-agent"
APP = WORKSPACE / "travel-app"

# Frontend paths that mention variant names without rendering them.
FE_EXCLUDE = (
    "__tests__",
    "/constants/personas/",
    "/constants/mocks/",
    "/utils/api/schema.gen.ts",
    "/utils/api/types.ts",
    "/app/dev/",
    ".test.",
    ".stories.",
)


# ---------------------------------------------------------------- helpers


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return ""


def walk(root: Path, suffixes: tuple[str, ...], exclude: tuple[str, ...] = ()) -> list[Path]:
    """Every file under root with one of these suffixes, minus excludes."""
    if not root.exists():
        return []
    out: list[Path] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix not in suffixes:
            continue
        posix = path.as_posix()
        if "node_modules" in posix or "__pycache__" in posix:
            continue
        if any(token in posix for token in exclude):
            continue
        out.append(path)
    return out


def hits(paths: list[Path], patterns: list[re.Pattern[str]]) -> dict[str, list[str]]:
    """Map matched group(1) -> files it was found in."""
    found: dict[str, list[str]] = {}
    for path in paths:
        body = read(path)
        if not body:
            continue
        rel = path.relative_to(WORKSPACE).as_posix()
        for pattern in patterns:
            for match in pattern.finditer(body):
                found.setdefault(match.group(1), [])
                if rel not in found[match.group(1)]:
                    found[match.group(1)].append(rel)
    return found


def literal_union(path: Path, name: str) -> list[str]:
    """Parse `NAME = Literal["a", "b", ...]` out of a Python module."""
    body = read(path)
    match = re.search(rf"{re.escape(name)}\s*=\s*Literal\[(.*?)\]", body, re.S)
    if not match:
        return []
    return re.findall(r'"([^"]+)"', match.group(1))


def enum_members(path: Path, class_name: str) -> list[str]:
    """Parse `VALUE = "value"` members out of a StrEnum class body."""
    body = read(path)
    match = re.search(rf"class {re.escape(class_name)}\(StrEnum\):(.*?)(?=\nclass |\Z)", body, re.S)
    if not match:
        return []
    return re.findall(r'^\s+[A-Z_0-9]+\s*=\s*"([^"]+)"', match.group(1), re.M)


# ---------------------------------------------------------------- model


@dataclass
class Variant:
    name: str
    declared: bool = True
    produced_in: list[str] = field(default_factory=list)
    dispatched_in: list[str] = field(default_factory=list)
    note: str = ""
    visual: bool = True

    @property
    def verdict(self) -> str:
        produced, dispatched = bool(self.produced_in), bool(self.dispatched_in)
        # A semantic axis is not SUPPOSED to have a visual branch — section
        # reason drives the label and the ordering, and treatment (a separate,
        # server-owned axis) drives the shape. Scoring it against dispatch
        # would report 16 correct designs as 16 gaps.
        if not self.visual:
            return "LIVE" if produced else "CAPACITY"
        if produced and dispatched:
            return "LIVE"
        if produced and not dispatched:
            return "INVISIBLE"
        if not produced and dispatched:
            return "ORPHAN"
        return "CAPACITY"


@dataclass
class Axis:
    surface: str
    axis: str
    source: str  # where the declaration lives, for the report header
    mechanism: str  # how the frontend routes, in one line
    variants: list[Variant]
    visual: bool = True  # False => dispatch is informational, not scored

    def __post_init__(self) -> None:
        for variant in self.variants:
            variant.visual = self.visual


# ---------------------------------------------------------------- trips


def trips_stack_kinds() -> Axis:
    models = AGENT / "backend/home/concierge_feed/models.py"
    declared = literal_union(models, "ConciergeHomeCardKind")

    be = walk(AGENT / "backend/home", (".py",))
    be = [p for p in be if p.name != "models.py"]
    produced = hits(be, [re.compile(r'\bkind\s*=\s*"([a-z_]+)"')])

    # Not every kind is emitted as a literal `kind="…"`. `_attention_kind`
    # maps archetype -> kind through a dict, so six kinds (daily_brief,
    # constraint_alert, capture_nudge, planning_brief, trip_retrospective,
    # settlement_closeout) reach the client as dict VALUES and a literal
    # scan reports them as producerless. Any function annotated
    # `-> ConciergeHomeCardKind` returns kinds by construction, so every
    # string literal in its body counts as an emission site.
    for path in be:
        body = read(path)
        for match in re.finditer(
            r"def \w+\([^)]*\)\s*->\s*ConciergeHomeCardKind:(.*?)(?=\ndef |\Z)", body, re.S
        ):
            rel = path.relative_to(WORKSPACE).as_posix()
            for literal in re.findall(r'"([a-z_]+)"', match.group(1)):
                if literal in declared:
                    produced.setdefault(literal, [])
                    if rel not in produced[literal]:
                        produced[literal].append(rel)

    # Property-qualified only. A bare `case 'starter':` in tripsHomeMast.ts
    # switches on POSTURE, which shares several names with the kind union —
    # counting it credited the stack with a shape it does not have.
    fe = walk(APP / "components/trips", (".ts", ".tsx"), FE_EXCLUDE)
    fe += walk(APP / "app/(tabs)/trips", (".ts", ".tsx"), FE_EXCLUDE)
    dispatched = hits(fe, [re.compile(r'\.kind\s*===\s*[\'"]([a-z_]+)[\'"]')])

    return Axis(
        "Trips",
        "stack kind",
        "backend/home/concierge_feed/models.py :: ConciergeHomeCardKind",
        "None. The crown and rows render generically from title/row_line; "
        "kind drives ranking, suppression and analytics, never a shape.",
        [
            Variant(name, True, produced.get(name, []), dispatched.get(name, []))
            for name in declared
        ],
    )


def trips_receipt_kinds() -> Axis:
    stack = AGENT / "backend/home/trips_stack.py"
    body = read(stack)

    # class TripsHomeReceiptLedger(BaseModel): ... kind: Literal["ledger"]
    pairs = re.findall(
        r'class (TripsHomeReceipt\w+)\(BaseModel\):(.*?)(?=\nclass |\Z)', body, re.S
    )
    declared: list[tuple[str, str]] = []
    for class_name, class_body in pairs:
        match = re.search(r'kind:\s*Literal\["([a-z_]+)"\]', class_body)
        if match:
            declared.append((class_name, match.group(1)))

    be = walk(AGENT / "backend/home", (".py",)) + walk(AGENT / "backend/api/routes", (".py",))
    # `(?<!class )` matters: `class TripsHomeReceiptLedger(BaseModel)` matches a
    # naive `Name\(` and made every declared receipt look produced.
    constructed = hits(be, [re.compile(r"(?<!class )\b(TripsHomeReceipt\w+)\(")])

    fe = walk(APP / "components/trips", (".ts", ".tsx"), FE_EXCLUDE)
    dispatched = hits(fe, [re.compile(r'kind\s*===\s*[\'"]([a-z_]+)[\'"]')])

    variants = [
        Variant(kind, True, constructed.get(class_name, []), dispatched.get(kind, []), note=class_name)
        for class_name, kind in declared
    ]

    return Axis(
        "Trips",
        "crown receipt",
        "backend/home/trips_stack.py :: TripsHomeReceipt* discriminated union",
        "components/trips/TripsStackCrown.tsx branches on receipt.kind — "
        "one branch only; every other variant falls through to title + row_line.",
        variants,
    )


def trips_plan_kind() -> Axis:
    """The local/travel discriminator.

    Not a card axis — a PLAN axis — but it belongs in the census for the
    reason the others do: `trip_kind` was ratified 2026-07-31 (§9.1 of the
    everyday-places MVP: generalize the trip aggregate, do not fork an
    `outings` stack), the column and its CHECK constraint are applied, and
    the model, CRUD, request schema and route are all threaded. What does
    not exist is a producer and a projection. Without a row here that gap
    is invisible to the census by construction — an axis nothing emits and
    nothing draws has no variant to report.
    """
    models = AGENT / "backend/core/models/trips.py"
    declared = literal_union(models, "TripKind")

    # The default value is produced by every creation path by definition;
    # any other value needs an explicit caller. Tests are not producers —
    # tests/core/test_local_trip_creation.py proves the planner ACCEPTS a
    # local trip, which is not the same as anything creating one.
    body = read(models)
    default = re.search(r'trip_kind:\s*TripKind\s*=\s*"([a-z_]+)"', body)
    default_value = default.group(1) if default else ""

    be = walk(AGENT / "backend", (".py",), ("/tests/",))
    supplied = hits(be, [re.compile(r'trip_kind\s*=\s*["\']([a-z_]+)["\']')])

    fe = walk(APP / "components", (".ts", ".tsx"), FE_EXCLUDE)
    fe += walk(APP / "app", (".ts", ".tsx"), FE_EXCLUDE)
    dispatched = hits(fe, [re.compile(r'trip_kind\s*===?\s*[\'"]([a-z_]+)[\'"]')])

    variants = []
    for value in declared:
        sites = list(supplied.get(value, []))
        if value == default_value and not sites:
            sites = [models.relative_to(WORKSPACE).as_posix() + " (model default)"]
        variants.append(Variant(value, True, sites, dispatched.get(value, [])))

    return Axis(
        "Trips",
        "plan kind",
        "backend/core/models/trips.py :: TripKind",
        "Nothing branches on trip_kind anywhere in the app, and nothing "
        "creates a local plan. The column, the CHECK constraint, the model "
        "field and the route are all in place; the creation door and the "
        "capability suppression are not. Note the untripped wire: a local "
        "plan is a trip row, and the story composer does not branch on kind "
        "— so the first one minted composes an LLM Letter at T+24h.",
        variants,
    )


# --------------------------------------------------------------- places


def places_axis(
    class_name: str, axis_name: str, assign_kw: str, fe_patterns: list[re.Pattern[str]]
) -> Axis:
    models = AGENT / "backend/core/models/places_sections.py"
    declared = enum_members(models, class_name)

    # Must be the ASSIGNMENT form (`treatment=PlacesSectionTreatment.CONVICTION`).
    # A bare `PlacesSectionTreatment.CONVICTION` also appears in the contract
    # validator and in ranking.py's sort key — reading a value is not producing
    # one, and counting those made `conviction` look live when the audit
    # correctly calls it dormant capacity.
    be = walk(AGENT / "backend/places", (".py",))
    produced = hits(be, [re.compile(rf"{assign_kw}\s*=\s*{class_name}\.([A-Z_0-9]+)")])
    # enum member name -> value
    body = read(models)
    match = re.search(rf"class {class_name}\(StrEnum\):(.*?)(?=\nclass |\Z)", body, re.S)
    member_to_value = dict(
        re.findall(r'^\s+([A-Z_0-9]+)\s*=\s*"([^"]+)"', match.group(1) if match else "", re.M)
    )
    produced_by_value: dict[str, list[str]] = {}
    for member, files in produced.items():
        value = member_to_value.get(member)
        if value:
            produced_by_value.setdefault(value, []).extend(files)

    fe = walk(APP / "components/places", (".ts", ".tsx"), FE_EXCLUDE)
    fe += walk(APP / "app/(tabs)/places", (".ts", ".tsx"), FE_EXCLUDE)
    dispatched = hits(fe, fe_patterns)

    return Axis(
        "Places",
        axis_name,
        f"backend/core/models/places_sections.py :: {class_name}",
        "",
        [
            Variant(v, True, produced_by_value.get(v, []), dispatched.get(v, []))
            for v in declared
        ],
    )


def places_card_kinds() -> Axis:
    """Card kinds route on PAYLOAD PRESENCE, not on card.kind.

    PlacesSectionFeed checks `card.place`, `card.angle`, `card.experience`…
    in order and defaults the scalar-only remainder to the notice/prompt
    renderer. So a kind is "dispatched" if EITHER its payload field is read
    or its literal is compared. The mechanism is recorded because it is
    itself the audit's Finding 4.
    """
    axis = places_axis(
        "PlacesCardKind",
        "card kind",
        "kind",
        [
            re.compile(r'card\.kind\s*===\s*[\'"]([a-z_]+)[\'"]'),
            re.compile(r"card\.([a-z_]+)\b"),
        ],
    )
    axis.mechanism = (
        "components/places/PlacesSectionFeed.tsx routes on PAYLOAD PRESENCE "
        "(card.place / card.angle / …), not on card.kind. Backend validation "
        "makes that safe today; a future scalar-only kind renders as a notice."
    )
    return axis


# --------------------------------------------------------------- vesper


def vesper_list_kinds() -> Axis:
    models = AGENT / "backend/home/vesper_workbench/models.py"
    declared = literal_union(models, "WorkbenchListKind")

    # Workbench list kinds are produced STRUCTURALLY — one module and one
    # `build_<kind>_items` per kind, assembled by a loop in assemble.py —
    # not by emitting a `kind="…"` literal. Scanning for the literal reported
    # route/season/here as producerless, which was true on 2026-07-31 and is
    # not true now. Detect the builder.
    be = walk(AGENT / "backend/home/vesper_workbench", (".py",))
    be = [p for p in be if p.name not in {"models.py", "rotation.py"}]
    produced = hits(be, [re.compile(r'\bkind\s*=\s*"([a-z_]+)"')])
    for name in declared:
        for path in be:
            if re.search(rf"def build_{name}_items\b", read(path)):
                produced.setdefault(name, []).append(
                    path.relative_to(WORKSPACE).as_posix()
                )

    fe = walk(APP / "components/vesper-workbench", (".ts", ".tsx"), FE_EXCLUDE)
    fe += walk(APP / "app/(tabs)/concierge", (".ts", ".tsx"), FE_EXCLUDE)
    dispatched = hits(
        fe,
        [
            re.compile(r'kind\s*===\s*[\'"]([a-z_]+)[\'"]'),
            re.compile(r'case\s+[\'"]([a-z_]+)[\'"]\s*:'),
        ],
    )

    return Axis(
        "Vesper",
        "list kind",
        "backend/home/vesper_workbench/models.py :: WorkbenchListKind",
        "Two row families only — a session row and a shared world row for "
        "route/season/here. Deliberate: they differ in data, not in grammar.",
        [
            Variant(name, True, produced.get(name, []), dispatched.get(name, []))
            for name in declared
        ],
    )


# ------------------------------------------------------- substrate pass
#
# The census answers "which variants have no shape". It cannot answer "how
# many shapes do we need" — 23 invisible stack kinds is nowhere near 23
# drawings, because a receipt is projected from the SUBSTRATE a producer
# computed, never from the kind. Several kinds share one shape; a kind whose
# producer computes nothing can only ever be a stamp.
#
# So this pass walks the producers with `ast` (constructions span dozens of
# lines — regex cannot see which kwargs belong to which call) and asks, per
# kind: which substrate does the producer actually attach, and therefore
# which receipt is it eligible for?

# Substrate carried on its own excluded field, straight to a receipt.
# Source of truth: trips_stack.py::_receipt_for_card, in its branch order.
FIELD_RECEIPT = {
    "seats": "people",
    "audio": "waveform",
    "conditions": "conditions",
    "checks": "checklist",  # closed polarity — resolved rows, past tense
}

# Substrate carried on a Deck face, keyed by its layout literal.
LAYOUT_RECEIPT = {
    # DeckStructured
    "settle": "ledger",
    "plan_readiness": "checklist",  # open polarity
    "readiness": "checklist",
    "proposal_approval": "diff",
    # DeckFocus
    "call": "call",
    "pick": "candidates",
    "compare": "candidates",
    "brief": "spine",
}

# Declared and contract-validated, but _receipt_for_card / _receipt_from_focus
# have no branch for them — substrate that reaches the crown and projects to
# nothing. Not the same as "no substrate": these producers did the work.
LAYOUT_NO_RECEIPT = {"near_you", "choice_vote"}

SUBSTRATE_FIELDS = tuple(FIELD_RECEIPT) + ("structured", "focus")

# Every module that constructs a ConciergeHomeCard, plus the two that supply
# its substrate. ranking.py and stay_compare.py build cards too — omitting
# them reported three DECK_REQUIRED kinds as substrate-less.
PRODUCER_MODULES = (
    "backend/home/concierge_feed/producers.py",
    "backend/home/concierge_feed/ranking.py",
    "backend/home/concierge_feed/stay_compare.py",
    "backend/home/deck_payloads.py",
    "backend/home/feed.py",
    "backend/home/cards.py",
)


def _called_name(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return None


class _FuncIndex(ast.NodeVisitor):
    """Per-function: layouts built, calls made, archetypes and cards built."""

    def __init__(self, module: str) -> None:
        self.module = module
        self.stack: list[str] = []
        self.layouts: dict[str, set[str]] = defaultdict(set)
        self.calls: dict[str, set[str]] = defaultdict(set)
        self.archetypes: dict[str, set[str]] = defaultdict(set)
        self.builds_card: set[str] = set()
        # local `name = helper(...)` bindings, per enclosing function
        self.assigns: dict[str, dict[str, str]] = defaultdict(dict)
        # (kind | None, {field: builder}, function, module, arg0-helper)
        self.cards: list[tuple[str | None, dict[str, str | None], str, str, str | None]] = []

    def _visit_func(self, node: ast.AST) -> None:
        self.stack.append(getattr(node, "name", "?"))
        self.generic_visit(node)
        self.stack.pop()

    visit_FunctionDef = _visit_func  # noqa: N815
    visit_AsyncFunctionDef = _visit_func  # noqa: N815

    def visit_Assign(self, node: ast.Assign) -> None:  # noqa: N802
        # `constraint_card = _constraint_meal_card(...)` — the proxy is then
        # called with the VARIABLE, so without this the archetype is lost.
        if isinstance(node.value, ast.Call) and len(node.targets) == 1:
            target = node.targets[0]
            name = _called_name(node.value.func)
            if isinstance(target, ast.Name) and name:
                self.assigns[self.stack[-1] if self.stack else "<module>"][target.id] = name
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:  # noqa: N802
        here = self.stack[-1] if self.stack else "<module>"
        name = _called_name(node.func)
        if name:
            self.calls[here].add(name)

        if name in {"DeckStructured", "DeckFocus"}:
            for kw in node.keywords:
                if kw.arg == "layout" and isinstance(kw.value, ast.Constant):
                    self.layouts[here].add(str(kw.value.value))

        archetype_literal: str | None = None
        if name == "HomeCard":
            for kw in node.keywords:
                if kw.arg == "archetype" and isinstance(kw.value, ast.Constant):
                    archetype_literal = str(kw.value.value)
                    self.archetypes[here].add(archetype_literal)

        # A card construction, or a call to a proxy that builds one. Both
        # carry the substrate as kwargs, so both are collected here and the
        # proxy is filtered out later once we know which names are proxies.
        kind: str | None = None
        fields: dict[str, str | None] = {}
        for kw in node.keywords:
            if kw.arg == "kind" and isinstance(kw.value, ast.Constant):
                kind = str(kw.value.value)
            elif kw.arg in SUBSTRATE_FIELDS:
                if isinstance(kw.value, ast.Constant) and kw.value.value is None:
                    continue  # `structured=None` is an explicit absence
                # Attribute the layout to the builder called in THIS kwarg,
                # not to every builder the enclosing function touches —
                # that over-credited urgent_trip_action with three shapes.
                fields[kw.arg] = _kwarg_builder(kw.value)
        arg0 = None
        if node.args:
            first = node.args[0]
            if isinstance(first, ast.Call):
                arg0 = _called_name(first.func)
            elif isinstance(first, ast.Name):
                arg0 = first.id  # resolved against local assigns later

        if name == "HomeCard" and fields:
            # HomeCard carries its own `focus` field (cards.py), and
            # _home_card_to_concierge_card passes it straight through as
            # `card.focus`. Without this, constraint_alert's Call face —
            # attached upstream in feed.py, never at the card call site —
            # is invisible and a DECK_REQUIRED kind reads as substrate-less.
            self.cards.append(
                (None, fields, here, self.module, "archetype:" + (archetype_literal or ""))
            )
        elif name == "ConciergeHomeCard":
            self.builds_card.add(here)
            self.cards.append((kind, fields, here, self.module, arg0))
        elif fields:
            self.cards.append((kind, fields, here, self.module + " " + (name or ""), arg0))

        self.generic_visit(node)


def _kwarg_builder(node: ast.AST) -> str | None:
    """The builder whose result is passed as substrate — a call name, or a
    local variable name to be resolved against the function's assignments
    (`brief_focus = build_brief_focus(...)` then `focus=brief_focus`)."""
    if isinstance(node, ast.Call):
        return _called_name(node.func)
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.IfExp):  # `focus=x if x is not None else card.focus`
        return _kwarg_builder(node.body) or _kwarg_builder(node.orelse)
    return None


def _proxy_name(module_field: str) -> str:
    return module_field.split(" ", 1)[1]


def _module_of(module_field: str) -> str:
    return module_field.split(" ", 1)[0]


def _kinds_via_archetype(
    arg0: str | None,
    func: str,
    assigns: dict[str, dict[str, str]],
    helper_archetype: dict[str, str],
    archetype_kind: dict[str, str],
) -> set[str]:
    """Resolve a computed `kind` through the archetype of THIS call's card.

    _home_card_to_concierge_card takes focus/structured as PARAMETERS and
    derives kind via _attention_kind(card.archetype), so the call site holds
    both halves: argument 0 is the cards.py helper that stamps one archetype,
    and the kwargs carry the substrate. Join helper -> archetype -> kind.

    Resolving per CALL SITE rather than per function matters: one producer
    function emits several archetypes, and unioning across it gave four
    unrelated kinds an identical four-shape set.
    """
    if arg0 and arg0.startswith("archetype:"):
        # Substrate attached directly to a HomeCard. Prefer the literal in
        # the call; fall back to the enclosing builder's single archetype
        # (generic builders take `archetype` as a parameter).
        archetype = arg0.split(":", 1)[1] or helper_archetype.get(func, "")
        kind = archetype_kind.get(archetype)
        return {kind} if kind else set()

    helper = arg0
    if helper and helper not in helper_archetype:
        helper = assigns.get(func, {}).get(helper, helper)
    archetype = helper_archetype.get(helper or "")
    kind = archetype_kind.get(archetype or "")
    return {kind} if kind else set()


def substrate_map() -> dict:
    layouts: dict[str, set[str]] = defaultdict(set)
    calls: dict[str, set[str]] = defaultdict(set)
    archetypes: dict[str, set[str]] = defaultdict(set)
    builds_card: set[str] = set()
    assigns: dict[str, dict[str, str]] = defaultdict(dict)
    raw: list[tuple[str | None, dict[str, str | None], str, str, str | None]] = []

    for rel in PRODUCER_MODULES:
        body = read(AGENT / rel)
        if not body:
            continue
        index = _FuncIndex(rel)
        index.visit(ast.parse(body))
        for store, found in (
            (layouts, index.layouts),
            (calls, index.calls),
            (archetypes, index.archetypes),
        ):
            for func, values in found.items():
                store[func] |= values
        for func, bindings in index.assigns.items():
            assigns[func].update(bindings)
        builds_card |= index.builds_card
        raw.extend(index.cards)

    def resolved(func: str | None, depth: int = 4, seen: frozenset[str] = frozenset()) -> set[str]:
        """Follow the call graph from a substrate builder to its layout —
        build_settle_structured_from_transfers is three hops from the card."""
        if not func or depth <= 0 or func in seen:
            return set()
        out = set(layouts.get(func, ()))
        for callee in calls.get(func, ()):
            out |= resolved(callee, depth - 1, seen | {func})
        return out

    # archetype -> kind, from _attention_kind's mapping literal. This is the
    # join that rescues the seven kinds whose cards are built through
    # _home_card_to_concierge_card, where `kind` is computed, not written.
    src = read(AGENT / "backend/home/concierge_feed/producers.py")
    mapping = re.search(r"mapping:\s*dict\[str,\s*ConciergeHomeCardKind\]\s*=\s*\{(.*?)\n    \}", src, re.S)
    archetype_kind = dict(re.findall(r'"([a-z_]+)":\s*"([a-z_]+)"', mapping.group(1) if mapping else ""))
    # cards.py helper -> the archetype it stamps
    helper_archetype = {f: sorted(a)[0] for f, a in archetypes.items() if len(a) == 1}

    by_kind: dict[str, dict] = defaultdict(lambda: {"fields": set(), "layouts": set(), "funcs": set()})
    unresolved: list[str] = []

    for kind, fields, func, module, arg0 in raw:
        proxy = " " in module
        if proxy and _proxy_name(module) not in builds_card:
            continue  # an ordinary call that happens to take a `focus=` kwarg

        kinds = {kind} if kind else _kinds_via_archetype(
            arg0, func, assigns, helper_archetype, archetype_kind
        )
        if not kinds:
            if fields:
                unresolved.append(f"{_module_of(module)} :: {func}()")
            continue

        for resolved_kind in kinds:
            entry = by_kind[resolved_kind]
            entry["funcs"].add(func)
            entry["fields"] |= set(fields)
            for field, builder in fields.items():
                if field not in {"structured", "focus"}:
                    continue
                found = resolved(builder)
                if not found:
                    # A local: `brief_focus = build_brief_focus(...)`.
                    found = resolved(assigns.get(func, {}).get(builder or ""))
                if found:
                    entry["layouts"] |= found
                else:
                    # Deliberately NOT falling back to every builder the
                    # enclosing function touches — that credited planning_brief
                    # with ledger and call, which it never carries.
                    unresolved.append(
                        f"{_module_of(module)} :: {func}() — {field}={builder or '?'}"
                    )

    declared = literal_union(
        AGENT / "backend/home/concierge_feed/models.py", "ConciergeHomeCardKind"
    )
    required = set(
        re.findall(
            r'"([a-z_]+)"',
            re.search(
                r"DECK_REQUIRED_KINDS[^{]*\{(.*?)\}",
                read(AGENT / "backend/home/concierge_feed/models.py"),
                re.S,
            ).group(1),
        )
    )

    rows = []
    for kind in declared:
        entry = by_kind.get(kind, {"fields": set(), "layouts": set(), "funcs": set()})
        shapes: set[str] = {
            FIELD_RECEIPT[f] for f in entry["fields"] if f in FIELD_RECEIPT
        }
        dead: set[str] = set()
        for layout in entry["layouts"]:
            if layout in LAYOUT_RECEIPT:
                shapes.add(LAYOUT_RECEIPT[layout])
            elif layout in LAYOUT_NO_RECEIPT:
                dead.add(layout)
        rows.append(
            {
                "kind": kind,
                "deck_required": kind in required,
                "fields": sorted(entry["fields"]),
                "layouts": sorted(entry["layouts"]),
                "shapes": sorted(shapes),
                "projects_to_nothing": sorted(dead),
                "verdict": "SHAPED" if shapes else ("STARVED" if dead else "STAMP"),
            }
        )

    return {"rows": rows, "dynamic": sorted(set(unresolved))}


def substrate_report(result: dict) -> None:
    rows = result["rows"]
    print()
    print("=" * 78)
    print("SUBSTRATE PASS — what each stack kind can actually project")
    print("=" * 78)
    print("  Derived by walking the producers with ast, then applying")
    print("  trips_stack.py::_receipt_for_card's own branch order.")
    print()
    print("  SHAPED  — carries substrate that projects to a receipt.")
    print("  STARVED — carries substrate that projects to NOTHING. The")
    print("            producer did the work and no branch reads it.")
    print("  STAMP   — no substrate. Can only ever be title + kicker.")
    print("-" * 78)

    width = max(len(r["kind"]) for r in rows) + 2
    order = {"STARVED": 0, "SHAPED": 1, "STAMP": 2}
    for row in sorted(rows, key=lambda r: (order[r["verdict"]], r["kind"])):
        flag = "!" if row["deck_required"] and row["verdict"] == "STAMP" else " "
        shapes = ", ".join(row["shapes"]) or (
            "→ " + ", ".join(row["projects_to_nothing"]) if row["projects_to_nothing"] else "—"
        )
        print(f" {flag}{row['kind']:<{width}} {row['verdict']:<8} {shapes}")

    shapes_needed: set[str] = set()
    for row in rows:
        shapes_needed |= set(row["shapes"])
    stamps = [r["kind"] for r in rows if r["verdict"] == "STAMP"]
    starved = [r["kind"] for r in rows if r["verdict"] == "STARVED"]

    print("-" * 78)
    print(f"  {len(rows)} kinds collapse to {len(shapes_needed)} receipt shapes + stamp.")
    print(f"  shapes: {', '.join(sorted(shapes_needed))}")
    print(f"  stamp-only ({len(stamps)}): {', '.join(stamps)}")
    if starved:
        print(f"  ⚠ starved ({len(starved)}): {', '.join(starved)}")
        print("    substrate computed, no receipt branch reads it — fix the")
        print("    projection before drawing anything for these.")
    if result["dynamic"]:
        print()
        print("  Substrate attached where the kind could not be resolved")
        print("  statically — attribute these by hand before drawing:")
        for site in result["dynamic"]:
            print(f"    {site}")


# ---------------------------------------------------- composition pass
#
# The variant census asks "which projections exist". This asks the question
# one level out: what does a root actually COMPOSE, in what order, and under
# what guard? Ordering and conditionality are the product on a home surface,
# and neither is visible from a type union.
#
# The reachability question has a proven precedent. ColdHome was deleted on
# 2026-07-31 with a comment explaining that its branch could never run —
# `starter` is unconditionally lead-queue-eligible, so `stackCrown` is truthy
# on a bare account before the else-branch is reached. That class of dead
# branch is what the crownless-only column below is for.
#
# JSX has no ast module here, so this is an indentation-and-guard-stack scan
# over prettier-formatted source. It is a reading aid, not a compiler: the
# guard chain it prints is the evidence, and it prints line numbers so every
# row can be checked by hand.

ROOTS = {
    "trips": "app/(tabs)/trips/index.tsx",
    "places": "app/(tabs)/places/index.tsx",
    "vesper": "app/(tabs)/concierge/index.tsx",
}

# Components that are layout or text plumbing, not composition.
COMPOSITION_SKIP = {
    "View", "Text", "ScrollView", "SafeAreaView", "Pressable", "Fragment",
    "VText", "Tap", "Ionicons", "RefreshControl", "ActivityIndicator",
    "TouchableOpacity", "Image", "Animated", "KeyboardAvoidingView",
}

_GUARD_OPEN = re.compile(r"^\s*\{?\s*(.+?)\s*(?:\?|&&)\s*\(?\s*$")
_ELSE_ARM = re.compile(r"^\s*\)\s*:\s*(?:\{?\s*(.+?)\s*\?\s*\(?)?\s*$")
# `(?<![A-Za-z0-9_])` before the `<` so a generic type parameter is not read
# as a JSX tag: `Partial<Record<HeroKind, string>>` and
# `useMemo<ReturnedDeskItem[]>` each matched three "components" without it.
_RENDER = re.compile(r"(?<![A-Za-z0-9_])<([A-Z][A-Za-z0-9_]*)")


def composition(root_key: str) -> dict:
    rel = ROOTS[root_key]
    path = APP / rel
    src = read(path)
    if not src:
        return {"root": rel, "rows": [], "imports": {}}

    imports: dict[str, str] = {}
    for match in re.finditer(r"import\s+(?:\{([^}]*)\}|(\w+))[^;]*?from\s+[\"']([^\"']+)[\"']", src, re.S):
        names = match.group(1) or match.group(2) or ""
        for name in re.findall(r"[A-Z][A-Za-z0-9_]*", names):
            imports[name] = match.group(3)

    rows: list[dict] = []
    stack: list[tuple[int, str]] = []  # (indent, guard)
    seen: set[str] = set()

    for lineno, line in enumerate(src.split("\n"), 1):
        if not line.strip() or line.strip().startswith(("//", "*", "/*")):
            continue
        indent = len(line) - len(line.lstrip())

        # The else-arm MUST be handled before the pop loop. `) : x ? (` sits
        # at the same indent as the `{cond ? (` that opened the branch, whose
        # stack entry was pushed at indent+2 — so popping first discards the
        # guard we are about to negate, and every crownless-only branch reads
        # as unguarded.
        # indent+2 is the first arm (pushed by `{cond ? (`); indent+4 is any
        # later arm of a CHAINED ternary `a ? A : b ? B : c ? C`. Accepting
        # only indent+2 stopped accumulating after the first `:`, so a
        # third-arm component printed the negation of arm one as its whole
        # guard — evidence that did not match the code.
        else_arm = _ELSE_ARM.match(line)
        if else_arm and stack and stack[-1][0] in (indent + 2, indent + 4):
            open_indent, open_guard = stack[-1]
            negated = open_guard if open_guard.startswith("!") else "!" + open_guard
            stack[-1] = (open_indent, negated)
            if else_arm.group(1):
                # indent+2, matching where the arm's CONTENT sits. Pushing at
                # indent+4 put the guard below its own children, so the pop
                # loop dropped it on the very next line and every arm past
                # the first vanished from the chain.
                stack.append((indent + 2, else_arm.group(1).strip()))
            continue

        while stack and indent < stack[-1][0]:
            stack.pop()

        guard_open = _GUARD_OPEN.match(line)
        if guard_open and "<" not in line and "=>" not in line:
            expr = guard_open.group(1).lstrip("{").strip()
            if expr and len(expr) < 90:
                stack.append((indent + 2, expr))
                continue

        for name in _RENDER.findall(line):
            if name in COMPOSITION_SKIP or name in seen:
                continue
            seen.add(name)
            chain = [g for _, g in stack]
            rows.append(
                {
                    "order": len(rows) + 1,
                    "component": name,
                    "line": lineno,
                    "guards": chain,
                    "source": imports.get(name, "—"),
                    "generation": _generation(chain),
                    "crownless_only": any(
                        g.startswith("!") and "stackCrown" in g for g in chain
                    ),
                }
            )

    return {"root": rel, "rows": rows, "imports": imports}


def _generation(chain: list[str]) -> str:
    """Derived, not hand-labelled: the guard says which generation owns it.

    A component admitted by `heroKind === …` IS the legacy cascade; one
    admitted by a stackCrown test belongs to the ranked model; one with no
    guard at all is standing furniture that renders on every visit.
    """
    if any("heroKind ===" in g for g in chain):
        return "legacy-cascade"
    # Only a POSITIVE stackCrown test means the ranked model owns the slot.
    # Matching the raw string counted `!stackCrown` too, which filed the
    # group-planning standfirst arm — a crownless fallback — as ranked-stack.
    if any("stackCrown" in g for g in chain if not g.startswith("!")):
        return "ranked-stack"
    if any(g.startswith("!") and "stackCrown" in g for g in chain):
        return "crownless"
    if not chain:
        return "always"
    return "conditional"


def composition_report(result: dict, verbose: bool = False) -> None:
    rows = result["rows"]
    print()
    print("=" * 78)
    print(f"COMPOSITION — {result['root']}")
    print("=" * 78)
    print("  What the root renders, in source order, and the guard that")
    print("  admits it. Generation is derived from the guard, not labelled.")
    print("-" * 78)

    width = max((len(r["component"]) for r in rows), default=10) + 2
    for row in rows:
        flag = "!" if row["crownless_only"] else " "
        print(f" {flag}{row['order']:>3}  {row['component']:<{width}} {row['generation']:<15} :{row['line']}")
        if verbose and row["guards"]:
            for guard in row["guards"]:
                print(f"      {'':<{width}} └ {guard[:70]}")

    print("-" * 78)
    counts: dict[str, int] = defaultdict(int)
    for row in rows:
        counts[row["generation"]] += 1
    print("  " + "   ".join(f"{k} {v}" for k, v in sorted(counts.items())))

    crownless = [r["component"] for r in rows if r["crownless_only"]]
    if crownless:
        print()
        print(f"  ⚠ Renders ONLY when there is no crown ({len(crownless)}):")
        print(f"    {', '.join(crownless)}")
        print("    ColdHome was deleted from this exact branch on 2026-07-31")
        print("    as unreachable. Re-check each of these the same way before")
        print("    designing anything for them.")


# ---------------------------------------------------------------- report

BUCKETS = ("LIVE", "INVISIBLE", "CAPACITY", "ORPHAN")


def report(axes: list[Axis], verbose: bool = False) -> None:
    for axis in axes:
        counts = {b: sum(1 for v in axis.variants if v.verdict == b) for b in BUCKETS}
        print()
        print("=" * 78)
        kind = "visual axis" if axis.visual else "semantic axis"
        print(f"{axis.surface.upper()} — {axis.axis}  ({len(axis.variants)} declared, {kind})")
        print(f"  source: {axis.source}")
        if axis.mechanism:
            for i, line in enumerate(_wrap(axis.mechanism, 68)):
                print(f"  {'render:' if i == 0 else '       '} {line}")
        print("-" * 78)
        width = max((len(v.name) for v in axis.variants), default=10) + 2
        for variant in sorted(axis.variants, key=lambda v: (BUCKETS.index(v.verdict), v.name)):
            produced = "yes" if variant.produced_in else " — "
            drawn = "yes" if variant.dispatched_in else " — "
            print(
                f"  {variant.name:<{width}} produced {produced}   "
                f"dispatched {drawn}   {variant.verdict}"
            )
            # Every verdict is auditable. This census under-reported four
            # axes on its first run because emission mechanisms differ per
            # axis; printing the evidence is how that stays visible.
            if verbose:
                for label, sites in (("produced", variant.produced_in), ("drawn", variant.dispatched_in)):
                    for site in sites:
                        print(f"  {'':<{width}}   {label:<9} {site}")
        print("-" * 78)
        print("  " + "   ".join(f"{b} {counts[b]}" for b in BUCKETS))


def _wrap(text: str, width: int) -> list[str]:
    words, lines, line = text.split(), [], ""
    for word in words:
        if len(line) + len(word) + 1 > width:
            lines.append(line)
            line = word
        else:
            line = f"{line} {word}".strip()
    if line:
        lines.append(line)
    return lines


def summary(axes: list[Axis]) -> None:
    print()
    print("=" * 78)
    print("CENSUS SUMMARY")
    print("=" * 78)
    total = {b: 0 for b in BUCKETS}
    for axis in axes:
        for variant in axis.variants:
            total[variant.verdict] += 1
    print(f"  {sum(total.values())} declared variants across {len(axes)} axes")
    for bucket in BUCKETS:
        print(f"    {bucket:<10} {total[bucket]}")
    print()
    print("  Drawings the board needs, in priority order:")
    print("    1. INVISIBLE — produced, unrendered. Real data with no shape.")
    print("    2. LIVE      — has a shape; draw to check the family coheres.")
    print("    3. CAPACITY  — rule near-term-or-retire BEFORE spending a drawing.")
    print("       ORPHAN    — not a drawing. A renderer with no producer is a bug.")


def to_json(axes: list[Axis]) -> dict:
    return {
        "generated_from": "code",
        "workspace": WORKSPACE.as_posix(),
        "axes": [
            {
                "surface": axis.surface,
                "axis": axis.axis,
                "source": axis.source,
                "render_mechanism": axis.mechanism,
                "variants": [
                    {
                        "name": v.name,
                        "verdict": v.verdict,
                        "declared": v.declared,
                        "produced_in": v.produced_in,
                        "dispatched_in": v.dispatched_in,
                        "note": v.note,
                    }
                    for v in axis.variants
                ],
            }
            for axis in axes
        ],
    }


def _mechanism(axis: Axis, mechanism: str) -> Axis:
    axis.mechanism = mechanism
    return axis


def _semantic(axis: Axis, mechanism: str) -> Axis:
    """Mark an axis as semantic — dispatch is reported but not scored."""
    axis.visual = False
    axis.mechanism = mechanism
    axis.__post_init__()
    return axis


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", metavar="PATH", help="write the census as JSON (board input)")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="print the evidence file for every verdict"
    )
    parser.add_argument(
        "--substrate",
        action="store_true",
        help="one level down: what each stack kind can project, and how many shapes that is",
    )
    parser.add_argument(
        "--composition",
        action="store_true",
        help="one level out: what a root renders, in order, under which guard",
    )
    parser.add_argument(
        "--surface",
        choices=["trips", "places", "vesper"],
        action="append",
        help="limit to one surface (repeatable)",
    )
    args = parser.parse_args()

    if not AGENT.exists() or not APP.exists():
        print(f"error: expected both repos under {WORKSPACE}", file=sys.stderr)
        return 2

    builders = {
        "trips": [trips_stack_kinds, trips_receipt_kinds, trips_plan_kind],
        "places": [
            lambda: _semantic(
                places_axis(
                    "PlacesSectionReason",
                    "section reason",
                    "reason",
                    [re.compile(r'reason\s*===\s*[\'"]([a-z_]+)[\'"]')],
                ),
                "Semantic, not visual. Reason drives the section label and the "
                "server-side ordering; treatment drives the shape. A reason "
                "with no frontend branch is correct, not a gap.",
            ),
            lambda: _mechanism(
                places_axis(
                    "PlacesSectionTreatment",
                    "treatment",
                    "treatment",
                    [re.compile(r'treatment\s*===\s*[\'"]([a-z_]+)[\'"]')],
                ),
                "treatmentStyle() branches for fork and conviction and returns "
                "nothing for single and choice — so the two treatments that "
                "actually ship render as the DEFAULT, which is their intended "
                "shape, while the two with bespoke styling have no producer. "
                "Read INVISIBLE here as 'default-rendered', not 'unstyled'.",
            ),
            places_card_kinds,
        ],
        "vesper": [vesper_list_kinds],
    }

    if args.composition:
        results = [composition(k) for k in (args.surface or ["trips"])]
        for result in results:
            composition_report(result, verbose=args.verbose)
        if args.json:
            out = Path(args.json)
            out.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
            print(f"\n  wrote {out}")
        return 0

    if args.substrate:
        result = substrate_map()
        substrate_report(result)
        if args.json:
            out = Path(args.json)
            out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
            print(f"\n  wrote {out}")
        return 0

    wanted = args.surface or ["trips", "places", "vesper"]
    axes = [build() for surface in wanted for build in builders[surface]]

    report(axes, verbose=args.verbose)
    summary(axes)

    if args.json:
        out = Path(args.json)
        out.write_text(json.dumps(to_json(axes), indent=2) + "\n", encoding="utf-8")
        print(f"\n  wrote {out}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
