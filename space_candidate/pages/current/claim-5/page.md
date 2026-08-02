# Claim 5 — VERIFIED

## Exact contract and assumptions

Algorithm 2[`sigma`] changes only scan order. `R(sigma)` is exactly the number of LearnHyperplane calls. For `R>=1`, queries are `O((n+m log(1/epsilon))R)`; `R=0` uses the paper's separate initial-`n`-query footnote (Theorem 5.1).

Source TeX SHA-256: `73dd9aa76258e676da3cdec4454a84e5dc576b680424e1366a4fff719ed6b3ab`.

## Inline result

Forty exact rows reached `n=65,536`, `m=256`, `1/epsilon=65,536`. Permutations realized `R=1,2,4,8,16,32,64,128,256` exactly. At `n=8,192`, total queries were exactly `8,192+7,958R`, reaching 2,045,440. Every row matched its transcript and finite envelope. `R=0` made exactly 4,096 queries. The checker detected corruption; three controls failed as intended.

## Reproduce and inspect

- Git `65f10745687b9bf38e7983b320586c1cb250a6ad`; HF `cpu-upgrade`; 64 CPUs; 382.691014 s; no stochastic seeds.
- Fixed command: `uv sync --frozen && uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py`.
- [Verifier](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/code/claim5_prediction.py), [checker](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/code/claim5_verify_claim.py), [raw CSV](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/evidence/claim-5/raw_scaling.csv), [checker output](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/evidence/claim-5/checker_output.json), [controls](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/evidence/claim-5/negative_control_output.json), [proof](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/evidence/claim-5/proof_certificate.json)
- [Claim contract](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/evidence/claim-5/claim_contract.json), [source audit](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/evidence/claim-5/source_audit.md), [method](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/evidence/claim-5/method.md), [full evaluator record](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/evidence/claim-5/EVAL.md)

Limitation: controlled nested constraints realize operational `R`; no rank-correlation proxy is claimed.
