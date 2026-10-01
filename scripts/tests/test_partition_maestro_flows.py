from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partition_maestro_flows import list_maestro_flows, partition_flows  # noqa: E402


def test_four_shards_are_stable_disjoint_and_cover_every_flow(tmp_path: Path) -> None:
    flows = [f".maestro/nested/flow-{index:03}.yaml" for index in range(17)]
    app_dir = tmp_path / "travel-app"
    for flow in flows:
        path = app_dir / flow
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("{}")  # Contents are irrelevant to inventory selection.

    selected = [partition_flows(list_maestro_flows(app_dir), shard, 4) for shard in range(4)]
    flattened = [path for shard in selected for path in shard]

    assert sorted(flattened) == flows
    assert len(flattened) == len(set(flattened))
    assert [len(shard) for shard in selected] == [5, 4, 4, 4]
    assert selected == [partition_flows(flows, shard, 4) for shard in range(4)]


def test_inventory_matches_wrapper_yaml_and_config_selection(tmp_path: Path) -> None:
    maestro = tmp_path / ".maestro"
    (maestro / "flows/nested").mkdir(parents=True)
    for name in ["a.yaml", "b.yml", "config.pr.yaml", "config-local.yml"]:
        (maestro / name).write_text("input")
    (maestro / "flows/nested/c.yaml").write_text("input")
    (maestro / "notes.txt").write_text("not a flow")

    assert list_maestro_flows(tmp_path) == [
        ".maestro/a.yaml",
        ".maestro/b.yml",
        ".maestro/config-local.yml",
        ".maestro/flows/nested/c.yaml",
    ]


@pytest.mark.parametrize(
    ("shard", "shard_count", "message"),
    [(-1, 4, "between 0 and 3"), (4, 4, "between 0 and 3"), (0, 0, "at least one")],
)
def test_invalid_shard_definition_fails(shard: int, shard_count: int, message: str) -> None:
    with pytest.raises(ValueError, match=message):
        partition_flows(["a.yaml"], shard, shard_count)


def test_empty_partition_fails_instead_of_skipping_expected_work() -> None:
    with pytest.raises(ValueError, match="is empty"):
        partition_flows(["only-flow.yaml"], 1, 4)


def test_missing_inventory_fails_closed(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="No .maestro directory"):
        list_maestro_flows(tmp_path)


def test_cli_emits_the_selected_inventory_for_nul_delimited_xargs(tmp_path: Path) -> None:
    app_dir = tmp_path / "travel-app"
    for name in ["a.yaml", "b.yaml", "c.yaml", "d.yaml"]:
        path = app_dir / ".maestro" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("flow")
    script = Path(__file__).resolve().parents[1] / "partition_maestro_flows.py"

    result = subprocess.run(
        [sys.executable, str(script), "--app-dir", str(app_dir), "--shard", "2",
         "--shards", "4", "--nul-delimited"],
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr.decode()
    assert result.stdout.split(b"\0")[:-1] == [b".maestro/c.yaml"]
    assert b"1 of 4 flow files" in result.stderr


def test_missing_maestro_executable_fails_the_syntax_pipeline(tmp_path: Path) -> None:
    app_dir = tmp_path / "travel-app"
    flow = app_dir / ".maestro/one.yaml"
    flow.parent.mkdir(parents=True)
    flow.write_text("flow")
    script = Path(__file__).resolve().parents[1] / "partition_maestro_flows.py"
    command = (
        f"python3 {script} --app-dir {app_dir} --shard 0 --shards 1 --nul-delimited "
        "| xargs -0 -n 1 maestro check-syntax"
    )
    result = subprocess.run(
        ["bash", "-e", "-o", "pipefail", "-c", command],
        env={**os.environ, "PATH": os.pathsep.join([str(Path(sys.executable).parent), "/usr/bin", "/bin"])},
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode != 0
    assert "maestro" in result.stderr.lower()
