# Homomorphisms are a Good Basis for counting small Subgraphs


---

## Abstract
- Graph motif parameters
	- depends only on the frequencies of constant-size induced subgraphs
- faster algo for counting subgraph copies of fixed graphs H in host graphs G

---

## 1 Introduction
- Deciding the existence of subgraph patterns H in input graphs G ~ classical subgraph iso problem
	- generalizes NP-complete problems, ex Hamiltonian cycle or clique.
- Existence of perfect matchings can be tested in polytime, counting version #P-hard



### 1.1 Counting small subgraphs
- For any fixed k-vertex pattern grpah H, we can count all subgraph copies of H in an n-vertex host graph G using brute-force for a running time of O(n^k)
	- Improvements: triangles, k-edge paths, vc(H)

Def: #Sub(H->G) number of subgraphs of G that are iso to H
- #Sub(H->G) in O(n^(t+1)), t ~ treewidth among the homomorphic images of H
Def: Hom image: any simple graph obtained from H by possibly merging non-adj vertices
Def: Spasm: set of all homomorphic images
 
Thm 1.1: input k-edge graph H, n-vertex graph G, we can compute #Sub(H->G) in k^O(k) * n^(t+1), t max tw in spasm of H

- merging vertices can never increase size of smallest vertex-cover
- vc >= tw
- contracting edges can not increase tw
- contracting non-edges can increase tw
- k-edge matching H, all k-edge graphs can be obtained by contracting non-edges => tw Omega(k)

Thm 1.2: Thm 1 + better boundary
Thm 1.3: all graphs in spasm of H have tw <= 2, #Sub in f(H)*|V(G)|^w, f(H) only dep on H

Counting exponential time hypothesis (#ETH):
No exp(o(n))*poly(m) algo to count all satisfying assignments of 3-CNF with n variables, m clauses.
No f(k)*n^o(k) algo to count all cliques of size exactly k.
-> k-clique hard special case of subgraph counting problem

?? Sub(Hclass), count H-copies in G for H in Hclass

Thm 1.4: Hclass recursively enumerable, unbounded vc number. If #ETH, then #Sub(Hclass) can not be in f(H)*n^(o(vc(H)/log(vc(H)))

- #W[1]-complete if equi under para red to counting k-cliques with turing red in time f(k)poly(n)
- #ETH => FPT != #W[1]

Thm 1.5: Hclass rec enu class of graphs. If Hclass has bounded vc, then #Sub(Hclass) is polytime computable, otherwise #W[1]-complete (para by size |V(H)|)



### 1.2 Counting small homomorphisms
Def: Homomorphism
Def: Injective <=> subgraph embedding from H to G
- spasm contains exactly loop-free hom images of H
- not requiring injecctivity makes counting patterns easier
=> separators to divide H into subpatterns to compose global one for H via dyn prog
- counting k-walks in G by taking the k-th power of the adjacency matrix of G

Prop 1.6: ex deterministic exp(O(k))+poly(k)*n^(t(H)+1) to compute number of homs from H to G, where k = |V(H)|, n=|V(G)|, tw of H

Thm 1.7: If H has tw <= 2, compute #Hom(H->G) in poly(|V(H)|)*|V(G)|^w
-> using fast matrix multiplication

Thm 1.8: Hclass rec enu. If Hclass has bounded tw, then #Hom(Hclass) is polytime, otherwise #W[1]-complete.

Prop 1.9: not relevant?



### 1.3 Counting small induced subgraphs
Thm 1.10: Hclass rec enu. If Hclass is finite, then #Ind(Hclass) of counting induced subgraphs is polytime, otherwise #W[1]-complete



### 1.4 A unified view: graph motif parameters
- reduction from subgraph counting to hom counting

Def: Embedding = injective Hom = sugraph F of G iso to H
- #Emb(H->G) = #Sub(H->G) * #Aut(H)
Ex: cannot map 2 adj vertices, hom from triangle must be inj

Def: #Emb(H->G) = #Hom(H->G) - sum_(F in Spasm(H)\{H}) #Emb(F->G)
=> Möbius inversion over partition lattice
- partitions p of V(H), each block independent set
- quotient graph H/p, merging each block of p into single vertex
=> injective <=> p_h is finest partition, i.e. each block size 1

Def: #Sub(H->G) = sum_p (-1)^...
=> important formula!

Def: graph motif parameter: any graph parameter f that is a finite linear comb of induced subgraph numbers
=> exists a_1, ..., a_t in Q, graphs H_1, ..., H_t: forall G: f(G) = sum_i=1^t a_i * #IndSub(H_i -> G)
- parameterize problem by description length k of a_1, ... and H_1, ...
- complexity of comp any graph para f ~ max complexity of counting the hom occuring in its representation over the hom basis
- If each #Hom(H_i -> G) can be comp in time O(n^c) for n =|V(G)|, then f(G) can be computed in time O(n^c)
- both directions hold (a_i != 0)
- equivalence is not true for lin comb of embedding numbers

Ex 1.12: Embeddings with cancellation effects

Thm 1.13: A ...
TODO: everything a little weird here.. Aclass of lin combs



### 1.5 Counting vertex-colored subgraphs
Def: colorful: every vertex of the pattern H has a different color
- count only subgraphs of G with iso to H that respect colors
- emb and homs are the same for colorful patterns.
- colorful pattern: bounded tw is the tractability criterion
- only technical change required: consider only partitions p that respect coloring

thm 1.14, 1.15: not needed?



## 2 Preliminaries
Def: Iverson bracket [P] in {0,1} whether P is satisfied
Def principal submatrix Ms submatix of M where selected row and column index sets are the same set S



### 2.1 Parameterized complexity theory
TODO



### 2.2 Graphs, subgraphs, and homomorphisms
- labeled, finite, undirected, simple graphs (no loops / parallel edges)

Def: Subgraph: V(F) subseteq V(G) and E(F) subsetseq E(G)
Def induced Subgraph: uv not in E(F) => uv not in E(G)

Def: Homomorphism
Def: Embedding: injective Homs
Def: Strong Embedding: non-edges map to non-edges
	=> {f(u), f(v)} not in E(G) for all {u,v} not in E(G)
Def: Surjective: all vertices and all edges
	- stronger than surjective on codomain
Def: iso: strong embedding that is also surjective
Def: Auto: Iso with H=G

Def: vertex-colored: adj vertices need distinct colors
Def: colorful: subg H of G is colorful if V(H) intersects each color class in exactly one vertex

Def: Tree Decomposition
TODO



## 3 The space of graph motif parameters
Def: graph parameters: functions f:G -> Q invariant under iso
Def: graph motif parameters: graph parameters that can be expressed as finite lin comb of induced sugraph numbers

- matrices indices with respect to |V(F)| + |E(F)|
- H > G => H can not be induced subgraph of G => IndSub(H,G)=0
=> IndSub upper triangular matrix

Def: support supp(alpha) of a vector alpha is the set of all graphs F in G* with alpha_F != 0

Def 3.1.: A graph parameter f:G*->Q is a graph motif parameter, if there is a vector 
alpha in Q^G* with finite support such that f(G)=sum_(F in G*) alpha_F * IndSub(F,G) holds for all G in G*

- interpret f and alpha as row vectors: f = alpha * IndSub for alpha of finite support

Def: scalar product: (alpha, beta) = sum_(F in G*) alpha_F * beta_F (if sum is defined)

- set of all graph motif parameters forms an infinite-dimensional vector space
=> finitely supported row-span of matrix IndSub

- even with infinite support alpha*IndSub is well-defined, since every column of IndSub has finite support
=> Every graph has only finitely many induced Subgraphs
- every graph parameter f can be written as alpha * IndSub for some alpha



## 3.1 Relations between graph motif parameters
- Subgraph and homomorphism numbers are graph motif parameters themself and span the same space
- complexity easier to understand over hom basis

=> Basis transformation

### Subgraphs and induced subgraphs:
- express Sub(H,G) as lin comb of numbers IndSub(F,G)
- every subgraph copy of H in G is contained in some induced subgraph F of G on |V(H)| vertices
=> ind subg F is iso to a supergraph of H

Def: Extensions: supergraphs
=> ext of H is a supergraph X of H with V(X) = V(H)
- different extensions can be isomorphic

Def: Ext(H,F): number of extensions X of H that are isomorphic to F
- Ext(H,F) = [|V(H)| = |V(F)] * Sub(H,F)
- Sub(H,G) = sum_(F in G*) Ext(H,F) * IndSub(F,G)

- only finitely many extensions => Sub(H,*) is graph motif parameter for every fixed H

- Sub = Ext * IndSub

- Sub, Ext, IndSub upper triangular matrices with diagonal 1
- invertible: IndSub = Ext^-1 * Sub

- Every function IndSub(H,*) is a finite linear combination of functions Sub(F,*) with coefficients Ext^-1(H,F)

- values of the coefficients Ext^-1(H,F): indentity interpreted as a zeta function over the subset lattice
=> Möbius inversion: Ext^-1(H,F) = (-1)^(|E(F)| - |E(H)|) * Ext(H,F) for all H and F
- Ext^-1(H,F) != 0 holds for specific pairs (H,F)

### Homomorphisms and subgraphs
- express Hom(H,G) as finitely supported lin comb sum_F alpha_F Sub(F,G) of subgraph numbers
TODO - Every hom H->G can be written as a surj hom into a subgraph F of G

Def: Hom(H,G) = sum_(F in G*) Surj(H,F) * Sub(F,G)
- Surj(H,F) = 0 holds if H is smaller than F
- Surj(H,F) != 0 only for finitely many F in G*

- Hom = Surj*Sub

- Surj is lower triangular, diagonal Surj(F,F) = Aut(F) != 0
=> invertible

- Sub = Surj^-1 * Hom

- Support of vector Surj(H,*): set of all unlabeled grpahs that are hom images of H
=> Spasm(H) = {F in G*: Surj(H,F) >=0}

Def: Partition like spasm
For H in G and partition p in Part(H), the quotient H/p is the graph obtained by identifying, for each block B in p, the vertices in B into a single vertex. 
- Keep loops intact, turn parallel edges into simple edges.








- F in G* does not have loops
- F iso H/p can only holdif all blocks of p are indep sets of H

- Every surj hom from H to F can be interpreted as a pair (p, pi) where H/p iso F and pi in Aut(F):
=> Surj(H,F) = #Aut(F)*sum_(p in Part(H)) [H/p iso F]

Def: p >= p': p coarser than p', i.e. every block of p' is in a block of p
Def: partition lattice (Part(H),>=): partially ordered set 
=> minimal element _|_ is the finest partition, i.e. all blocks have size one

Def: upwards zeta-transform on the partition lattice: f*(p) = sum_(p' >= p) f(p')

- Hom(H, G) = f*(_|_)

- Möbius Inversion.. not that important

- Surj^-1(H,F) = (-1)^... / Aut * sum prod (|B| - 1)!
- Surj^-1(H,F) != 0 <=> Surj(H,F) != 0 <=> F in Spasm(H)

- rows of Hom are linearly independent with respect to finite lin combs

Lemma 3.3: S subseteq G* finite set of graphs closed under surj homs, i.e. Spasm(H) subseteq S for all H in S.
Then the principal submatrix Hom_S of Hom is invertible and satisfies Hom_S = Surj_S * Sub_S
Proof: short: closed => only terms with F in S contribute to sum (10)

- Every graph F in Spasm(H) has at most |V(H)| vertices and at most |E(H)| edges

picture: Hom_S = Surj_S * Sub_S

### Embeddings and strong embeddings
- Iso is diag matrix with Iso(F,F) = Aut(F)
- Emb = Iso  * Sub
- StrEmb = Iso * IndSub



## 3.2 The complexity of graph motif parameters

- evaluation problem: input graph motif parameter f:G* -> Q and a graph G in G*, compute value f(G)
=> homomorphism basis
- represent f as vector-matrix products f = alpha * Hom for finitely supported row vectors alpha in Q^G*
- coefficient vector alpha, encoded as a list of pairs (F, alpha_F) for F in suppa(alpha)
- |alpha| description length of alpha
- tw(alpha) maximum tw(F) among all F in supp(alpha)

Lemma 3.5 Algorithm: There is a det algo with inputs alpha and G to compute (alpha * Hom)(G) in time 
g(alpha) + poly(|alpha|) * |V(G)|^(tw(alpha) + 1) for some computable func g
Proof: foreach F in supp(alpha), run algo from Prop 1.6 to comp Hom(F,G) in time exp(O(k)) + poly(k)*n^(tw(F)+1), k = |V(F)|, n=|V(G)|. Output sum_F alpha_F Hom(F,G)

- eval problem for graph motif paras is #W[1]-hard, since it subsumes counting k-cliques as a special case
- evaluating f with f = alpha*Hom is at least as hard as every individual hom problem Hom(F;*) for F in supp(alpha)

Lemma 3.6 Extracting summands: there is a det Turing red that is given a finitely supported vector alpha in Q^G*, a graph F in supp(alpha) and a graph G in G* to compute the number Hom(F,G) 
with an oracle for the function (alpha * Hom)(*). The red runs in time g(alpha) * poly(|V(G)|) for some comp function g, makes at most g(alpha) queries to (alpha*Hom)(*) and each queried graph has at most max_(H in supp(alpha)) |V(H)|*|V(G)| vertices.
Proof: On input (alpha, F, G) the reduction only makes queries of the form (alpha * Hom)(G times X) for grpahs X, where G x G is the categorical product:
graph with vertex set V(G) times V(X) such that (v,x) and (v',x') are adjacent in G x X iff vv' in E(G) and xx' in E(X).
15: Hom(F,G x X) = Hom(F,G) * Hom(F,X)
16: sys lin eq: sum_H alpha_H * Hom(H,G) * Hom(H,X) = (alpha * Hom)(G x X)
=> compute right side of lin eq using oracle, determine numbers alpha_H and Hom(H,X) in some time f(alpha)
- choose suitable set S of graphs X so that resulting sys lin eq can be uniquely solved for Hom(F,G)
- S = U_(H in supp(alpha)) Spasm(H), closure of supp(alpha) under spasms
- alpha Hom = alpha_S Hom_S
- rewrite 16 as Hom_S * x = b, Hom_S in Q^(S x S)
-> b_X = (alpha * Hom)(G x X), Hom_S(H,x)=Hom(H,X)
-> vector x in Q^S repr indeterminates with x_H = alpha_H * Hom(H,G)
- x = (Hom_S)^-1 * b
- Hom(F,G) = x_F / alpha_F computable since alpha_F != 0 by assumption
- set S and matrices Hom_S, Hom_S^-1 can be computed in time g(alpha)
- vector b: compute product graphs and query oracle
-> number of queries |S| bounded by g(alpha)
-> overall time g(alpha) * poly(|V(G)|)

Def 3.7: Aclass subseteq Q^G* set of finitely supported vectors. Let #Hom(Aclass) be the comp prob whose task is to compute (alpha * Hom)(G) on input alpha in Aclass and G in G*

Lemma 3.8 (Hardness) Aclass subseteq Q^G* be rec enu class of fin supported vectors. If Aclass contains vectors of arbitrarily large tw(alpha), then #Hom(Aclass) is #W[1]-hard when para by |alpha|.
Moreover, the problem does not have g(alpha) * |V(G)|^o(tw(alpha) log(tw(alpha)) time algorithms if #ETH holds.

TODO



## 4 Algorithms for counting subgraphs
- counting subgraphs and embedding via hom basis and running an algo for counting homs
- Recall: Sub(H,G) = sum_F Surj^-1(H,F) * Hom(F,G)
- Recall: Surj^-1(H,F) != 0 <=> F in Spasm(H)
- if comp hom numb Hom(F,G) for all F in Spasm(H) in time O(n^c) on n-verte graphs G, then we can comp Sub(H,G) in time O(n^c)
-> Prop 1.6 => O(n^c) governed by max tw among Spasm(H)

Thm 1.1 (restated)

















