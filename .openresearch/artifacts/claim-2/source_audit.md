# Source audit: Claim 2

Source: arXiv 2604.17505 TeX retrieved 2026-08-02, SHA-256 `73dd9aa76258e676da3cdec4454a84e5dc576b680424e1366a4fff719ed6b3ab`.

Algorithm 3 uses `r=16(m-1)^2`, samples `min(r,W)` labeled multiset copies uniformly without replacement, learns and caches the sampled support, solves its exact lexicographic subproblem, queries every agent, and doubles every violator's weight. Theorem 3.4 bounds expected queries by `O(nm log n + min(n,m^3 log n)m log(1/epsilon))`; correctness holds for every random realization.

The proof uses an extreme-copy double count, a witness of size at most `m`, positive expected log-potential drift `log(2)-1/4`, a stopping-time telescope for `E[T]=O(m log n)`, and `L<=min(n,rT)` plus Jensen.
