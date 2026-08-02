# Claim 3 method

## Route A: exact large-scale query growth

Run literal `LearnHyperplane` on a worst-case quantized family forcing all `m-1` edge searches. Sweep the Cartesian product of powers of two `m=2..256` and `1/epsilon=2..1024`. No query budget or horizon is selected from the theorem. A standalone checker recomputes the exact count without calling Algorithm 1.

## Route B: exhaustive correctness and symbolic lift

Enumerate every utility vector and positive threshold for complete domains `(m=2, K=2..12)`, `(m=3, K=2..6)`, and `(m=4, K=2..3)`. Compare Algorithm 1 with an independent expected-utility oracle on every grid point of denominator `2K^2`.

Reconstruct the continuous proof: exact turning points give `c_j=(u_j-u_r)/(tau-u_r)`, hence `<c,x> >= 1` iff `<u,x> >= tau` because simplex coordinates sum to one. At most `m-1` searches each use logarithmically many queries.

Controls remove quantization, remove edge searches, mutate inclusive boundary membership, and skip a necessary edge.
