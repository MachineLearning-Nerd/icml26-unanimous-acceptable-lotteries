# Limitations and deviations

The certificate follows the paper's always-correct randomized model. Algorithms allowed a nonzero failure probability are outside this theorem and the per-seed reduction would not apply.

Finite enumeration audits the explicit family but does not quantify over algorithms. The proof-level decision-tree/Kraft/Yao certificate carries that quantifier.

The asymptotic rows instantiate `delta=1/2`; the symbolic derivation records where arbitrary fixed positive `delta` enters the constant hidden by `Omega`.
