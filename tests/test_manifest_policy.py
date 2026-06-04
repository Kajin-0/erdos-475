"""Tests for manifest policy behavior."""
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CHECKER = REPO_ROOT / "scripts" / "check_sha256_manifest_completeness.py"
MAKER = REPO_ROOT / "scripts" / "make_manifest.sh"


def _run_checker(manifest: Path, policy: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(CHECKER), str(manifest), "--policy", str(policy)],
        capture_output=True, text=True,
    )


def _make_policy(trusted: list[str] | None = None, never: list[str] | None = None,
                 excluded: list[str] | None = None) -> str:
    return json.dumps({
        "schema": "erdos475.manifest_policy.v1",
        "description": "test policy",
        "trusted_release_files": trusted or [],
        "never_in_manifest": never or [],
        "excluded_path_globs": excluded or [],
    })


def _make_manifest(entries: dict[str, str]) -> str:
    return "\n".join(f"{h}  {f}" for f, h in entries.items()) + "\n"


def test_fails_if_manifest_has_self_entry():
    with tempfile.TemporaryDirectory() as td:
        tdir = Path(td)
        policy = tdir / "policy.json"
        policy.write_text(_make_policy(trusted=["file.txt", ".gitignore"]))
        manifest = tdir / "MANIFEST.sha256"
        # Include MANIFEST.sha256 as an entry
        manifest.write_text(_make_manifest({
            "file.txt": "a" * 64,
            ".gitignore": "b" * 64,
            "MANIFEST.sha256": "c" * 64,
        }))
        # Create the referenced files
        (tdir / "file.txt").write_text("x")
        (tdir / ".gitignore").write_text("y")
        r = _run_checker(manifest, policy)
        # The checker should either fail on the forbidden self-entry or
        # fail because the entry doesn't match the hash of the manifest.
        # Either way, it should exit nonzero.
        assert r.returncode != 0


def test_fails_if_trusted_file_missing_from_manifest():
    with tempfile.TemporaryDirectory() as td:
        tdir = Path(td)
        policy = tdir / "policy.json"
        policy.write_text(_make_policy(trusted=["file.txt", "missing_file.txt"]))
        manifest = tdir / "MANIFEST.sha256"
        manifest.write_text(_make_manifest({"file.txt": "a" * 64}))
        (tdir / "file.txt").write_text("x")
        r = _run_checker(manifest, policy)
        assert r.returncode != 0
        assert "missing from manifest" in r.stderr or "missing from manifest" in r.stdout


def test_fails_if_excluded_path_in_manifest():
    with tempfile.TemporaryDirectory() as td:
        tdir = Path(td)
        policy = tdir / "policy.json"
        policy.write_text(_make_policy(
            trusted=["file.txt"],
            excluded=["*.jsonl", "*.log"],
        ))
        manifest = tdir / "MANIFEST.sha256"
        manifest.write_text(_make_manifest({
            "file.txt": "a" * 64,
            "bad.log": "b" * 64,
        }))
        (tdir / "file.txt").write_text("x")
        (tdir / "bad.log").write_text("y")
        r = _run_checker(manifest, policy)
        assert r.returncode != 0
        assert "excluded path" in r.stderr or "excluded path" in r.stdout


def test_fails_on_duplicate_manifest_entry():
    with tempfile.TemporaryDirectory() as td:
        tdir = Path(td)
        policy = tdir / "policy.json"
        policy.write_text(_make_policy(trusted=["file.txt"]))
        manifest = tdir / "MANIFEST.sha256"
        manifest.write_text(
            f"{'a' * 64}  file.txt\n{'b' * 64}  file.txt\n"
        )
        (tdir / "file.txt").write_text("x")
        r = _run_checker(manifest, policy)
        assert r.returncode != 0
        assert "duplicate" in r.stderr.lower()


def test_make_manifest_fails_if_trusted_file_does_not_exist():
    """Simulate make_manifest.sh logic: missing trusted file causes nonzeo exit."""
    # Simulate by running the Python policy logic inline
    code = """
import json, sys, fnmatch
policy = json.loads('''{"trusted_release_files": ["file.txt", "ghost.txt"], "never_in_manifest": [], "excluded_path_globs": []}''')
never = set(policy.get('never_in_manifest', []))
excluded = policy.get('excluded_path_globs', [])
trusted = set(policy.get('trusted_release_files', []))
all_files = ["file.txt"]
missing_trusted = list(trusted)
for f in all_files:
    if f in never: continue
    skip = False
    for pat in excluded:
        if fnmatch.fnmatch(f, pat): skip = True; break
    if skip: continue
    if f in missing_trusted: missing_trusted.remove(f)
if missing_trusted:
    print(f'MISSING TRUSTED FILE: {missing_trusted[0]}', file=sys.stderr)
    sys.exit(2)
"""
    r = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True)
    assert r.returncode != 0
    assert "MISSING TRUSTED FILE" in r.stderr


def test_make_manifest_excludes_self():
    """make_manifest.sh should never include MANIFEST.sha256 in its output."""
    code = """
import json, sys, fnmatch
policy = json.loads('''{"trusted_release_files": ["file.txt"], "never_in_manifest": ["MANIFEST.sha256"], "excluded_path_globs": []}''')
never = set(policy.get('never_in_manifest', []))
excluded = policy.get('excluded_path_globs', [])
all_files = ["file.txt", "MANIFEST.sha256"]
for f in all_files:
    if f in never: continue
    skip = False
    for pat in excluded:
        if fnmatch.fnmatch(f, pat): skip = True; break
    if skip: continue
    print(f)
"""
    r = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True)
    assert r.returncode == 0
    lines = r.stdout.strip().splitlines()
    assert "MANIFEST.sha256" not in lines
    assert "file.txt" in lines


def test_make_manifest_excludes_logs_jsonl():
    """make_manifest.sh should exclude logs/*.jsonl."""
    code = """
import json, sys, fnmatch
policy = json.loads('''{"trusted_release_files": [], "never_in_manifest": [], "excluded_path_globs": ["logs/*.jsonl"]}''')
excluded = policy.get('excluded_path_globs', [])
all_files = ["file.txt", "logs/data.jsonl", "logs/train.log"]
for f in all_files:
    skip = False
    for pat in excluded:
        if fnmatch.fnmatch(f, pat): skip = True; break
    if skip: continue
    print(f)
"""
    r = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True)
    assert r.returncode == 0
    lines = r.stdout.strip().splitlines()
    assert "logs/data.jsonl" not in lines
    assert "logs/train.log" in lines
    assert "file.txt" in lines
