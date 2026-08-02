# Claim 3 method

The literal `LearnHyperplane` implementation is run on a worst-case quantized family with one rejected vertex, `m-1` accepted vertices, and turning point `1/2` on every searched edge. This forces all `m-1` threshold searches.

The sweep is the Cartesian product `m = 2,...,256` and `1/epsilon = 2,...,1024`, both in powers of two. No query budget, tolerance, or stopping horizon is selected from the claimed bound. The algorithm runs to its source stopping rule.

An independent CSV checker derives the exact bisection depth from bounded-denominator rational separation and recomputes every expected query count without calling `LearnHyperplane`. It also checks the two scaling axes and their regression residuals.

Controls remove finite precision (`tau = 1/17` at `epsilon = 1/16`) and remove edge searches (two halfspaces with identical vertex labels but opposite midpoint labels). Both must fail for the intended reason.
