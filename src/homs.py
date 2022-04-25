# Hom, Emb, Surj, Sub, Iso, Matrices
# ----------------------------------------------------------------
"""
Hom(F, G): Number of homomorphisms from F to G
Emb(F, G): Number of injective homomorphisms from F to G
Surj(F, G): Number of surjective homomorphisms from F to G
Sub(F, G): Number of times F occurs as a subgraph in G
Iso(F, G): Number of isomorphisms from F to G

Matrices(Gs, f): Matrix for a list of graphs and their relation with respect to f
"""

# ----------------------------------------------------------------
# Imports
import networkx as nx
import itertools
import numpy as np

# --------------------------------------
# #Hom(F -> G)
def Hom(F, G):
    m, n = F.number_of_nodes(), G.number_of_nodes()
    perm = list(itertools.product([i for i in range(n)], repeat=m))
    cnt = 0
    for per in perm:
        homomorphism = True
        for edge in F.edges():
            if not (((per[edge[0]], per[edge[1]]) in G.edges()) or ((per[edge[1]], per[edge[0]]) in G.edges())):
                homomorphism = False
                break
        if homomorphism:
            cnt += 1
    return cnt

# --------------------------------------
# #Emb(F -> G)
def Emb(F, G):
    m, n = F.number_of_nodes(), G.number_of_nodes()
    perm = list(itertools.product([i for i in range(n)], repeat=m))
    perm = [per for per in perm if (len(set(per)) == m)]
    cnt = 0
    for per in perm:
        homomorphism = True
        for edge in F.edges():
            if not (((per[edge[0]], per[edge[1]]) in G.edges()) or ((per[edge[1]], per[edge[0]]) in G.edges())):
                homomorphism = False
                break
        if homomorphism:
            cnt += 1
    return cnt
    
# --------------------------------------
# #Surj(F -> G)
def Surj(F, G):
    m, n = F.number_of_nodes(), G.number_of_nodes()
    perm = list(itertools.product([i for i in range(n)], repeat=m))
    perm = [per for per in perm if (len(set(per)) == n)]
    cnt = 0
    for per in perm:
        homomorphism = True
        for edge in F.edges():
            if not (per[edge[0]], per[edge[1]]) in G.edges():
                homomorphism = False
                break
        edges = []
        for g in F.edges():
            x = (per[g[0]], per[g[1]])
            x1 = list(x)
            x1.sort()
            edges.append(x1)
        edges = list(edges for edges,_ in itertools.groupby(edges))
        new_edges = []
        for elem in edges:
            if elem not in new_edges:
                new_edges.append(elem)
        edges = new_edges
        if not (len(G.edges()) == len(edges)):
            homomorphism = False
        if homomorphism:
            cnt += 1
            print(per)
    return cnt  

# ---------------------------------
# Count Isomorphisms
def Iso(G, H):
    n = G.number_of_nodes()
    m = H.number_of_nodes()
    AG = nx.adjacency_matrix(G)
    AG = AG.todense()
    AH = nx.adjacency_matrix(H).todense()
    G = G.edges()
    H = H.edges()
    
    if n != m or len(G) != len(H):
        return 0
    
    rangeG = [i for i in range(n)]
    assignments = list(itertools.permutations(rangeG))
    
    cnt = 0
    for a in assignments:
        P = np.zeros((n,n))
        for i in range(len(a)):
            P[i][a[i]] = 1
        I = np.matmul(P, AG)
        I = np.matmul(I, np.transpose(P))
        
        if np.allclose(I, AH):
            cnt += 1
        
    return cnt

# ---------------------------------
# Count Subgraphs
def Sub(F, G):
    return Emb(F, G) / Iso(F,F)

# ---------------------------------
# Matrices
def matrices(GS, f):
    n = len(GS)
    A = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            x = GS[i]
            y = GS[j]
            A[i][j] = f(x,y)
    return A 
