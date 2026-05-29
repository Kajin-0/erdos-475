#!/usr/bin/env python3
"""Check required repository artifacts before finite-certificate verification.

This is intentionally path-based rather than hash-based.  It prevents accidental
claim drift caused by deleting required docs/scripts/certificate sources, while
still allowing generated logs to remain untracked working artifacts.

Manifest format:

    required <path>
    certificate_source <certificate_path> <trace_path_1> <trace_path_2> ...

A certificate_source line passes when either the certificate exists, or every
listed trace source exists so the verification script can regenerate the
certificate.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class RequiredPath:
    path: Path
    lineno: int


@dataclass(frozen=True)
class CertificateSource:
    certificate: Path
    traces: tuple[Path, ...]
    lineno: int


def parse_manifest(path: Path) -> tuple[list[RequiredPath], list[CertificateSource]]:
    required: list[RequiredPath] = []
    certs: list[CertificateSource] = []
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        kind = parts[0]
        if kind == "required":
            if len(parts) != 2:
                raise SystemExit(f"{path}:{lineno}: required line must be: required <path>")
            required.append(RequiredPath(Path(parts[1]), lineno))
        elif kind == "certificate_source":
            if len(parts) < 3:
                raise SystemExit(
                    f"{path}:{lineno}: certificate_source line must be: "
                    "certificate_source <certificate> <trace1> [trace2 ...]"
                )
            certs.append(CertificateSource(Path(parts[1]), tuple(Path(p) for p in parts[2:]), lineno))
        else:
            raise SystemExit(f"{path}:{lineno}: unknown directive {kind!r}")
    return required, certs


def missing(paths: Iterable[Path]) -> list[str]:
    return [str(path) for path in paths if not path.exists()]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("manifest", nargs="?", default="MANIFEST.required")
    args = ap.parse_args()

    manifest = Path(args.manifest)
    if not manifest.exists():
        print(f"[artifact-check] missing manifest: {manifest}")
        return 2

    required, certs = parse_manifest(manifest)
    failures: list[str] = []

    for item in required:
        if not item.path.exists():
            failures.append(f"{manifest}:{item.lineno}: missing required path: {item.path}")

    for item in certs:
        if item.certificate.exists():
            continue
        absent = missing(item.traces)
        if absent:
            failures.append(
                f"{manifest}:{item.lineno}: missing certificate {item.certificate} "
                f"and missing source traces: {', '.join(absent)}"
            )

    if failures:
        print("[artifact-check] FAIL")
        for failure in failures:
            print(f"  - {failure}")
        return 2

    print(f"[artifact-check] PASS {len(required)} required paths, {len(certs)} certificate source rules")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
