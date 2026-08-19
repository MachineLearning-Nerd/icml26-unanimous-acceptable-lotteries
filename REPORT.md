# Audit report

## Executive result

The cumulative campaign supplies scoped finite verification for all five
source-anchored claims in *Learning Unanimously Acceptable Lotteries via
Queries*. Each contract has a source anchor, executable mechanism, result,
negative control, proof certificate, and explicit limitation.

Overall status:

`ALL_FIVE_CLAIMS_VERIFIED_SCOPED_FINITE_AUDIT_HISTORICAL_SCORE_5_OF_10_NO_CURRENT_SCORE`

## Claim matrix

| Claim | Result | Main production path | Main limitation |
| --- | --- | --- | --- |
| C1 | `VERIFIED_SCOPED` | Exact halfspace recovery, scaling, and exhaustive cell checking | Finite quantized domains; asymptotic universal statement remains proof-anchored |
| C2 | `VERIFIED_SCOPED` | Deterministic learn/restart/Select transcripts and exact query certificates | Finite executions do not replace the theorem proof |
| C3 | `VERIFIED_SCOPED` | Weighted sampling, reweighting, verification, and seeded expectation certificate | Finite runs support the mechanism; expectation lift is proof-anchored |
| C4 | `VERIFIED_SCOPED` | Singleton hard family plus decision-tree/minimax/Kraft/Yao checks | Finite calibration parameters; proof supplies the universal lower bound |
| C5 | `VERIFIED_SCOPED` | Predicted-order traces, record-agent counts, and reversal controls | Constructed finite instances; theorem supplies asymptotic scope |

Open the [claim ledger](CLAIM_EVIDENCE.md) for exact files and controls, the
[source audit](SOURCE_AUDIT.md) for paper anchors, and the
[release report](reports/full-reproduction/release_report.md) for campaign
runtime and publication details.

## Score and publication boundary

The previous live evaluator snapshot scored the earlier candidate **5/10**.
That score is historical only. The current candidate revision is
`b9ca864e0933fb79daa53802cc38bf971397eae8`; it passed the publication gate but
is awaiting a fresh evaluator review. Therefore:

- `current_score_claim`: `false`
- `publication_allowed`: `false`
- `official_author_endorsement`: `false`

This repository is an independent audit and does not imply endorsement by the
paper’s authors.
