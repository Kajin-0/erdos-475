"""Negative regression tests for audit_canonical_counts.py."""

import json
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
AUDITOR = REPO_ROOT / "scripts" / "audit_canonical_counts.py"


def run_auditor(lines: list[str], domains: list[str], extra: list[str] | None = None) -> subprocess.CompletedProcess:
    data = "\n".join(lines) + "\n"
    with tempfile.NamedTemporaryFile(mode="w", suffix=".jsonl", delete=False) as f:
        f.write(data)
        fname = f.name
    try:
        cmd = [sys.executable, str(AUDITOR), fname]
        for d in domains:
            cmd.extend(["--domain", d])
        if extra:
            cmd.extend(extra)
        return subprocess.run(cmd, capture_output=True, text=True)
    finally:
        Path(fname).unlink()


def test_rejects_incomplete_coverage():
    """Only 2 of 35 canonical B sets for p=17 |B|=3, must fail."""
    lines = []
    for B in [[1, 2], [1, 3]]:
        B_sorted = sorted(B)
        A = [x for x in range(1, 17) if x not in B_sorted]
        lines.append(json.dumps({"p": 17, "B": B_sorted, "final_order": A}))
    r = run_auditor(lines, ["17:3"])
    assert r.returncode != 0
    assert "missing" in r.stdout


def test_rejects_missing_domain():
    """Requesting a domain not present in input must fail."""
    lines = [
        json.dumps({"p": 5, "B": [1], "final_order": [2, 3, 4]}),
    ]
    r = run_auditor(lines, ["5:1", "7:1"])
    assert r.returncode != 0
    assert "missing" in r.stdout or "FAIL" in r.stdout


def test_passes_full_coverage():
    """All canonical B sets for p=5 |B|=2 should pass (2 canonical classes)."""
    lines = [
        json.dumps({"p": 5, "B": [1, 2], "final_order": [3, 4]}),
        json.dumps({"p": 5, "B": [1, 4], "final_order": [2, 3]}),
    ]
    r = run_auditor(lines, ["5:2"])
    assert r.returncode == 0
    assert "PASS" in r.stdout


def test_rejects_non_prime_p():
    lines = [json.dumps({"p": 1, "B": [2], "final_order": [3]})]
    r = run_auditor(lines, ["1:1"])
    assert r.returncode != 0
    assert "malformed" in r.stdout


def test_rejects_p_as_bool():
    lines = [json.dumps({"p": True, "B": [1], "final_order": [2, 3]})]
    r = run_auditor(lines, ["5:1"])
    assert r.returncode != 0
    assert "malformed" in r.stdout


def test_rejects_B_with_bool():
    lines = [json.dumps({"p": 5, "B": [1, True], "final_order": [2, 3]})]
    r = run_auditor(lines, ["5:2"])
    assert r.returncode != 0
    assert "malformed" in r.stdout


def test_rejects_B_containing_zero():
    lines = [json.dumps({"p": 5, "B": [1, 0], "final_order": [2, 3]})]
    r = run_auditor(lines, ["5:2"])
    assert r.returncode != 0
    assert "malformed" in r.stdout


def test_rejects_B_containing_p():
    lines = [json.dumps({"p": 5, "B": [1, 5], "final_order": [2, 3]})]
    r = run_auditor(lines, ["5:2"])
    assert r.returncode != 0
    assert "malformed" in r.stdout


def test_rejects_noncanonical_with_flag():
    lines = [json.dumps({"p": 7, "B": [5, 6], "final_order": [1, 2, 3, 4]})]
    r = run_auditor(lines, ["7:2"], extra=["--require-canonical"])
    assert r.returncode != 0
    assert "noncanonical" in r.stdout


def test_rejects_duplicate_canonical():
    line = json.dumps({"p": 5, "B": [1, 2], "final_order": [3, 4]})
    r = run_auditor([line, line], ["5:2"])
    assert r.returncode != 0
    assert "duplicate" in r.stdout


def test_rejects_extra_domain_with_flag():
    lines = [json.dumps({"p": 5, "B": [1], "final_order": [2, 3, 4]})]
    r = run_auditor(lines, ["5:1"], extra=["--fail-extra-domains"])
    assert r.returncode == 0  # Only one domain, no extras


def test_rejects_malformed_json():
    r = run_auditor(["{bad}"], ["5:1"])
    assert r.returncode != 0
    assert "malformed" in r.stdout
