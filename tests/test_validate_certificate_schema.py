"""Negative regression tests for validate_certificate_schema.py."""

import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = REPO_ROOT / "scripts" / "validate_certificate_schema.py"


def run_validator(lines: list[str]) -> subprocess.CompletedProcess:
    data = "\n".join(lines) + "\n"
    with tempfile.NamedTemporaryFile(mode="w", suffix=".jsonl", delete=False) as f:
        f.write(data)
        fname = f.name
    try:
        return subprocess.run(
            [sys.executable, str(VALIDATOR), fname],
            capture_output=True, text=True,
        )
    finally:
        Path(fname).unlink()


def test_rejects_invalid_json():
    r = run_validator(["{bad}"])
    assert r.returncode != 0
    assert "invalid JSON" in r.stdout or "ERROR" in r.stdout


def test_rejects_non_object_root():
    r = run_validator(['["not", "an", "object"]'])
    assert r.returncode != 0
    assert "not a JSON object" in r.stdout


def test_rejects_missing_p():
    r = run_validator(['{"B": [1], "final_order": [2, 3]}'])
    assert r.returncode != 0
    assert "missing" in r.stdout and "p" in r.stdout


def test_rejects_missing_B():
    r = run_validator(['{"p": 7, "final_order": [1, 2, 3, 4, 5, 6]}'])
    assert r.returncode != 0
    assert "missing" in r.stdout and "B" in r.stdout


def test_rejects_missing_final_order():
    r = run_validator(['{"p": 7, "B": [1]}'])
    assert r.returncode != 0
    assert "missing" in r.stdout and "final_order" in r.stdout


def test_rejects_non_int_p():
    r = run_validator(['{"p": "seven", "B": [1], "final_order": [2, 3]}'])
    assert r.returncode != 0
    assert "integer" in r.stdout


def test_rejects_non_list_B():
    r = run_validator(['{"p": 7, "B": "not_a_list", "final_order": [1, 2, 3, 4, 5, 6]}'])
    assert r.returncode != 0
    assert "list" in r.stdout


def test_accepts_valid():
    r = run_validator([
        '{"p": 17, "B": [1], "final_order": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]}'
    ])
    assert r.returncode == 0
    assert "PASS" in r.stdout
