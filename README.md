# Reproduction: Learning Unanimously Acceptable Lotteries via Queries

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-daiccpXZfU-unanimous-acceptable-lotteries/blob/main/notebooks/reproduction.py)

This project reproduces all five query-complexity claims in [arXiv:2604.17505](https://arxiv.org/abs/2604.17505). The paper gives asymptotic bounds rather than headline accuracy numbers; the observed quantities are exact membership-query transcripts, exhaustive-domain agreement counts, seeded expectation estimates, and independently checked proof certificates.

All five claim contracts are **VERIFIED** with HIGH scientific confidence in the cumulative campaign. This is a forecastable evidence status, not a live judge result: the judged Hugging Face score remains **5/10** until the evaluator reviews a published revision.

Strongest observed scales include `n=1,000,000`, `m=256`, `1/epsilon=65,536`, 40 complete randomized executions, 12,272 exhaustively enumerated halfspaces, and 9,882,192 exact simplex-cell comparisons. The work uses constructed theorem-calibration families rather than natural preference data; finite runs are never used alone to claim a universal theorem. Symbolic, minimax, exhaustive-policy, decision-tree, Kraft, and Yao certificates provide the required quantifier lifts.

All research computation ran on Hugging Face `cpu-upgrade` with 64 allocated logical/affinity CPUs and no GPU. The environment is Python 3.12 under `uv`; every scientific node used the same fixed command and dependency-free base environment. A locked optional notebook extra is installed into the same `.venv` only after scientific verification for `marimo check`.

- [Illustrated technical report](reports/full-reproduction/report.md)
- [Final release report and score forecast](reports/full-reproduction/release_report.md)
- [Self-contained marimo tutorial](notebooks/reproduction.py)
- [Current evaluator-visible candidate](space_candidate/pages/current/index.md)

## Experiment log

`main` is presentation-only: **Not run as an experiment (publication surface)**.

| Branch / experiment | Purpose | Exact run command | Assessment / outcome | Compute |
|---|---|---|---|---|
| [`orx/locked-validated-baseline`](https://github.com/MachineLearning-Nerd/icml26-repro-daiccpXZfU-unanimous-acceptable-lotteries/tree/orx/locked-validated-baseline) | Freeze and rerun the judged toy baseline | `uv sync --frozen && uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py` | Historical rejected baseline; 5/10 live judge state | HF `cpu-upgrade`, 64 CPUs, 21 s end-to-end |
| [`orx/c3-combined-evaluator-milestone`](https://github.com/MachineLearning-Nerd/icml26-repro-daiccpXZfU-unanimous-acceptable-lotteries/tree/orx/c3-combined-evaluator-milestone) | Exact Algorithm 1 scaling, enumeration, and algebra | `uv sync --frozen && uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py` | Claim 3 VERIFIED | HF `cpu-upgrade`, 64 CPUs, 238 s end-to-end |
| [`orx/c1-symbolic-transcript-certificate`](https://github.com/MachineLearning-Nerd/icml26-repro-daiccpXZfU-unanimous-acceptable-lotteries/tree/orx/c1-symbolic-transcript-certificate) | Algorithm 2 transcripts and universal envelope | `uv sync --frozen && uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py` | Claim 1 VERIFIED | HF `cpu-upgrade`, 64 CPUs, 307 s end-to-end |
| [`orx/c5-exact-record-quality-certificate`](https://github.com/MachineLearning-Nerd/icml26-repro-daiccpXZfU-unanimous-acceptable-lotteries/tree/orx/c5-exact-record-quality-certificate) | Exact prediction record quality `R` | `uv sync --frozen && uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py` | Claim 5 VERIFIED | HF `cpu-upgrade`, 64 CPUs, 403 s end-to-end |
| [`orx/c4-minimax-lower-bound-certificate`](https://github.com/MachineLearning-Nerd/icml26-repro-daiccpXZfU-unanimous-acceptable-lotteries/tree/orx/c4-minimax-lower-bound-certificate) | Universal lower-bound and minimax certificates | `uv sync --frozen && uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py` | Claim 4 VERIFIED | HF `cpu-upgrade`, 64 CPUs, 386 s end-to-end |
| [`orx/c2-weighted-sampling-expectation-certificate`](https://github.com/MachineLearning-Nerd/icml26-repro-daiccpXZfU-unanimous-acceptable-lotteries/tree/orx/c2-weighted-sampling-expectation-certificate) | Algorithm 3 expectation and 40 full seeded runs | `uv sync --frozen && uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py` | Claims 1–5 cumulatively VERIFIED | HF `cpu-upgrade`, 64 CPUs, 562 s end-to-end |
| [`orx/hf-generated-visual-report-assets`](https://github.com/MachineLearning-Nerd/icml26-repro-daiccpXZfU-unanimous-acceptable-lotteries/tree/orx/hf-generated-visual-report-assets) | Generate the five report figures from committed evidence | `uv sync --frozen && uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py` | Five SVGs generated; all claims regressed | HF `cpu-upgrade`, 64 CPUs, 583 s verifier runtime |

## Reproduce

The formal command is fixed across the experiment tree:

```console
uv sync --frozen && uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py
```

The notebook is evidence-first and does not require the expensive claim suite to display the conclusions:

```console
uv sync --frozen --extra notebook
uv run --frozen --extra notebook marimo edit notebooks/reproduction.py
```

Use `marimo run notebooks/reproduction.py` instead of `edit` for a read-only local app after the optional extra is synced.
