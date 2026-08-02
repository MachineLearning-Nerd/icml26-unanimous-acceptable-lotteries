# Claim 2 — VERIFIED

## Exact contract and assumptions

Algorithm 3 uses `r=16(m-1)^2`, uniform sampling without replacement from labeled weight copies, cached exact halfspaces, lexicographic Select, full verification, and violator doubling. For always-correct randomness it has expected complexity `O(nm log n + min(n,m^3 log n)m log(1/epsilon))` (Theorem 3.4).

## Inline result

Forty deterministic-seed runs used `n=32,768`, `epsilon=1/64`, and `m=4,8,16,24,32` (sample cap through 15,376). Mean rounds were 11.500, 11.875, 13.875, 15.625, 16.250 with 95% CI halfwidths 1.228, 1.306, 1.590, 1.654, 2.690. Mean total queries rose from 383,366.5 to 1,594,062; every mean was below the reconstructed finite expectation envelope. Maximum: 21 rounds and 1,750,158 queries.

The proof certificate checks the extreme-copy sampling lemma, basis/Helly witness, witness hit, drift `log(2)-1/4`, stopping-time telescope, `L<=min(n,rT)`, Jensen, and query decomposition. Controls distinguish without-replacement sampling, no reweighting, and caching.

## Reproduce and inspect

- Same fixed command and locked Python 3.12 environment; seeds `0..7` per `m`.
- Git `be3545e0410b2cdaf9e98eccb7acf4f0b9df3def`; HF `cpu-upgrade`; 64 CPUs; 539.627361 s.
- [Verifier](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/code/claim2_randomized.py), [checker](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/code/claim2_verify_claim.py), [raw runs](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/evidence/claim-2/raw_seed_runs.json), [summary](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/evidence/claim-2/raw_summary.json), [controls](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/evidence/claim-2/negative_control_output.json), [proof](https://huggingface.co/spaces/DineshAI/daiccpXZfU/blob/main/evidence/claim-2/proof_certificate.json)

Limitation: seeded coordinate-basis runs audit implementation and finite constants; the proof certificate carries the universal expectation.
