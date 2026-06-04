"""Negative regression tests for verify_minimal_witnesses.py."""

import json
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
VERIFIER = REPO_ROOT / "scripts" / "verify_minimal_witnesses.py"


def run_verifier(lines: list[str], extra: list[str] | None = None) -> subprocess.CompletedProcess:
    data = "\n".join(lines) + "\n"
    with tempfile.NamedTemporaryFile(mode="w", suffix=".jsonl", delete=False) as f:
        f.write(data)
        fname = f.name
    try:
        cmd = [sys.executable, str(VERIFIER), fname]
        if extra:
            cmd.extend(extra)
        return subprocess.run(cmd, capture_output=True, text=True)
    finally:
        Path(fname).unlink()


def test_rejects_non_prime_p():
    r = run_verifier(['{"p": 1, "B": [2], "final_order": [3]}'])
    assert r.returncode != 0
    assert "must be >= 2" in r.stderr or "not prime" in r.stderr


def test_rejects_duplicates_in_B():
    r = run_verifier(['{"p": 7, "B": [1, 1], "final_order": [2, 3, 4, 5, 6]}'])
    assert r.returncode != 0
    assert "duplicate" in r.stderr.lower() or "duplicates" in r.stderr


def test_rejects_B_not_subset():
    r = run_verifier(['{"p": 7, "B": [1, 0], "final_order": [2, 3, 4, 5, 6]}'])
    assert r.returncode != 0
    assert "subset" in r.stderr.lower()


def test_rejects_non_canonical_with_flag():
    r = run_verifier(
        ['{"p": 7, "B": [5, 6], "final_order": [1, 3, 2, 4]}'],
        extra=["--require-canonical"],
    )
    assert r.returncode != 0
    assert "canonical" in r.stderr.lower()


def test_rejects_wrong_final_order():
    r = run_verifier(['{"p": 7, "B": [1], "final_order": [2, 3, 4, 5]}'])
    assert r.returncode != 0
    assert "missing" in r.stderr.lower() or "not a permutation" in r.stderr.lower()


def test_rejects_repeated_partial_sum():
    r = run_verifier(['{"p": 7, "B": [2], "final_order": [1, 4, 6, 3, 5]}'])
    assert r.returncode != 0
    assert "repeated" in r.stderr.lower() or "partial sum" in r.stderr.lower()


def test_rejects_duplicate_witness():
    line = '{"p": 7, "B": [1], "final_order": [2, 3, 5, 4, 6]}'
    r = run_verifier([line, line])
    assert r.returncode != 0
    assert "duplicate" in r.stderr.lower()


def test_accepts_valid_witness():
    r = run_verifier(['{"p": 7, "B": [1], "final_order": [2, 3, 5, 4, 6]}'])
    assert r.returncode == 0
    assert "PASS" in r.stdout


def test_rejects_p_as_bool():
    r = run_verifier(['{"p": true, "B": [1], "final_order": [2, 3]}'])
    assert r.returncode != 0
    assert "bool" in r.stderr.lower() or "integer" in r.stderr.lower()


def test_rejects_b_contains_bool():
    r = run_verifier(['{"p": 7, "B": [1, true], "final_order": [2, 3, 4, 5, 6]}'])
    assert r.returncode != 0
    assert "bool" in r.stderr.lower() or "integer" in r.stderr.lower()


def test_rejects_final_order_contains_bool():
    r = run_verifier(['{"p": 7, "B": [1], "final_order": [2, true, 3, 4, 5, 6]}'])
    assert r.returncode != 0
    assert "bool" in r.stderr.lower() or "integer" in r.stderr.lower()


def test_rejects_p_as_string():
    r = run_verifier(['{"p": "17", "B": [1], "final_order": [2, 3]}'])
    assert r.returncode != 0
    assert "integer" in r.stderr.lower()


def test_rejects_B_contains_string():
    r = run_verifier(['{"p": 7, "B": ["1", 2], "final_order": [3, 4, 5, 6]}'])
    assert r.returncode != 0
    assert "integer" in r.stderr.lower()


def test_rejects_final_order_contains_string():
    r = run_verifier(['{"p": 7, "B": [1], "final_order": ["3", 4, 5, 6, 2]}'])
    assert r.returncode != 0
    assert "integer" in r.stderr.lower()


def test_rejects_root_array():
    r = run_verifier(['["not", "an", "object"]'])
    assert r.returncode != 0
    assert "object" in r.stderr.lower()


def test_rejects_non_int_float():
    r = run_verifier(['{"p": 7.0, "B": [1], "final_order": [2, 3, 4, 5, 6]}'])
    assert r.returncode != 0
    assert "integer" in r.stderr.lower()
