# Method

This verifier certifies a lower bound over algorithms; it does not run Algorithm 2 and mistake its cost for a minimax result.

It independently reconstructs the singleton hard family, exact binomial leaf count, dummy-agent pruning, binary-tree/Kraft depth bounds, and Yao reduction. Six large parameter rows cover both `n>=m` and `n<m` under an explicit `delta=1/2` assumption audit. Three complete finite domains enumerate every positive-grid hard instance against every grid lottery.

For the separate `n=1` result, an exact symmetry-reduced exhaustive policy recurrence evaluates all remaining candidate counts through `m=64`: a nonvertex query eliminates none, while a vertex query can eliminate at most one feasible singleton on a False answer, giving exact minimax value `m`.
