# SPASM
# ----------------------------------------------------------------
"""
test


Returns:
    list of networkx graphs: List of graph-spasms
"""

# ----------------------------------------------------------------
# Imports
from collections import Counter
import networkx as nx
from globals import *

# ----------------------------------------------------------------
# Spasm
def spasm(G, pure = False):
    """ returns a list of all spasm graphs of the input graph."""
    """ Does return the graph itself."""
    
    # Base Case
    if nx.is_isomorphic(G, nx.complete_graph(2)) or nx.is_isomorphic(G, nx.complete_graph(3)):
        return [G]
    
    n = G.number_of_nodes()
    spasms = [[[i] for i in range(n)]]

    G.graph["p"] = [1 for i in range(n)]
    
    # Generate
    for i in range(n - 1):
        for j in range(i + 1, n):
            new_spasms = []
            for s in spasms:
                
                # edge exists
                edge = False
                for x in s[i]:
                    for y in s[j]:
                        if (x,y) in G.edges():
                            edge = True
                if not edge:
                    new = s.copy()
                    var = list(set(s[i] + s[j]))
                    s[i], s[j] = var, var
                    new_spasms.append(new)
            spasms += new_spasms       
    
    
    
    ret = []
    # remove duplicate blocks
    for s in spasms:
        keeps = []
        for i in range(len(s)):
            keep = True
            for j in range(len(s)):
                if i != j and ( set(s[i]) < set(s[j]) ):
                    keep = False
            if keep:
                keeps.append(s[i])
        new_k = []
        for elem in keeps:
            if elem not in new_k:
                new_k.append(elem)
        ret.append(new_k)

    new_k = []
    for r in ret:
        if not (sorted(r) in new_k):
            new_k.append(sorted(r))
    
    final = []
    for r in new_k:
        G_new = G.copy()
        for elem in r:
            if len(elem) > 1:
                try:
                    for e in elem[1:]:
                        G_new = nx.contracted_nodes(G_new, elem[0], e)
                    G_new.graph["p"] = [len(i) for i in r]
                except:
                    pass
        final.append(G_new)
    
    rel = []
    for f in final:
        mapping = dict(zip(f, range(f.number_of_nodes())))
        
        rel.append(nx.relabel_nodes(f, mapping))
    return rel

