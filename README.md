# Learning Unanimously Acceptable Lotteries via Queries

Independent reproduction audit for [arXiv:2604.17505](https://arxiv.org/abs/2604.17505),
“Learning Unanimously Acceptable Lotteries via Queries,” by Davin Choo, Paul
W. Goldberg, and Nicholas Teh.

## Audit record

- Overall status: `ALL_FIVE_CLAIMS_VERIFIED_SCOPED_FINITE_AUDIT_HISTORICAL_SCORE_5_OF_10_NO_CURRENT_SCORE`
- Repository: [MachineLearning-Nerd/icml26-unanimous-acceptable-lotteries](https://github.com/MachineLearning-Nerd/icml26-unanimous-acceptable-lotteries)
- Scope: finite, source-faithful membership-query executions plus the public TeX proof anchors
- Current score claim: none; the candidate is awaiting a fresh evaluator review
- Publication gate: passed; author endorsement: not claimed
- Standard audit surfaces: [CLAIM_EVIDENCE.md](CLAIM_EVIDENCE.md), [REPORT.md](REPORT.md), [STATUS.md](STATUS.md), [SOURCE_AUDIT.md](SOURCE_AUDIT.md), and [verify_final.py](verify_final.py)

## Result at a glance

All five source-anchored claim contracts are **VERIFIED (SCOPED)** with high
scientific confidence in the cumulative campaign. The candidate is finite,
source-faithful evidence—not a live-score claim: the previous live judged
score is **5/10**, the published candidate is awaiting a fresh evaluator
review, and no score increase is claimed.

The current candidate revision is
[`b9ca864e0933fb79daa53802cc38bf971397eae8`](https://huggingface.co/spaces/DineshAI/daiccpXZfU/commit/b9ca864e0933fb79daa53802cc38bf971397eae8).
Its release audit recorded 85 uploaded hashes, 20 protected historical paths,
and two identical canonical traversals. All scientific computation used
Hugging Face `cpu-upgrade` with no GPU; the evidence uses constructed
theorem-calibration families rather than natural preference data.

Read the [illustrated report](reports/full-reproduction/report.md), the
[release report](reports/full-reproduction/release_report.md), the
[source audit](docs/SOURCE_AUDIT.md), and the
[machine-readable verdict](outputs/verdict.json). The normalized summary is in
[reproduction_verdicts.json](reproduction_verdicts.json), and the required
files and controls are listed in [EVIDENCE_MANIFEST.json](EVIDENCE_MANIFEST.json).

## Problem and paper scope

There are `n` agents and `m` alternatives. Each agent accepts a lottery when
its expected utility clears an unknown threshold. The algorithms receive only
binary membership-query answers and must either return a lottery accepted by
everyone or certify infeasibility.

The paper studies three algorithmic layers: exact learning of one
acceptability halfspace, adaptive deterministic and randomized multi-agent
feasibility procedures, and learning-augmented order or lottery predictions.
It also gives worst-case lower bounds on query complexity.

## Claim-to-evidence ledger

The canonical C1–C5 labels below follow [`docs/SOURCE_AUDIT.md`](docs/SOURCE_AUDIT.md)
and [`outputs/verdict.json`](outputs/verdict.json). Some historical branch
names use the campaign’s earlier numbering; the branch map calls that out.

| Claim | Paper anchor | How the result is produced | Control and scope | Status |
|---|---|---|---|---|
| C1 — exact halfspace recovery | Algorithm 1; Lemmas 3.1–3.2 | [`verify.py`](repro/src/verify.py) runs exact edge-threshold recovery; [`claim3_scaling.py`](repro/src/claim3_scaling.py) and [`claim3_exhaustive.py`](repro/src/claim3_exhaustive.py) provide scaling and exhaustive correctness routes. | An unquantized `1/11` threshold breaks the bounded-denominator premise; the canonical verdict checks 2,480 grid cells for source-model quantized halfspaces. | VERIFIED — HIGH |
| C2 — deterministic feasibility | Algorithm 2; Theorem 3.3 | [`verify.py`](repro/src/verify.py) runs the learn/restart/Select loop on feasible and infeasible instances; [`claim1_deterministic.py`](repro/src/claim1_deterministic.py) provides exact query certificates. | Ignoring a rejecting agent creates a false positive; the finite loop is source-faithful while the asymptotic bound remains proof-anchored. | VERIFIED — HIGH |
| C3 — randomized reweighting | Algorithm 3; Theorem 3.4 | [`claim2_randomized.py`](repro/src/claim2_randomized.py) implements weighted sampling without replacement, cached hyperplanes, global verification, and violator doubling; the verifier records 12 seeded runs. | Disabling weight updates leaves first-round violators unresolved; finite executions support the stated mechanism and expectation certificate. | VERIFIED — HIGH |
| C4 — universal lower bounds | Theorems 4.1–4.2 | [`claim4_lower_bound.py`](repro/src/claim4_lower_bound.py) constructs the positive epsilon-grid singleton family and independently counts decision-tree leaves, with minimax/Kraft/Yao certificates in the release bundle. | A non-singleton family invalidates the leaf-count argument; the canonical finite witness uses `n=6`, `m=3`, `epsilon=0.1`. | VERIFIED — HIGH |
| C5 — prediction-augmented ordering | Theorems 5.1–5.2 | [`claim5_prediction.py`](repro/src/claim5_prediction.py) runs ordered Algorithm 2 and records record-agent and verification-query counts; the release bundle sweeps `R` and independent dimensions. | Reversed advice changes the query trace; the canonical finite instance uses two binding and three dummy agents. | VERIFIED — HIGH |

The evaluator-visible candidate mirrors claim contracts, methods, raw CSV/JSON,
proof certificates, independent checkers, negative controls, limitations, and
source audits under [`space_candidate/`](space_candidate/). The public TeX
proofs, not finite enumeration alone, supply the universal asymptotic
quantifiers.

## Reproduce the published checks

The locked Python 3.12 environment is:

```bash
uv sync --frozen
uv run --frozen python repro/src/verify.py
uv run --frozen python repro/src/publication_gate.py
```

The optional evidence-first notebook uses the same environment:

```bash
uv sync --frozen --extra notebook
uv run --frozen --extra notebook marimo edit notebooks/reproduction.py
```

## Branch organization

`main` is the canonical reader-facing publication surface. The 16 historical
`orx/*` branches are preserved as descriptive `audit/*`, `experiment/*`,
`integration/*`, and `release/*` names, giving 17 branches including `main`.
The complete old-to-new mapping and the purpose of every branch are in
[`branch-audit.md`](branch-audit.md). No branch beginning with `orx/` remains
after cleanup. All reachable commits are attributed to `MachineLearning-Nerd`.

## Citation

```bibtex
@misc{choo2026learning,
  title         = {Learning Unanimously Acceptable Lotteries via Queries},
  author        = {Davin Choo and Paul W. Goldberg and Nicholas Teh},
  year          = {2026},
  eprint        = {2604.17505},
  archivePrefix = {arXiv},
  primaryClass  = {cs.GT},
  doi           = {10.48550/arXiv.2604.17505}
}
```

## Thank you

Thank you to Davin Choo, Paul W. Goldberg, and Nicholas Teh for making this
query-model paper and its source available for independent reproduction. The
clear separation between membership-query transcripts, exact finite
certificates, lower-bound constructions, and advice-sensitive algorithms made
it possible to audit both the mechanics and the quantifier boundaries
carefully. This repository is an independent audit and does not imply
endorsement by the authors.

## Attribution and license

Repository maintenance and reproduction commits are attributed to
**MachineLearning-Nerd**. The paper and source remain the property of their
authors; consult the [arXiv record](https://arxiv.org/abs/2604.17505) for the
paper’s license and reuse terms.
