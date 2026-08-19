# Claim-to-evidence ledger

This is an independent, finite, source-faithful audit of *Learning Unanimously
Acceptable Lotteries via Queries*. The five labels below use the paper’s
canonical order. Some historical campaign directories used a different
internal number; the mapping is explicit so that no claim is silently
renumbered.

| Canonical claim | Paper anchor | How the result is produced | Evidence and controls | Scope and status |
| --- | --- | --- | --- | --- |
| C1 — exact learning of one acceptability halfspace | Algorithm 1; Lemmas 3.1–3.2 | Exact edge-threshold recovery and rational reconstruction are evaluated across dimension and precision; exhaustive simplex-cell checks compare recovered halfspaces with an independent oracle. | `repro/src/claim3_scaling.py`, `repro/src/claim3_exhaustive.py`, and `.openresearch/artifacts/claim-3/` provide raw rows, checkers, proof certificates, and an unquantized-threshold control. | Quantized source-model instances, including 80 scaling rows and 18 complete finite domains. Universal asymptotics remain proof-anchored. **VERIFIED_SCOPED — HIGH** |
| C2 — deterministic unanimous feasibility | Algorithm 2; Theorem 3.3 | The learn/restart/Select loop is run on feasible and infeasible instances with exact membership-query accounting and an independent finite simplex check. | `repro/src/claim1_deterministic.py`, `repro/src/verify.py`, and `.openresearch/artifacts/claim-1/` provide the transcript, finite envelope, proof certificate, and an ignored-rejecting-agent false-positive control. | Source-faithful finite executions, including large symbolic query-envelope rows. The universal theorem is supplied by the public proof. **VERIFIED_SCOPED — HIGH** |
| C3 — randomized reweighting | Algorithm 3; Theorem 3.4 | Weighted sampling without replacement, cached learned hyperplanes, global verification, and violator doubling are executed with fixed seeds; the query count is compared with an independently derived expectation envelope. | `repro/src/claim2_randomized.py` and `.openresearch/artifacts/claim-2/` contain seeded runs, raw summaries, checkers, proof certificate, and a no-weight-update control. | Finite source-model runs, including the canonical 12-seed record. The expectation lift is proof-anchored. **VERIFIED_SCOPED — HIGH** |
| C4 — universal query lower bounds | Theorems 4.1–4.2 and proof appendices | The positive epsilon-grid singleton family is constructed, its feasible set is checked, and decision-tree, minimax, Kraft, and Yao certificates are independently evaluated. | `repro/src/claim4_lower_bound.py` and `.openresearch/artifacts/claim-4/` contain the hard family, raw counts, proof certificates, and a non-singleton-family control. | Finite calibration at `n=6`, `m=3`, `epsilon=0.1`, with universal quantifiers supplied by the source proof. **VERIFIED_SCOPED — HIGH** |
| C5 — prediction-augmented ordering | Theorems 5.1–5.2 | Ordered Algorithm 2 is run while recording record-agent and verification-query counts; precision and order controls test the operational dependence on `R(sigma)`. | `repro/src/claim5_prediction.py` and `.openresearch/artifacts/claim-5/` contain raw sweeps, checker output, proof certificate, and a reversed-advice control. | Finite constructed instances with two binding and three dummy agents. The asymptotic bound is proof-anchored. **VERIFIED_SCOPED — HIGH** |

## Reading the evidence

- The root `outputs/verdict.json` is the original campaign verdict and retains
  the historical internal numbering.
- The canonical C1–C5 mapping above is also encoded in
  [`claims.json`](claims.json) and [`reproduction_verdicts.json`](reproduction_verdicts.json).
- `space_candidate/` is the evaluator-visible copy. Its claim pages link the
  exact method, raw data, checker, negative control, limitation, source audit,
  and proof certificate for each claim.
- The public TeX source establishes the universal theorem statements; finite
  runs alone do not establish every asymptotic quantifier.

## Overall result

`ALL_FIVE_CLAIMS_VERIFIED_SCOPED_FINITE_AUDIT_HISTORICAL_SCORE_5_OF_10_NO_CURRENT_SCORE`

The historical live judge scored the earlier candidate `5/10` and called the
evidence toy-scale. The current cumulative candidate expanded the evidence and
passed the publication gate, but it has not received a fresh live score. No
score increase or author endorsement is claimed.
