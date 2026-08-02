# Source audit: Claim 4

Source: arXiv 2604.17505 TeX retrieved 2026-08-02 from `https://export.arxiv.org/e-print/2604.17505`, SHA-256 `73dd9aa76258e676da3cdec4454a84e5dc576b680424e1366a4fff719ed6b3ab`.

Theorem 4.1 (`thm:lowerbound_query`) quantifies over every correct deterministic or randomized algorithm and lower-bounds worst-case expected membership queries by `Omega((n-min(n,m)) + (min(n,m)-1) log(1/epsilon))`. The counting step uses the preliminary fixed-`delta` assumption `m <= (1/epsilon)^(1-delta)`.

The proof constructs a positive epsilon-grid family with `binomial(1/epsilon-1, p-1)` distinct singleton outputs, where `p=min(n,m)`. For `n>=m`, always-accepting dummy agents force another `n-m` queries. Kraft's inequality supplies an average-depth bound and Yao's principle transfers it to always-correct randomized algorithms.

Theorem 4.2 uses one infeasible single-agent instance and `m` feasible singleton-vertex instances. Only query `e_j` distinguishes feasible instance `j` from the all-False infeasible transcript, so every correct deterministic seed must query all `m` vertices.
