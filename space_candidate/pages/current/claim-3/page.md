# Claim 3 — VERIFIED

## Exact claim contract

For every integer `m >= 2` and `epsilon in (0, 1/2]` with integer `1/epsilon`, and every agent with utilities in `{0, epsilon, ..., 1}` and threshold in `{epsilon, ..., 1}`, Algorithm 1 returns an exact representation of the agent’s inclusive expected-utility acceptability halfspace using `O(m log(1/epsilon))` membership queries.

Source anchors: Algorithm 1 (`alg:learnhyperplane`), Lemma 3.1 (`lem:learnhyperplane_queries`), Lemma 3.2 (`lem:learnhyperplane_correctness`), and the finite-precision assumptions in `sec:prelims`. The arXiv TeX archive SHA-256 is `73dd9aa76258e676da3cdec4454a84e5dc576b680424e1366a4fff719ed6b3ab`.

## Strongest evidence

| Evidence | Result |
| --- | ---: |
| Exact scaling rows | 80 |
| Largest dimension | 256 alternatives |
| Finest precision | `epsilon = 1/1024` |
| Maximum observed queries | 5,866 |
| Exact-envelope mismatches | 0 |
| Dimension log-log slope | 1.012482 |
| Dimension fit `R^2` | 0.999986 |
| Queries vs `log2(1/epsilon)` fit `R^2` | 1.000000 |
| Complete finite domains | 18 |
| Valid agents exhaustively checked | 12,272 |
| Exact simplex cells checked | 9,882,192 |
| Independent checker failures | 0 |
| Intended control failures detected | 4/4 |

The exact worst-case family forces all `m-1` edge searches. Every measured count equals the independently reconstructed formula `m + (m-1) bit_length(2/epsilon^2)`. Separately, exact turning-point recovery gives `c_j=(u_j-u_r)/(tau-u_r)`, so on the simplex `<c,x> >= 1` is algebraically equivalent to `<u,x> >= tau`. This symbolic identity, not finite extrapolation, carries the universal correctness quantifier.

## Reproducible materials

- Fixed command: `uv sync --frozen && uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py`
- Environment: Python 3.12, repository `pyproject.toml` and `uv.lock`, no third-party dependencies.
- Route A: Git `b42cc1c3f37b7a6577d65a96096854e7d831bde9`; HF `cpu-upgrade`; 64 logical/affinity CPUs; verifier 90.522974 s; no stochastic seeds.
- Route B: Git `c7469b37254866a008239eef79d23c015d859dcc`; HF `cpu-upgrade`; 64 logical/affinity CPUs; verifier 122.239276 s; no stochastic seeds.
- [Raw scaling CSV](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/evidence/claim-3/raw_scaling.csv)
- [Raw exhaustive JSON](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/evidence/claim-3/raw_exhaustive.json)
- [Scaling checker](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/evidence/claim-3/scaling_checker_output.json)
- [Exhaustive checker](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/evidence/claim-3/exhaustive_checker_output.json)
- [Scaling verifier source](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/code/claim3_scaling.py)
- [Exhaustive verifier source](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/code/claim3_exhaustive.py)
- [Standalone checker source](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/code/verify_claim.py)

## Controls and limitations

Controls remove finite precision, use vertex labels without edge searches, change inclusive `>=` to strict `>`, and skip a necessary edge. Each is detected for its intended reason. The scaling family is worst-case, not representative. Finite sweeps and exhaustive small domains are corroboration; the exact algebraic certificate is required for the universal verdict.
