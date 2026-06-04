# Theorem Extraction Status

Last updated: 2026-06-04

Purpose:

```text
Track effectivity extraction status for external analytic theorems used in the Erdős 475 / Graham rearrangement residue bridge.
```

Claim boundary:

```text
This dashboard does not claim a complete proof.
Only source entries marked effective in docs/source_theorems.yaml may be used by --prove residue audits.
```

---

## 1. Current summary

| Source | Role | Effectivity level | Ledger status | Proof-mode usable? | Main blocker |
|---|---|---:|---|---|---|
| Costa--Della Fiore--Fontana--Vena 2026 | very small sets `t<=20` | 4 provisional | effective | yes | verify theorem body, not only abstract |
| Bedert--Kravitz 2024 | small sets `t <= exp((log p)^1/4)` | 1 | non_effective | no | explicit large-prime threshold `P_small` not extracted |
| Pham--Sauermann 2026 | medium sets `C_alpha <= t <= p^(1-alpha)` | 1 | non_effective | no | `C_alpha` and effective threshold graph not extracted |
| BBKMM 2025 | large sets `t >= p^(1-c)` | 1 | non_effective | no | explicit `c` and threshold not extracted |
| repo finite certificates | finite complement domains | finite | finite verification | yes as finite-local/verified-domain | artifact availability / CI scope |

---

## 2. Effectivity scale

| Level | Meaning |
|---:|---|
| 0 | abstract-only or informal reference |
| 1 | exact theorem statement identified, constants not tracked |
| 2 | constant/lemma dependency graph extracted |
| 3 | recursively effective symbolic constants extracted |
| 4 | executable bound available |
| 5 | residue audit closes against verified finite domain |

---

## 3. Current verdict

```text
Current bridge verdict: C — not currently effective.
```

Reason:

```text
The central p-dependent theorems remain non_effective in the source ledger.
The --prove gate correctly rejects them.
No source-backed residue inclusion theorem is currently proved.
```

---

## 4. Immediate extraction priority

```text
Priority 1: Pham--Sauermann 2026.
```

Reason:

```text
It controls the central medium range.
Without effective C_alpha / P_alpha extraction, the three-range bridge cannot close.
```

Expected file:

```text
docs/theorem_extraction/pham_sauermann_2026.md
```

---

## 5. Proof-mode policy

The proof-mode audit is:

```text
python scripts/reduction_residue_audit.py --prove ...
```

In proof mode:

```text
1. p-dependent theorem rules require effective source ledger entries.
2. manual --range rules require source_id=<effective source>.
3. finite manual ranges require kind=finite_local and explicit finite p-bounds.
```

Exploratory runs may use placeholders without `--prove`, but their output must not be described as proof-level residue closure.

---

## 6. Next dashboard update

After each source audit, update:

```text
1. docs/source_theorems.yaml;
2. this status dashboard;
3. docs/ANALYTIC_BRIDGE_PLAN.md;
4. docs/AGENT_WORKLOG.md.
```
