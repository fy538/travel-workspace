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


def test_workspace_merge_readiness_plans_before_conditional_installs():
    workflow = yaml.load(
        (ROOT / ".github/workflows/merge-ready.yml").read_text(), Loader=yaml.BaseLoader
    )
    steps = workflow["jobs"]["ready"]["steps"]
    plan = next(i for i, step in enumerate(steps) if step.get("id") == "plan")
    python_setup = next(
        i
        for i, step in enumerate(steps)
        if step.get("uses", "").startswith("actions/setup-python")
    )
    node_setup = next(
        i
        for i, step in enumerate(steps)
        if step.get("uses", "").startswith("actions/setup-node")
    )
    verify = next(
        i
        for i, step in enumerate(steps)
        if step.get("run", "").startswith(
            "python3 scripts/verify_changed.py --workspace-only"
        )
    )
    assert plan < python_setup < verify
    assert plan < node_setup < verify
    assert "--dry-run --plan-json" in steps[plan]["run"]
    assert steps[python_setup]["if"] == "steps.plan.outputs.travel_agent == 'true'"
    assert steps[node_setup]["if"] == "steps.plan.outputs.travel_app == 'true'"
    for step in steps:
        if step.get("run", "").startswith("pip install -r travel-agent/"):
            assert step["if"] == "steps.plan.outputs.travel_agent == 'true'"
        if step.get("run", "").startswith("npm ci --prefix travel-app"):
            assert step["if"] == "steps.plan.outputs.travel_app == 'true'"


def test_workspace_real_journeys_have_an_explicit_disposable_database():
    workflow = yaml.load((ROOT / ".github/workflows/reliability.yml").read_text(), Loader=yaml.BaseLoader)
    job = workflow["jobs"]["workspace-checks"]
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


def test_reliability_required_check_aggregates_workspace_and_matrix_jobs():
    workflow = yaml.load((ROOT / ".github/workflows/reliability.yml").read_text(), Loader=yaml.BaseLoader)
    jobs = workflow["jobs"]
    aggregate = jobs["contract-and-golden-path"]
    assert aggregate["name"] == "Contract and golden paths"
    assert aggregate["if"] == "always()"
    assert aggregate["needs"] == ["workspace-checks", "maestro-flow-validation"]
    gate = next(step for step in aggregate["steps"] if step.get("name", "").startswith("Require workspace checks"))
    assert gate["env"]["NEEDS_JSON"] == "${{ toJSON(needs) }}"
    assert gate["run"] == "python3 scripts/require_successful_jobs.py workspace-checks maestro-flow-validation"


@pytest.mark.parametrize("workspace,maestro", [
    ("success", "success"),
    ("failure", "success"),
    ("success", "failure"),
    ("cancelled", "success"),
    ("success", "cancelled"),
    ("skipped", "success"),
    ("success", "skipped"),
])
def test_reliability_required_check_fails_closed_for_dependency_results(workspace, maestro):
    gate = ROOT / "scripts/require_successful_jobs.py"
    needs = {"workspace-checks": {"result": workspace},
             "maestro-flow-validation": {"result": maestro}}
    result = subprocess.run(
        ["python3", str(gate), "workspace-checks", "maestro-flow-validation"],
        env={**os.environ, "NEEDS_JSON": json.dumps(needs)},
        capture_output=True,
        text=True,
        check=False,
    )
    assert (result.returncode == 0) == (workspace == "success" and maestro == "success"), result.stderr


@pytest.mark.parametrize("needs", [
    {},
    {"workspace-checks": {"result": "success"}},
    {"workspace-checks": {"result": "success"}, "maestro-flow-validation": {}},
])
def test_reliability_required_check_rejects_missing_jobs_or_results(needs):
    gate = ROOT / "scripts/require_successful_jobs.py"
    result = subprocess.run(
        ["python3", str(gate), "workspace-checks", "maestro-flow-validation"],
        env={**os.environ, "NEEDS_JSON": json.dumps(needs)},
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 1


def test_reliability_required_check_rejects_an_unreadable_needs_context():
    gate = ROOT / "scripts/require_successful_jobs.py"
    result = subprocess.run(
        ["python3", str(gate), "workspace-checks", "maestro-flow-validation"],
        env={**os.environ, "NEEDS_JSON": "not-json"},
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 2
    assert "invalid NEEDS_JSON" in result.stderr


def test_reliability_syntax_matrix_runs_all_four_full_checkout_shards():
    workflow = yaml.load((ROOT / ".github/workflows/reliability.yml").read_text(), Loader=yaml.BaseLoader)
    job = workflow["jobs"]["maestro-flow-validation"]
    assert job["strategy"]["fail-fast"] == "false"
    assert job["strategy"]["max-parallel"] == "4"
    assert job["strategy"]["matrix"]["shard"] == ["0", "1", "2", "3"]
    steps = job["steps"]
    checkouts = [step["with"] for step in steps if step.get("uses", "").startswith("actions/checkout")]
    assert any(checkout.get("path") == "travel-agent" for checkout in checkouts)
    app_checkout = next(checkout for checkout in checkouts if checkout.get("path") == "travel-app")
    assert app_checkout["fetch-depth"] == "0"
    cli = next(step for step in steps if step.get("name") == "Install pinned Maestro CLI")
    assert cli["env"]["MAESTRO_VERSION"] == "2.6.1"
    validation = next(step for step in steps if step.get("name") == "Validate this required syntax partition")
    assert "partition_maestro_flows.py" in validation["run"]
    assert "maestro check-syntax" in validation["run"]
    assert "xargs -0 -n 1" in validation["run"]
    assert "install frontend dependencies" not in " ".join(str(step).lower() for step in steps)


def test_cheap_registry_checks_precede_frontend_installation():
    workflow = yaml.load((ROOT / ".github/workflows/reliability.yml").read_text(), Loader=yaml.BaseLoader)
    steps = workflow["jobs"]["workspace-checks"]["steps"]
    names = [step.get("name") for step in steps]
    install = names.index("Install frontend dependencies")
    for name in [
        "Require Qdrant readiness",
        "Maestro flow inventory validation",
        "New-document governance guard",
        "Documentation inventory coverage",
        "Canonical documentation spine and current-state drift",
        "API coverage check",
        "Journey-set registry guard",
        "Flag registry guard",
    ]:
        assert names.index(name) < install
    readiness = next(step for step in steps if step.get("name") == "Require Qdrant readiness")
    assert "/readyz" in readiness["run"]
    inventory = next(step for step in steps if step.get("name") == "Maestro flow inventory validation")
    assert inventory["run"] == "make maestro-flow-inventory-check"
    metadata = next(step for step in steps if step.get("name") == "Maestro flow metadata validation")
    assert metadata["run"] == "make maestro-flow-metadata-check"


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
