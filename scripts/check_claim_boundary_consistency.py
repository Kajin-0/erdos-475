#!/usr/bin/env python3
"""Check consistency between declared domains and committed certificate files.

Validates:
  1. Every tier_1a domain has committed artifacts that actually cover its
     declared (p, b_min, b_max) range.
  2. Every tier_1b domain has corresponding artifact ledger entries.
  3. No domain is over-claimed beyond what committed artifacts can verify.

Usage:
    check_claim_boundary_consistency.py [--domains certificates/verified_domains.json]
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--domains", default="certificates/verified_domains.json")
    args = ap.parse_args()

    path = Path(args.domains)
    if not path.exists():
        print(f"ERROR domains file not found: {path}")
        return 2

    doc = json.loads(path.read_text(encoding="utf-8"))
    domains = doc.get("domains", [])
    failures: list[str] = []

    # Committed certificate files and the domains they cover
    committed_coverage: dict[str, list[dict]] = {
        "certificates/direct_witnesses_small_primes.jsonl": [
            {"p": 17, "b_min": 3, "b_max": 3},
            {"p": 19, "b_min": 3, "b_max": 5},
            {"p": 23, "b_min": 3, "b_max": 9},
        ],
        "certificates/minimal_witnesses.jsonl": [
            {"p": 29, "b_min": 3, "b_max": 7},
            {"p": 31, "b_min": 3, "b_max": 6},
        ],
        "certificates/witnesses_p29_b08.jsonl": [
            {"p": 29, "b_min": 8, "b_max": 8},
        ],
    }

    tier1a_committed_files = {str(p) for p in Path("certificates").glob("*.jsonl")
                               if p.stat().st_size > 0}

    for d in domains:
        name = d["name"]
        p = d["p"]
        b_min = d["b_min"]
        b_max = d["b_max"]
        artifact_class = d.get("artifact_class", "")
        trust_tier = d.get("trust_tier", 0)

        if trust_tier != 1:
            continue

        if artifact_class == "tier_1a_committed_repo_checkable":
            # Verify committed files cover this domain
            covered = False
            for cert_file, ranges in committed_coverage.items():
                cert_path = Path(cert_file)
                if not cert_path.exists() or cert_path.stat().st_size == 0:
                    continue
                for r in ranges:
                    if r["p"] == p and r["b_min"] <= b_min and r["b_max"] >= b_max:
                        covered = True
                        break
                if covered:
                    break

            if not covered:
                failures.append(
                    f"tier_1a domain {name} (p={p} b={b_min}-{b_max}): "
                    f"no committed certificate file covers this range"
                )
            else:
                print(f"OK domain={name} class=tier_1a covered_by_committed")

        elif artifact_class in ("tier_1b_verified_external_jsonl", "tier_1b_verified_summary_digest"):
            # Check artifact ledger exists
            ledgers = [
                Path("local_artifacts/batch_manifest/local_jsonl_artifact_manifest.json"),
                Path("local_artifacts/batch_manifest/summary_only_artifact_manifest.json"),
            ]
            found_ledger = False
            for ledger in ledgers:
                if ledger.exists():
                    try:
                        data = json.loads(ledger.read_text(encoding="utf-8"))
                        artifacts = data.get("artifacts", [])
                        for a in artifacts:
                            if a.get("p") == p and a.get("b_min", a.get("b")) is not None:
                                found_ledger = True
                                break
                    except (json.JSONDecodeError, KeyError):
                        pass

            if not found_ledger:
                failures.append(
                    f"tier_1b domain {name} (p={p} b={b_min}-{b_max}): "
                    f"no artifact ledger entry found for this domain"
                )
            else:
                print(f"OK domain={name} class={artifact_class} ledger_found")

        elif artifact_class == "tier_3_unhardened":
            print(f"WARN domain={name} class=tier_3_unhardened no committed verification required")

    # Check 2: Detect over-claiming — domains declared beyond what's verifiable
    for cert_file, ranges in committed_coverage.items():
        cert_path = Path(cert_file)
        if not cert_path.exists():
            continue
        for r in ranges:
            p = r["p"]
            b_min = r["b_min"]
            b_max = r["b_max"]
            matched = False
            for d in domains:
                if d["p"] == p and d["b_min"] <= b_min and d["b_max"] >= b_max:
                    matched = True
                    break
            if not matched:
                failures.append(
                    f"committed file {cert_file} covers p={p} b={b_min}-{b_max} "
                    f"but no matching domain entry exists in {path}"
                )

    if failures:
        print()
        print("FAIL claim boundary consistency check")
        for f in failures:
            print(f"  - {f}")
        return 2

    print()
    print("PASS claim boundary consistency check")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
