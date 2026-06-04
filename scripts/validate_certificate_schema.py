#!/usr/bin/env python3
"""Validate the JSON schema of finite certificate files.

Checks:
  - JSONL lines parse correctly
  - Required fields (p, B, final_order) are present with correct types
  - verified_domains.json conforms to expected schema

Usage:
    validate_certificate_schema.py <file.jsonl> [file2.jsonl ...]
    validate_certificate_schema.py --domains certificates/verified_domains.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def check_jsonl(path: Path) -> int:
    errors = 0
    with path.open("r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
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
            if p is not None and not isinstance(p, int):
                print(f"ERROR {line_id}: p must be an integer, got {type(p).__name__}")
                errors += 1

            for field in ("B", "final_order"):
                val = obj.get(field)
                if val is not None and (not isinstance(val, list) or not all(isinstance(x, int) for x in val)):
                    print(f"ERROR {line_id}: {field} must be a list of integers, got {type(val).__name__}")
                    errors += 1

    if errors == 0:
        print(f"PASS schema={path}")

    return errors


def check_domains_json(path: Path) -> int:
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
                for field in ("name", "p", "b_min", "b_max", "method", "trust_tier", "artifact_class"):
                    if field not in d:
                        print(f"ERROR {path}: domains[{i}] missing field {field!r}")
                        errors += 1

    if errors == 0:
        print(f"PASS schema={path}")

    return errors


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("files", nargs="+", help="Certificate files (.jsonl) or --domains flag")
    ap.add_argument("--domains", action="store_true", help="Validate verified_domains.json instead of JSONL")
    args = ap.parse_args()

    total = 0
    for path_str in args.files:
        path = Path(path_str)
        if not path.exists():
            print(f"ERROR file not found: {path}")
            total += 1
            continue
        if args.domains:
            total += check_domains_json(path)
        else:
            total += check_jsonl(path)

    if total > 0:
        print(f"FAIL schema validation: {total} files with errors")
    else:
        print("PASS all schema validation")

    return 1 if total > 0 else 0


if __name__ == "__main__":
    raise SystemExit(main())
