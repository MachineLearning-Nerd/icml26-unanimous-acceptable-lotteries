# Method

The verifier executes literal Algorithm 2 on exact rational, epsilon-quantized coordinate-halfspace instances. On this family, the paper's lexicographic linear program has an independently derived closed form: each learned constraint is `x_j >= a_j`, all non-first coordinates take their lower bounds, and the remaining mass goes to the first coordinate. This is exact `Select`, not a grid approximation.

Four independently selected sweeps isolate a calibrated quadratic-verification regime and independent variation in `n`, `m`, and `1/epsilon`. Literal execution reaches `n=65,536`, `m=256`, and `1/epsilon=65,536` in the independent regimes. The verifier records verification and hyperplane-learning queries separately and compares them only afterward with the exact finite envelope.

The universal quantifier is discharged by a machine-checked proof-obligation certificate: learned constraints are oracle-equivalent; the loop invariant covers learned agents; every nonterminal iteration removes one agent; at most `n` hyperplanes are learned; verification costs at most `n+(n-1)+...+1`; and the independently established Algorithm-1 envelope is substituted.

Feasible, jointly infeasible, and `RejectAll` instances are checked. Mutations cover a missing restart, a dropped learned constraint, and changing inclusive acceptance to strict acceptance.
