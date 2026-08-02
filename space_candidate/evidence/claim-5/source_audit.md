# Source audit: Claim 5

Source: arXiv 2604.17505 TeX retrieved 2026-08-02 from `https://export.arxiv.org/e-print/2604.17505`, SHA-256 `73dd9aa76258e676da3cdec4454a84e5dc576b680424e1366a4fff719ed6b3ab`.

The paper defines Algorithm 2[`sigma`] by changing only the order in which unlearned agents are scanned. `H(sigma)` is the set of agents on which LearnHyperplane is invoked during that execution and `R(sigma)=|H(sigma)|`.

Theorem 5.1 (`thm:perm-det`) states correctness and query complexity `O((n + m log(1/epsilon)) R(sigma))`. The proof first establishes the exact finite form with `R+1` verification rounds and then uses `R+1 <= 2R` under its explicit `R>=1` convention. Its footnote separately states that `R=0` terminates after the initial scan using at most `n` queries.
