from __future__ import annotations

from pathlib import Path

import run_required_pytest as subject


def test_skipped_cases_returns_test_identity_and_reason(tmp_path: Path) -> None:
    report = tmp_path / "junit.xml"
    report.write_text(
        """<?xml version=\"1.0\"?>
<testsuites><testsuite><testcase classname=\"tests.test_gate\" name=\"test_required\">
<skipped message=\"database is behind migrations\" />
</testcase><testcase classname=\"tests.test_gate\" name=\"test_passed\" /></testsuite></testsuites>"""
    )

    assert subject.skipped_cases(report) == [
        "tests.test_gate::test_required (database is behind migrations)"
    ]


def test_skipped_cases_accepts_empty_report(tmp_path: Path) -> None:
    report = tmp_path / "junit.xml"
    report.write_text("<testsuites><testsuite><testcase name=\"test_passed\" /></testsuite></testsuites>")

    assert subject.skipped_cases(report) == []
