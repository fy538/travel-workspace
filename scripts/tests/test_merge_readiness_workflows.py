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


def test_workspace_real_journeys_have_an_explicit_disposable_database():
    workflow = yaml.load((ROOT / ".github/workflows/reliability.yml").read_text(), Loader=yaml.BaseLoader)
    job = workflow["jobs"]["contract-and-golden-path"]
    env = job["env"]
    assert env["TEST_DATABASE_DISPOSABLE"] == "1"
    assert env["TEST_DATABASE_URL"] == env["DATABASE_URL"]
    assert "@localhost:5432/vesper" in env["TEST_DATABASE_URL"]
    database = job["services"]["postgres"]
    assert database["env"]["POSTGRES_DB"] == "vesper"
    assert database["ports"] == ["5432:5432"]
    steps = job["steps"]
    migration = next(i for i, step in enumerate(steps)
                     if step.get("run") == "PYTHONPATH=. alembic upgrade head")
    journey = next(i for i, step in enumerate(steps)
                   if step.get("run") == "make golden-path-qa")
    assert migration < journey
    assert steps[migration]["working-directory"] == "travel-agent"


@pytest.mark.parametrize("repo,broad,retained", [
    ("travel-agent", ("test", "test-db"),
     ("lint", "import-boundaries", "typecheck", "test-db-migrate", "dogfood-persona-gate", "eval-replay", "package-smoke")),
    ("travel-app", ("test", "logic-qa"),
     ("lint", "frontend-governance", "security", "visual-evidence", "typecheck", "contract-types", "qa-tooling", "design-gate")),
])
def test_broad_regression_moves_off_prs_without_disabling_fast_checks(repo, broad, retained):
    workflow = yaml.load((ROOT / repo / ".github/workflows/ci.yml").read_text(), Loader=yaml.BaseLoader)
    assert workflow["on"]["push"]["branches"] == ["main"]
    assert workflow["on"]["schedule"]
    assert "workflow_dispatch" in workflow["on"]
    assert workflow["on"]["pull_request"]["branches"] == ["main"]
    for job in broad:
        assert workflow["jobs"][job]["if"] == "github.event_name != 'pull_request'"
    for job in retained:
        assert "if" not in workflow["jobs"][job], job
