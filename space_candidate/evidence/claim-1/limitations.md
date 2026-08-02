# Limitations and deviations

The large empirical family uses coordinate halfspaces because their lexicographic optimum is available exactly without a third-party LP dependency. It does not sample every possible halfspace. Universal correctness and complexity therefore rely on the independently reconstructed invariant and counting certificate, not empirical slope fitting.

The calibrated quadratic regime co-varies `m` and precision with `n` so that a feasible instance can contain a linear number of positive coordinate lower bounds. Its literal dense-lottery endpoint is `n=128, m=65`; larger dense endpoints were rejected because tuple construction measures representation overhead rather than membership-query complexity. Separate literal sweeps reach `n=65,536`, `m=256`, and `1/epsilon=65,536` independently to expose this coupling rather than hiding it.

Offline LP computation is not included in membership-query counts, matching the paper.
