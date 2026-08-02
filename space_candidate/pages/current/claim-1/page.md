# Claim 1 — VERIFIED

## Exact contract and assumptions

Under the paper's epsilon-quantized model (`n` agents, `m` alternatives, `epsilon<=1/2`, integral `1/epsilon`, inclusive membership oracle), literal Algorithm 2 returns a unanimously acceptable lottery iff one exists and uses `O(n^2+nm log(1/epsilon))` queries (Algorithm 2; Theorem 3.3). Source TeX SHA-256: `73dd9aa76258e676da3cdec4454a84e5dc576b680424e1366a4fff719ed6b3ab`.

## Inline result

The 37-row exact sweep reached `n=65,536`, `m=256`, `1/epsilon=65,536`, and 591,568 queries. The hard family satisfied `n^2/4 <= q_verify <= n^2/3`; every row matched exact transcript counts and the finite theorem envelope. Feasible, infeasible, and RejectAll cases passed. Three mutations failed as intended. The standalone checker passed and detected deliberate corruption.

Universal proof obligations establish the loop invariant, both sound Null paths, at most `n+1` rounds, at most `n` elicitation calls, and verification sum `n(n+1)/2`; finite scaling is an implementation audit, not the quantifier lift.

## Reproduce and inspect

- Fixed command: `uv sync --frozen && uv run --frozen python repro/src/verify.py && uv run --frozen python repro/src/publication_gate.py`
- Git `068fd258ad80e430a2c1fd25ed390eecb3795c27`; HF `cpu-upgrade`; 64 logical/affinity CPUs; 288.784583 s; no stochastic seeds.
- [Verifier](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/code/claim1_deterministic.py), [independent checker](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/code/claim1_verify_claim.py)
- [Raw CSV](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/evidence/claim-1/raw_scaling.csv), [checker output](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/evidence/claim-1/checker_output.json), [controls](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/evidence/claim-1/negative_control_output.json), [proof](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/evidence/claim-1/proof_certificate.json)

Limitation: the scalable family uses exact coordinate LPs; the universal certificate, not family representativeness, supports the theorem.
