# Branch audit

`main` is the canonical reader-facing release. Each former `orx/*` branch has
one descriptive replacement below. The historical branch names reflect the
OpenResearch campaign sequence; the clean names describe the evidence role.

| Former branch | Clean branch | What it contains |
|---|---|---|
| `orx/c1-deterministic-exact-query-certificate` | `audit/c2-deterministic-query-certificate` | Exact Algorithm 2 deterministic query accounting; the campaign’s `c1` label is the canonical source audit’s C2. |
| `orx/c1-symbolic-transcript-certificate` | `audit/c2-symbolic-transcript` | Symbolic deterministic feasibility transcripts and universal query envelope. |
| `orx/c2-weighted-sampling-expectation-certificate` | `audit/c3-weighted-sampling-expectation` | Algorithm 3 weighted sampling, expectation, and seeded-run certificate; the campaign’s `c2` label is canonical C3. |
| `orx/c3-combined-evaluator-milestone` | `integration/cumulative-evaluator-milestone` | Combined cumulative claim evidence prepared for evaluator visibility. |
| `orx/c3-exact-scaling-certificate` | `audit/c1-exact-scaling` | Algorithm 1 halfspace-recovery scaling certificate; the campaign’s `c3` label is canonical C1. |
| `orx/c3-exhaustive-correctness-certificate` | `audit/c1-exhaustive-correctness` | Exhaustive quantized halfspace correctness and simplex-cell audit. |
| `orx/c4-minimax-lower-bound-certificate` | `audit/c4-minimax-lower-bound` | Decision-tree, minimax, Kraft, and Yao lower-bound certificates. |
| `orx/c5-exact-record-quality-certificate` | `audit/c5-record-quality` | Exact prediction-order record-quality and query-accounting certificate. |
| `orx/committed-release-manifests-and-final-gate` | `release/committed-manifests-gate` | Byte-exact release manifests and final publication gate. |
| `orx/evaluator-visible-cumulative-candidate` | `release/evaluator-visible-cumulative` | Cumulative evaluator-visible candidate with all five claim bundles. |
| `orx/exact-published-revision-audit` | `audit/published-revision` | Exact published Space revision, hash, protected-history, and traversal audit. |
| `orx/final-release-report-and-manifest-regeneration` | `release/final-report-manifest` | Final forecast report and regenerated upload manifest. |
| `orx/github-publication-surface` | `integration/github-publication` | Reader-facing publication surface mirrored to GitHub `main`. |
| `orx/hf-generated-visual-report-assets` | `experiment/visual-report-assets` | Report SVG generation from committed evidence. |
| `orx/locked-validated-baseline` | `audit/locked-baseline` | Historical validated baseline corresponding to the earlier 5/10 judged state. |
| `orx/release-gate-and-blind-traversal` | `release/release-gate-blind-traversal` | Final scientific gate, evaluator-visible package, and repeated blind traversals. |

## Claim routing

| Canonical claim | Primary clean branches |
|---|---|
| C1 — halfspace recovery | `audit/c1-exact-scaling`, `audit/c1-exhaustive-correctness` |
| C2 — deterministic feasibility | `audit/c2-deterministic-query-certificate`, `audit/c2-symbolic-transcript` |
| C3 — randomized reweighting | `audit/c3-weighted-sampling-expectation`, `integration/cumulative-evaluator-milestone` |
| C4 — lower bounds | `audit/c4-minimax-lower-bound` |
| C5 — prediction augmentation | `audit/c5-record-quality` |
| Release/publication | `release/evaluator-visible-cumulative`, `release/final-report-manifest`, `release/committed-manifests-gate`, `release/release-gate-blind-traversal` |

The branch history is development evidence, not a second verdict system. The
current claim status is the five-claim verdict and fail-closed gate on `main`;
the live score remains the evaluator’s separate 5/10 result until a new
revision is judged.
