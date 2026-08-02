# Claim 3 exhaustive method

Enumerate every utility vector and positive threshold for complete domains `(m=2, K=2..12)`, `(m=3, K=2..6)`, and `(m=4, K=2..3)`, where `K=1/epsilon`. Run literal Algorithm 1 for every agent and compare its returned classifier with the independent expected-utility oracle on every simplex-grid point of denominator `2 K^2`.

Independently reconstruct the continuous proof: exact edge turning points imply `c_j=(u_j-u_r)/(tau-u_r)` in the nondegenerate case, so the normalized learned inequality is algebraically equivalent to expected-utility acceptability on the entire simplex.

Controls mutate `>=` to `>` at the boundary and skip one necessary edge. The first changes an exact boundary label; the second leaves identical observed transcripts for two distinct valid halfspaces.
