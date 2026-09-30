"""Exercise the real aggregate scripts with success, failure and skip inputs."""
import json
import os
from pathlib import Path
import subprocess

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[2]


@pytest.mark.parametrize("repo,command,delimiter", [
    ("travel-agent", "python3", "PY"),
    ("travel-app", "node", "JS"),
])
@pytest.mark.parametrize("mode,broken", [
    ("scoped", None), ("docs", None),
    ("scoped", "failure"), ("scoped", "cancelled"),
    ("scoped", "skipped"), ("docs", "bad-scope"),
])
def test_aggregate_requires_the_selected_jobs(repo, command, delimiter, mode, broken):
    workflow = yaml.load((ROOT / repo / ".github/workflows/merge-ready.yml").read_text(), Loader=yaml.BaseLoader)
    aggregate = workflow["jobs"]["ready"]
    assert aggregate["if"] == "always()"
    script = aggregate["steps"][0]["run"].split("\n", 1)[1].rsplit(f"\n{delimiter}", 1)[0]
    expected = "skipped" if mode == "docs" else "success"
    needs = {"scope": {"result": "success", "outputs": {"mode": mode, "database": "false"}},
             "static": {"result": expected}, "tests": {"result": expected}}
    if repo == "travel-agent":
        needs["database"] = {"result": "skipped"}
    if broken == "bad-scope":
        needs["scope"]["result"] = "failure"
    elif broken:
        needs["tests"]["result"] = broken
    args = [command, "-c", script] if command == "python3" else [command, "--input-type=module", "-e", script]
    result = subprocess.run(args, env={**os.environ, "RESULTS": json.dumps(needs)}, capture_output=True, text=True)
    assert (result.returncode == 0) == (broken is None), result.stderr


def test_full_backend_suites_do_not_duplicate_their_marker_partitions():
    workflow = yaml.load((ROOT / "travel-agent/.github/workflows/ci.yml").read_text(), Loader=yaml.BaseLoader)
    offline = [s["run"] for s in workflow["jobs"]["test"]["steps"] if "pytest" in s.get("run", "")]
    database = [s["run"] for s in workflow["jobs"]["test-db"]["steps"] if "pytest" in s.get("run", "")]
    assert len(offline) == len(database) == 1
    assert 'not requires_postgres and not requires_api_keys and not requires_dogfood_wedge' in offline[0]
    assert '(requires_postgres or requires_dogfood_wedge) and not requires_api_keys' in database[0]
