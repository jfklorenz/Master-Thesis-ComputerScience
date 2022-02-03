# COLOR REFINEMENT
# ----------------------------------------------------------------
# Imports
import networkx as nx
import numpy as np
from collections import Counter
from globals import COLORS
# ----------------------------------------------------------------

def colorrefinement(G):
    
    n = G.number_of_nodes()
    
    C = []
    Cn = [1 for _ in range(n)]
    cnt_cols = 1
    while C != Cn:
        C = Cn.copy()
        M = []
        
        for v in G.nodes():
            m = []
            for w in G.neighbors(v):
                m.append(C[w])
            M.append((C[v], m, v))

        #print("M:", M)
        
        cnt_cols_up = 0
        for c in range(1, cnt_cols + 1):
            Mi = list(filter(lambda m: m[0] == c, M))
            
            Mn = [mi[1] for mi in Mi]
            for m in Mn:
                m.sort()
            
            #print("Mn:", Mn)
            
            cnt_map = Counter(tuple(item) for item in Mn).most_common()
            
            #print('map', cnt_map)
            
            if len(cnt_map) > 1:
                for i in range(1, len(cnt_map)):
                    vs = [mi[2] for mi in M if mi[1] == list(cnt_map[i][0])]
                    cnt_cols_up += 1
                    for v in vs:
                        Cn[v] = cnt_cols + cnt_cols_up
                    
        cnt_cols += cnt_cols_up
        
        #print(Cn)
        
    return C
"""
gs = []
g = load_json_graph(29, 5)
c = colorrefinement(g)
print(c)
plot_color(g, c)

"""

