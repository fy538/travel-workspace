#!/usr/bin/env python3
"""Validate the frozen Life composition fixture used by visual and native labs."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURE_V1 = (
    ROOT
    / "docs/working/fixtures/life-composition/life-composition-fixtures-v0.1.json"
)
FIXTURE_V2 = (
    ROOT
    / "docs/working/fixtures/life-composition/life-composition-fixtures-v0.2.json"
)


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def validate_v2(errors: list[str]) -> tuple[int, int, int, int]:
    data = json.loads(FIXTURE_V2.read_text())
    require(
        data.get("schema_version") == "vesper.life-composition-fixtures.v0.2",
        "v0.2 has unexpected schema_version",
        errors,
    )
    require(
        data.get("status") == "content_complete_for_hybrid_composition",
        "v0.2 is not ready for hybrid composition",
        errors,
    )
    require(
        data.get("base_fixture", "").endswith("life-composition-fixtures-v0.1.json"),
        "v0.2 must preserve v0.1 as its explicit base fixture",
        errors,
    )

    lane_ids = {lane["lane_id"] for lane in data["lane_vocabulary"]}
    require(len(lane_ids) == 6, "v0.2 must define six optional lane semantics", errors)
    require(
        all(not lane["global_tab"] for lane in data["lane_vocabulary"]),
        "v0.2 lanes must not become global tabs",
        errors,
    )

    clusters = {cluster["cluster_id"]: cluster for cluster in data["period_clusters"]}
    expected_clusters = {
        "CLU-2026-08-EUROPE",
        "CLU-2026-BROOKLYN-DINNER",
        "CLU-RED-HOOK-EPISODES",
    }
    require(set(clusters) == expected_clusters, "v0.2 cluster portfolio is incomplete", errors)
    for cluster_id, cluster in clusters.items():
        missing_lanes = set(cluster["lanes"]) - lane_ids
        require(not missing_lanes, f"{cluster_id} references unknown lanes: {sorted(missing_lanes)}", errors)

    thread_ids = {thread["thread_id"] for thread in data["thread_candidates"]}
    require(
        thread_ids == {"THR-RED-HOOK-ACCESS", "THR-PASTA-MECHANISM", "THR-ROME-PARIS"},
        "v0.2 thread portfolio is incomplete",
        errors,
    )
    threads = {thread["thread_id"]: thread for thread in data["thread_candidates"]}
    require(
        threads["THR-PASTA-MECHANISM"]["status"] == "ineligible_single_observation",
        "pasta must remain nested until a second supported cluster",
        errors,
    )
    require(
        threads["THR-ROME-PARIS"]["status"] == "ineligible_as_thread",
        "one social comparison must not become a longitudinal thread",
        errors,
    )

    source_contract_ids = {
        source["source_contract_id"] for source in data["external_source_contracts"]
    }
    contributions = {
        contribution["contribution_id"]: contribution
        for contribution in data["contribution_briefs"]
    }
    require(set(contributions) == {f"C0{i}" for i in range(1, 6)}, "v0.2 requires C01-C05", errors)
    require(
        contributions["C03"]["status"] == "withheld_missing_authorized_comparable_evidence",
        "C03 must remain withheld under the current placeholder grant",
        errors,
    )
    require(
        contributions["C05"]["status"] == "admitted_nested_not_thread",
        "C05 must be admitted only as a nested explanation",
        errors,
    )
    for contribution_id, contribution in contributions.items():
        for field in (
            "operation",
            "known_to_person",
            "new_value",
            "proof",
            "uncertainty",
            "why_now",
            "silence_condition",
            "treatment_verdict",
        ):
            require(
                bool(contribution.get(field)),
                f"{contribution_id} lacks contribution-brief field {field}",
                errors,
            )
        external_refs = {
            proof for proof in contribution["proof"] if proof.startswith("EXT-")
        }
        missing_refs = external_refs - source_contract_ids
        require(
            not missing_refs,
            f"{contribution_id} references unknown external contracts: {sorted(missing_refs)}",
            errors,
        )

    map_contexts = {
        context["map_context_id"]: context for context in data["spatial_contexts"]
    }
    require(
        set(map_contexts) == {"MAP-RED-HOOK-ACCESS", "MAP-ROME-LOCAL-OPTIONAL"},
        "v0.2 must keep spatial contexts bounded",
        errors,
    )
    require(
        all("world_heatmap" in context["prohibited"] or "trip_city_map_as_decoration" in context["prohibited"] for context in map_contexts.values()),
        "each spatial context must explicitly prohibit decorative global geography",
        errors,
    )

    projections = {projection["projection_id"] for projection in data["textual_projections"]}
    require(
        projections == {"TXT-I-01", "TXT-E-01", "TXT-E-05", "TXT-E-07"},
        "v0.2 textual projection portfolio is incomplete",
        errors,
    )
    require(
        "C03" in data["page_admission"]["cluster_europe"]["suppress"],
        "Europe cluster must encode C03 silence",
        errors,
    )

    exposure_keys = {receipt["exposure_key"] for receipt in data["exposure_receipts"]}
    for contribution in contributions.values():
        if contribution.get("exposure_key"):
            require(
                contribution["exposure_key"] in exposure_keys,
                f"{contribution['contribution_id']} references an unknown exposure receipt",
                errors,
            )

    return len(clusters), len(thread_ids), len(contributions), len(projections)


def main() -> int:
    errors: list[str] = []
    data = json.loads(FIXTURE_V1.read_text())

    require(
        data.get("schema_version") == "vesper.life-composition-fixtures.v0.1",
        "unexpected schema_version",
        errors,
    )
    require(
        data.get("status") == "frozen_for_visual_round_1",
        "fixture is not frozen for visual round 1",
        errors,
    )

    source_ids = [source["source_id"] for source in data["source_catalog"]]
    require(len(source_ids) == len(set(source_ids)), "duplicate source_id", errors)
    source_set = set(source_ids)

    worlds = {world["world_id"]: world for world in data["worlds"]}
    require(set(worlds) == {f"L{i:02d}" for i in range(1, 7)}, "worlds must be L01-L06", errors)
    for world_id, world in worlds.items():
        missing = set(world["source_ids"]) - source_set
        require(not missing, f"{world_id} references unknown Sources: {sorted(missing)}", errors)

    require(
        worlds["L01"]["stable_door_eligibility"] == "eligible_in_rich_state",
        "L01 rich state must be stable-door eligible",
        errors,
    )
    require(
        worlds["L02"]["stable_door_eligibility"] == "eligible",
        "L02 must be stable-door eligible",
        errors,
    )
    require(
        worlds["L03"]["stable_door_eligibility"] == "ineligible",
        "L03 must remain ineligible for a stable door",
        errors,
    )
    require(
        worlds["L05"]["default_posture"] == "contextual",
        "L05 must remain contextual",
        errors,
    )
    require(
        worlds["L06"]["stable_door_eligibility"] == "eligible_after_supported_recurrence",
        "L06 eligibility must require supported recurrence",
        errors,
    )

    index_projections = {item["projection_id"]: item for item in data["index_projections"]}
    expected_indexes = {
        "IDX-RICH-COMBINED",
        "IDX-RICH-MINE",
        "IDX-RICH-TOGETHER",
        "IDX-QUIET-MATURE",
        "IDX-SPARSE-NEW",
        "IDX-SEARCH-L03",
    }
    require(set(index_projections) == expected_indexes, "index projection portfolio is incomplete", errors)

    combined = index_projections["IDX-RICH-COMBINED"]
    section_items = {
        item
        for section in combined["sections"]
        for item in section.get("items", [])
    }
    for stable_id in ("JRN-L01-EUROPE", "OCC-L02-DINNER", "PLREL-L06-RED-HOOK"):
        require(stable_id in section_items, f"combined index omits stable door {stable_id}", errors)

    nested = {item["resource_id"] for item in combined["nested_memberships"]}
    require(
        nested == {"PLN-L03-MUSEUM", "REL-L04-FILM-ROME", "CMP-L05-ROME-PARIS"},
        "combined index must preserve L03-L05 subordinate memberships",
        errors,
    )

    identities: list[tuple[str, str, str, str, str]] = []
    for item in data["index_projections"] + data["episode_projections"]:
        identity = item["projection_identity"]
        for field in ("resource_id", "revision", "viewer_id", "audience_epoch", "schema_version"):
            require(bool(identity.get(field)), f"{item.get('projection_id', item.get('episode_id'))} missing {field}", errors)
        identities.append(tuple(identity[field] for field in ("resource_id", "revision", "viewer_id", "audience_epoch", "schema_version")))
    require(len(identities) == len(set(identities)), "duplicate complete projection identity", errors)

    episodes = {item["world_id"]: item for item in data["episode_projections"]}
    require(set(episodes) == {"L01", "L02", "L06"}, "full episode portfolio must be L01, L02, and L06", errors)
    anatomy = {
        "identity_truth",
        "episode_skeleton",
        "occurred_story_spine",
        "plans_changes_unresolved",
        "people_contributions",
        "sources_in_place",
        "see_anew",
        "continue_repair",
    }
    for world_id, episode in episodes.items():
        section_ids = {section["section_id"] for section in episode["anatomy"]}
        require(section_ids == anatomy, f"{world_id} does not implement all eight anatomy regions", errors)

    compositions = {item["composition_id"]: item for item in data["derived_compositions"]}
    for composition_id, composition in compositions.items():
        missing = set(composition["source_ids"]) - source_set
        require(not missing, f"{composition_id} references unknown Sources: {sorted(missing)}", errors)
        require(bool(composition.get("substance_requirement")), f"{composition_id} lacks substance requirement", errors)
        require(bool(composition.get("suppression_reason_if_unmet")), f"{composition_id} lacks silence condition", errors)

    transitions = {item["transition_id"] for item in data["social_transitions"]}
    require(transitions == {f"S{i:02d}" for i in range(1, 15)}, "social transitions must be S01-S14", errors)

    frames = {item["frame_id"]: item for item in data["visual_frames"]}
    expected_frames = {f"I-{i:02d}" for i in range(1, 7)} | {f"E-{i:02d}" for i in range(1, 9)}
    require(set(frames) == expected_frames, "visual frame portfolio must be I-01-I-06 and E-01-E-08", errors)
    projection_refs = set(index_projections) | {item["episode_id"] for item in data["episode_projections"]}
    for frame_id, frame in frames.items():
        require(frame["fixture_ref"] in projection_refs, f"{frame_id} references unknown fixture {frame['fixture_ref']}", errors)

    around = index_projections["IDX-SEARCH-L03"]["around_this"]
    require(len(around) <= 3, "Around this exceeds the three-landmark default", errors)
    require("SRC-L03-CORRECTION" in around, "L03 search omits the occurrence correction", errors)

    v2_clusters, v2_threads, v2_contributions, v2_projections = validate_v2(errors)

    if errors:
        for error in errors:
            print(f"life-composition-fixture: {error}", file=sys.stderr)
        print(f"life-composition-fixture FAILED: {len(errors)} issue(s)", file=sys.stderr)
        return 1

    print(
        "life-composition-fixture OK: "
        f"{len(worlds)} worlds, {len(index_projections)} indexes, "
        f"{len(episodes)} full episodes, {len(compositions)} compositions, "
        f"{len(transitions)} social transitions, {len(frames)} visual frames; "
        f"v0.2 adds {v2_clusters} clusters, {v2_threads} thread candidates, "
        f"{v2_contributions} contribution briefs, and {v2_projections} textual projections"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
