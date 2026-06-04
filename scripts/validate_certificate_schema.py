#!/usr/bin/env python3
"""Validate the JSON schema of finite certificate files.

Usage:
    validate_certificate_schema.py [--strict] <file.jsonl> [file2.jsonl ...]
    validate_certificate_schema.py --domains certificates/verified_domains.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Fields that are never trusted in strict mode
UNTRUSTED_FIELDS = frozenset({
    "partial_sums", "trace_status", "repair_steps",
    "claimed_valid", "valid", "canonical_id", "coverage_count",
})

KNOWN_DOMAIN_FIELDS = frozenset({
    "name", "p", "b_min", "b_max", "method", "trust_tier", "artifact_class",
})

KNOWN_ARTIFACT_CLASSES = frozenset({
    "tier_1a_committed_repo_checkable",
    "tier_1b_verified_external_jsonl",
    "tier_1b_verified_summary_digest",
    "tier_3_unhardened",
})


def is_strict_int(val) -> bool:
    return isinstance(val, int) and not isinstance(val, bool)


def is_strict_int_list(val) -> bool:
    if not isinstance(val, list):
        return False
    return all(is_strict_int(x) for x in val)


def check_jsonl(path: Path, strict: bool) -> int:
    errors = 0
    rows = 0
    if path.stat().st_size == 0:
        print(f"ERROR {path}: file is empty (use --allow-empty to skip)")
        return 1

    with path.open("r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            rows += 1
            line_id = f"{path}:{lineno}"
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"ERROR {line_id}: invalid JSON: {e}")
                errors += 1
                continue

            if not isinstance(obj, dict):
                print(f"ERROR {line_id}: root value is not a JSON object")
                errors += 1
                continue

            for field in ("p", "B", "final_order"):
                if field not in obj:
                    print(f"ERROR {line_id}: missing required field {field!r}")
                    errors += 1

            p = obj.get("p")
            if p is not None:
                if not is_strict_int(p):
                    print(f"ERROR {line_id}: p must be an integer (not bool), got {type(p).__name__}")
                    errors += 1
                elif p < 2:
                    print(f"ERROR {line_id}: p must be >= 2, got {p}")
                    errors += 1

            for field in ("B", "final_order"):
                val = obj.get(field)
                if val is not None:
                    if not is_strict_int_list(val):
                        print(f"ERROR {line_id}: {field} must be a list of integers (not bools), got {type(val).__name__}")
                        errors += 1

            if strict:
                for key in obj:
                    if key in UNTRUSTED_FIELDS:
                        print(f"ERROR {line_id}: strict mode rejects untrusted field {key!r}")
                        errors += 1

    print(f"schema={path} rows={rows} errors={errors}")
    return errors


def check_domains_json(path: Path, strict: bool, allow_unknown_class: bool) -> int:
    errors = 0
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"ERROR {path}: invalid JSON: {e}")
        return 1

    if not isinstance(doc, dict):
        print(f"ERROR {path}: root must be a JSON object")
        return 1

    for key in ("schema", "claim_boundary", "domains"):
        if key not in doc:
            print(f"ERROR {path}: missing top-level key {key!r}")
            errors += 1

    domains = doc.get("domains")
    if domains is not None:
        if not isinstance(domains, list):
            print(f"ERROR {path}: domains must be an array")
            errors += 1
        else:
            for i, d in enumerate(domains):
                if not isinstance(d, dict):
                    print(f"ERROR {path}: domains[{i}] is not an object")
                    errors += 1
                    continue
                for field in KNOWN_DOMAIN_FIELDS:
                    if field not in d:
                        print(f"ERROR {path}: domains[{i}] missing field {field!r}")
                        errors += 1
                ac = d.get("artifact_class")
                if ac is not None and ac not in KNOWN_ARTIFACT_CLASSES and not allow_unknown_class:
                    print(f"ERROR {path}: domains[{i}] unknown artifact_class {ac!r}")
                    errors += 1

    print(f"domains_schema={path} domains={len(domains) if isinstance(domains, list) else '?'} errors={errors}")
    return errors


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("files", nargs="+", help="Certificate files (.jsonl) or --domains flag")
    ap.add_argument("--domains", action="store_true", help="Validate verified_domains.json instead of JSONL")
    ap.add_argument("--strict", action="store_true", help="Enable strict checks")
    ap.add_argument("--allow-empty", action="store_true", help="Allow empty files")
    ap.add_argument("--allow-unknown-class", action="store_true", help="Allow unknown artifact classes")
    args = ap.parse_args()

    total = 0
    for path_str in args.files:
        path = Path(path_str)
        if not path.exists():
            print(f"ERROR file not found: {path}")
            total += 1
            continue
        if args.domains or path.suffix == ".json":
            total += check_domains_json(path, args.strict, args.allow_unknown_class)
        else:
            if path.stat().st_size == 0 and args.allow_empty:
                print(f"SKIP {path}: empty file allowed by --allow-empty")
                continue
            total += check_jsonl(path, args.strict)

    if total > 0:
        print(f"FAIL schema validation: {total} files with errors")
    else:
        print("PASS all schema validation")

    return 1 if total > 0 else 0


if __name__ == "__main__":
    raise SystemExit(main())
