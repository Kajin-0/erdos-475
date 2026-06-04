#!/usr/bin/env python3
"""Check MANIFEST.required completeness and cross-reference against verified_domains.json.

This is the MANIFEST.required checker. The MANIFEST.sha256 checker is a separate
script (check_sha256_manifest_completeness.py).

Validates:
  1. All paths listed in MANIFEST.required exist.
  2. All certificate_source rules are satisfied (cert exists or all traces exist).
  3. Every tier_1a domain in verified_domains.json has a corresponding entry in
     MANIFEST.required (either as a required certificate path or as a certificate_source).
  4. No duplicate entries in the manifest.

Usage:
    check_manifest_completeness.py [MANIFEST.required] [--domains verified_domains.json]
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Req:
    path: Path
    lineno: int


@dataclass(frozen=True)
class CertSource:
    certificate: Path
    traces: tuple[Path, ...]
    lineno: int


def parse_manifest(path: Path) -> tuple[list[Req], list[CertSource]]:
    required: list[Req] = []
    certs: list[CertSource] = []
    seen_paths: set[str] = set()
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        kind = parts[0]
        if kind == "required":
            p = Path(parts[1])
            key = str(p)
            if key in seen_paths:
                raise SystemExit(f"{path}:{lineno}: duplicate required path: {p}")
            seen_paths.add(key)
            required.append(Req(p, lineno))
        elif kind == "certificate_source":
            cert = Path(parts[1])
            traces = tuple(Path(p) for p in parts[2:])
            certs.append(CertSource(cert, traces, lineno))
        else:
            raise SystemExit(f"{path}:{lineno}: unknown directive {kind!r}")
    return required, certs


def missing(paths: Iterable[Path]) -> list[str]:
    return [str(p) for p in paths if not p.exists()]


def load_domains(path: Path) -> list[dict]:
    doc = json.loads(path.read_text(encoding="utf-8"))
    return doc.get("domains", [])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("manifest", nargs="?", default="MANIFEST.required")
    ap.add_argument("--domains", default="certificates/verified_domains.json")
    args = ap.parse_args()

    manifest = Path(args.manifest)
    if not manifest.exists():
        print(f"ERROR missing manifest: {manifest}")
        return 2

    required, certs = parse_manifest(manifest)
    failures: list[str] = []

    for item in required:
        if not item.path.exists():
            failures.append(f"missing required path: {item.path} (line {item.lineno})")

    for item in certs:
        if item.certificate.exists():
            continue
        absent = missing(item.traces)
        if absent:
            failures.append(
                f"missing certificate {item.certificate} and traces: {', '.join(absent)} "
                f"(line {item.lineno})"
            )

    # Cross-reference tier_1a domains against manifest
    domains_path = Path(args.domains)
    if domains_path.exists():
        domains = load_domains(domains_path)
        required_strs = {str(item.path) for item in required}
        cert_strs = {str(item.certificate) for item in certs}

        for d in domains:
            if d.get("artifact_class") == "tier_1a_committed_repo_checkable":
                name = d["name"]
                p = d["p"]
                b_min = d["b_min"]
                b_max = d["b_max"]

                if p == 17 and b_min == 3 and b_max == 3:
                    expected_paths = {"certificates/direct_witnesses_small_primes.jsonl"}
                elif p == 19 and b_min == 3 and b_max == 5:
                    expected_paths = {"certificates/direct_witnesses_small_primes.jsonl"}
                elif p == 23 and b_min == 3 and b_max == 9:
                    expected_paths = {"certificates/direct_witnesses_small_primes.jsonl"}
                elif p == 29 and b_min == 3 and b_max == 7:
                    expected_paths = {"certificates/minimal_witnesses.jsonl"}
                elif p == 29 and b_min == 8 and b_max == 8:
                    expected_paths = {"certificates/witnesses_p29_b08.jsonl"}
                elif p == 31 and b_min == 3 and b_max == 6:
                    expected_paths = {"certificates/minimal_witnesses.jsonl"}
                else:
                    failures.append(
                        f"tier_1a domain {name} (p={p} b={b_min}-{b_max}) "
                        f"has no known expected certificate path mapping"
                    )
                    continue

                for ep in expected_paths:
                    if ep not in required_strs and ep not in cert_strs:
                        failures.append(
                            f"tier_1a domain {name} requires certificate {ep} "
                            f"but it is not listed in {manifest}"
                        )

    if failures:
        print("FAIL manifest completeness check")
        for f in failures:
            print(f"  - {f}")
        return 2

    print(f"PASS manifest completeness: {len(required)} required paths, {len(certs)} certificate sources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
