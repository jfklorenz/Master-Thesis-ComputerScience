# Complexity


---

## ETH


---

## FPT
- Fixed parameter tractable
A parameterized problem L is fixed-parameter tractable if the question (x,k) in L can be 
decided in running time f(k) * |x|^O(1), where f is an arbitrary function depending only on k.
The corresponding complexity class is called FPT.
- f usually like 2^O(k)
- graph coloring (by number of colors) in FPT => P = NP

## W hierarchy
Problem in W[i], if every instance (x, k) can be transformed in fpt-time to a comb circuit that has weft at most i, such that (x,k) in L 
if and only if there is a satisfying assignment to the inputs that assings 1 to exactly k inputs.
- weft is the largest number of logical units with unbounded fan-in on any path from an input to output.
- FPT = W[0]

### Examples W[1]
- deciding if clique of size k
- deciding if ind.set of size k

### Examples W[2]
- deciding if dominating set of size k

---

## Other

- quasi-linear: O(n log^k n)
- super-poly: w(n^k), not bounded by poly, outside of P
- Quasi-poly: 2^O(log^c n), c = 1 ~ poly, c < 1 ~ sublinear