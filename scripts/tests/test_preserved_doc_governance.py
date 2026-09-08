import hashlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))
from check_child_doc_governance import preserved_artifact_findings
from check_doc_governance import validate


def fixture(tmp_path):
    docs = tmp_path / "docs"
    docs.mkdir()
    artifact = docs / "frozen.md"
    artifact.write_text("# Frozen external export\n")
    owner = docs / "owner.md"
    owner.write_text(
        "---\ndoc_type: working\nstatus: active\nowner: design\ncreated: 2026-09-07\nexpires: 2026-10-07\nwhy_new: Owns the lifecycle of the frozen external design source.\n---\n"
    )
    entry = {
        "path": "docs/frozen.md",
        "metadata_owner": "docs/owner.md",
        "reason": "Preserve externally authored bytes with independent lifecycle ownership",
        "sha256": hashlib.sha256(artifact.read_bytes()).hexdigest(),
    }
    return artifact, owner, entry


def test_frozen_bytes_have_valid_independent_owner(tmp_path):
    artifact, _, entry = fixture(tmp_path)
    assert not preserved_artifact_findings(tmp_path, entry)
    assert validate(artifact), (
        "an unregistered export still requires lifecycle metadata"
    )


def test_modified_or_missing_artifact_is_not_grandfathered(tmp_path):
    artifact, _, entry = fixture(tmp_path)
    artifact.write_text("changed")
    assert preserved_artifact_findings(tmp_path, entry)
    artifact.unlink()
    assert preserved_artifact_findings(tmp_path, entry)


def test_missing_invalid_or_self_owner_cannot_hide_metadata_failures(tmp_path):
    _, owner, entry = fixture(tmp_path)
    owner.write_text("invalid owner metadata")
    assert preserved_artifact_findings(tmp_path, entry)
    owner.unlink()
    assert preserved_artifact_findings(tmp_path, entry)
    entry["metadata_owner"] = entry["path"]
    assert preserved_artifact_findings(tmp_path, entry)


def test_registry_cannot_escape_document_tree(tmp_path):
    _, _, entry = fixture(tmp_path)
    entry["path"] = "../outside.md"
    assert preserved_artifact_findings(tmp_path, entry)
