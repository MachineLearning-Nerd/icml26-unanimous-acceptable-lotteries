# Claim 4 — VERIFIED

## Exact contract and assumptions

For every correct deterministic or always-correct randomized algorithm, worst-case expected queries are `Omega((n-min(n,m))+(min(n,m)-1)log(1/epsilon))`; for `n=1`, `Omega(m)` (Theorems 4.1–4.2). The counting step explicitly audits the paper's fixed-positive-`delta` precision assumption.

## Inline result

Six exact decision-tree rows cover `n>=m` and `n<m`, reaching `n=1,000,000`, `m=128`, and `1/epsilon=65,536`; minimum conservative certificate/target ratio was 0.7113095. Three complete domains checked 449 singleton hard instances and 158,323 grid comparisons. The exhaustive symmetry-reduced minimax recurrence equaled `m` for every single-agent case `m=1..64`.

This is a proof over algorithms: distinct singleton outputs force leaves; mandatory agent queries and dummy pruning add the linear term; Kraft and Yao supply randomized average/worst-case expectation. Four invalid-assumption controls failed as intended.

## Reproduce and inspect

- Git `489194915b8918e1fac2bbe3aadcd3db79f973c7`; HF `cpu-upgrade`; 64 CPUs; 368.871289 s; no seeds.
- [Verifier](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/code/claim4_lower_bound.py), [checker](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/code/claim4_verify_claim.py), [raw bound](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/evidence/claim-4/raw_lower_bound.json), [exhaustive](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/evidence/claim-4/raw_exhaustive.json), [minimax](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/evidence/claim-4/raw_minimax.json), [controls](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/evidence/claim-4/negative_control_output.json), [proof](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/evidence/claim-4/proof_certificate.json)

Limitation: algorithms allowed error are outside the paper's per-seed-correct model.
