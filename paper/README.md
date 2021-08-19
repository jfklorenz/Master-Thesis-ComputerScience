# Paper

**Table of Contents:**

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Paper](#paper)
	- [Legend](#legend)
	- [Graph Homomorphism Polynomials](#graph-homomorphism-polynomials)
		- [ToDo](#todo)
	- [Lovasz Meets Weisfeiler and Leman](#lovasz-meets-weisfeiler-and-leman)
		- [Theorem 1](#theorem-1)
		- [ToDo](#todo)

<!-- /TOC -->

---

## Legend

Color | Content
--- | ---
<span style="color:red">RED</span> | Definitions, Theorems, Lemmata
<span style="color:yellow">YELLOW</span> | Scientific information
<span style="color:green">GREEN</span> | Historical information
<span style="color:blue">BLUE</span> | Examples
<span style="color:purple">PURPLE</span> | References

---

## Graph Homomorphism Polynomials
- [Graph Homomorphism Polynomials: Algorithms and Complexity](https://arxiv.org/abs/2011.04778)
- First E-Mail, Paper 1
- homomorphism polynomials: enumerate all homomorphisms from a pattern graph $H$ to $n$-vertex graphs.
- polynomial families which are complete for algebraic complexity classes $VBP$, $VP$ and $VNP$



### ToDo
- homomorphism polynomials
- pattern graphs
- treedepth
- pathwidth
- treewidth of the pattern graph

---

## Lovasz Meets Weisfeiler and Leman
- [Lovász Meets Weisfeiler and Leman](https://arxiv.org/abs/1802.08876)
- First E-Mail, Paper 2, from Dell

- Graph G can be characterized by counting homomorphisms from all graphs F to G.
=> G isomorphic to H <=> homomorphism from F to G equals F to H
- homomorphism vector is NP-complete
=> restrict to class where it can be computed in poly time

### Theorem 1
How expressive are homomorphism vectors $HOM_F(G)$ for restricted graph classes $F$? Consider the class $T$ of trees:
1. $Hom_T(G) = HOM_T(H)$
2. Color refinement does not distinguish $G$ and $H$
3. $G$ and $H$ are fractionally isomorphic, that is, the system $F_{ISO}(G, H)$ of linear equations has a non-negative real solution.



### ToDo
- References [18], [19]?
- homomorphism vector
- color refinement algorithm
