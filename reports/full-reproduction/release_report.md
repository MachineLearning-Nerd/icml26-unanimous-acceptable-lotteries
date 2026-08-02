# Final release report

Previous live judged score: `5/10`

Conservative projected score range after the proposed change: **5–10/10**. This is a forecast, not a judge result.

Best-supported possible new score: **10/10 (forecast only)**. Only the live evaluator can change the score.

## Claim forecast

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
| --- | --- | --- | --- | --- | --- |
| 1 | 1/2 | 2/2 | HIGH | VERIFIED | Exact Algorithm 2 transcripts at `n=65,536`, `m=256`, and `1/epsilon=65,536`, with independent symbolic counting and failing controls. Remaining risk is evaluator acceptance of the certificate presentation. |
| 2 | 1/2 | 2/2 | HIGH | VERIFIED | Forty full Algorithm 3 executions plus an independently reconstructed expectation certificate. Remaining risk is interpretation of the proof-level expectation lift. |
| 3 | 1/2 | 2/2 | HIGH | VERIFIED | Eighty scaling rows, 12,272 exhaustive halfspaces, 9,882,192 exact cell checks, and a symbolic derivation. Remaining risk is evaluator interpretation, not an unresolved scientific check. |
| 4 | 1/2 | 2/2 | HIGH | VERIFIED | Decision-tree, Kraft, Yao, exhaustive hard-family, and exact minimax certificates quantify over all correct algorithms. Remaining risk is the paper's always-correct randomized-model interpretation. |
| 5 | 1/2 | 2/2 | HIGH | VERIFIED | Exact record-quality sweep through `R=256` and independent `n`, `m`, and precision sweeps. Remaining risk is that the evidence uses constructed theorem-calibration families rather than natural preferences. |

Current total score: **5/10**. Conservative projected total: **5–10/10**. Best-supported possible total: **10/10, forecast only**. All five claims changed from TOY evidence to current VERIFIED evidence. No claim is BLOCKED.

## Release basis

- Baseline branch and starting SHA: `main@15f5248dfce3fcb431e8b02ad9ffa266dc1a0357`.
- Previous HF Head and Judge Head: `88488bc18db7974567008ee55dbea85871de82e4`.
- Winning cumulative scientific revision: `orx/release-gate-and-blind-traversal@6e22b3b68ff9829c3cc3fa26f1593caeed36b4b9`.
- Fixed command on every node: `uv sync --frozen && uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py`.
- Environment: Python 3.12, `uv`, one repository `.venv`, frozen `uv.lock`; optional `marimo==0.23.1` is installed into that same environment after the scientific verifier.
- Compute contract: Hugging Face `cpu-upgrade`, officially 8 vCPU/32 GB, no GPU. The job process reported 64 logical CPUs and affinity 64; both figures are retained to distinguish provider flavor from container visibility.
- Protected history: the exact judged revision was downloaded with an explicit User-Agent and verified against its SHA-256 manifest. The old file set is a subset of the candidate, and untouched historical pages retain their hashes.
- Evaluator visibility: two blind traversals began only from `README.md` and `logbook.json`; every matrix cell was complete and no inaccessible conclusion remained.

The experiment tree is a stacked sequence: validated baseline; Claim 3 scaling and exhaustive certificate; Claim 1 transcript certificate; Claim 5 record-quality certificate; Claim 4 minimax certificate; Claim 2 expectation certificate; cumulative candidate; remotely generated figures; and the release/blind-traversal gate. Setup failures were repaired in place before each affected node froze.

## Runtime and estimated cost through evidence freeze

Every listed run used the exact fixed command above on Hugging Face `cpu-upgrade`. This table includes successful, failed, and cancelled attempts through run `6f3314ca-0c47-4f34-84bb-5d09cc637ced`.

| Experiment | Status | End-to-end runtime |
| --- | --- | ---: |
| Locked validated baseline | done | 21 s |
| C3 exact scaling certificate, setup attempt | failed | 111 s |
| C3 exhaustive correctness certificate | done | 143 s |
| C3 exact scaling certificate | done | 111 s |
| C3 combined evaluator milestone | done | 238 s |
| C1 deterministic exact query certificate, setup attempt | failed | 248 s |
| C1 deterministic exact query certificate, cancelled attempt | cancelled | 1,367 s |
| C1 symbolic transcript certificate, setup attempt | failed | 334 s |
| C1 symbolic transcript certificate | done | 307 s |
| C5 exact record-quality certificate | done | 403 s |
| C4 minimax lower-bound certificate | done | 386 s |
| C2 weighted-sampling expectation certificate | done | 562 s |
| Evaluator-visible cumulative candidate | done | 632 s |
| HF-generated visual report assets | done | 598 s |
| Release gate and blind traversal, notebook setup attempt | failed | 811 s |
| Release gate and blind traversal | done | 818 s |

Total end-to-end duration is **7,090 s (1.969 h)**. Hugging Face documents `cpu-upgrade` at `$0.0005/min` (`$0.03/h`) with minute-based billing. Conservatively rounding every job upward gives **125 billable minutes and an estimated compute cost of $0.0625**; the Hugging Face billing page remains authoritative because `orx` duration can include non-billed lifecycle time. The final manifest-confirmation and post-publication audit jobs occur after this immutable report cut and are reported separately.

## Evidence and publication action

The evaluator-visible evidence begins at `pages/current/index.md`. Claim contracts, source audits, methods, raw CSV/JSON, proof certificates, checker outputs, negative-control outputs, deviations, exact commands, seeds, SHAs, and CPU/runtime details are under `evidence/claim-1/` through `evidence/claim-5/`. The illustrated report is `reports/full-reproduction/report.md`; the tutorial is `notebooks/reproduction.py`.

The exact upload allowlist, SHA-256 manifest, and blind-review transcript are generated by the remote release gate and committed under `.openresearch/release/`. The publication action, after their final matching gate, is a text-only upload to the existing `DineshAI/daiccpXZfU` Space, followed by an exact-revision download, hash verification, evaluator-visible traversal, and a fast-forward publication of the reader-facing text artifacts to GitHub `main`. No second Space will be created, and no score increase will be claimed before live judging.
