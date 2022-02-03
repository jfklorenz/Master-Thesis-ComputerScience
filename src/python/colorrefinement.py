# COLOR REFINEMENT
# ----------------------------------------------------------------
# Imports
from collections import Counter
from globals import COLORS

# ----------------------------------------------------------------
# The k-dimensional Weisfeiler-Leman Algorithm (2019)
def colorrefinement(G):
    
    con = True
    for n in G.nodes():
        if G.degree[n] == 0:
            con = False
            break
    
    n = G.number_of_nodes()
    """
    
    if con:
        C = [1 for _ in range(n)] # coloring
        cnt_cols = 1
        L = [1]
    else:
        C = [1 if G.degree[i] == 0 else 2 for i in G.nodes()]
    
        cnt_cols = 2 # save all colorings
        L = [1,2]
    
    """
    C = [1 for _ in range(n)]
    cnt_cols = 1
    L = [1]
   
    M = []

    while L != []:
    #for _ in range(1):

        # for each color class l in L
        for c in L:
            #print(L)
            L.remove(c)
            
            # for each vertex w with C[w] == c
            for w in G.nodes():
                
                if C[w] == c:
                    # for each neighbour v of w
                    for v in G.neighbors(w):
                        M.append((v, c))
                
        M.sort()
        
        M2 = []
        cur = M[0][0]
        m = []
        
        for i in range(len(M)):
            if M[i][0] == cur:
                m.append(M[i][1])
            else:
                cur = M[i][0]
                m = [C[M[i-1][0]]] + [m] + [M[i-1][0]]
                M2.append(m)
                m = [M[i][1]]

        if not (M == []):
            M2.append([C[M[i][0]]] + [m] + [M[i][0]])
    
        """
        for v in G.nodes():
            fil = [m for m in M2 if m[2] == v]
            print(fil)
            if fil == []:
                M2.append([C[v], [], v])
        print('m2',M2)
        print("------")
        """
        
        cnt_cols_up = 0
        for c in range(1, cnt_cols + 1):
            Mi = list(filter(lambda m: m[0] == c, M2))
            
            Mn = [mi[1] for mi in Mi]
            cnt_map = Counter(tuple(item) for item in Mn).most_common()

            if len(cnt_map) > 1:
                for i in range(1, len(cnt_map)):
                    vs = [mi[2] for mi in M2 if mi[1] == list(cnt_map[i][0])]
                    for v in vs:
                        C[v] = cnt_cols + i
                    
                    cnt_cols_up += 1
                    
                    
        # Update
        cnt_cols += cnt_cols_up
        if cnt_cols_up > 0:
            for i in range(cnt_cols - cnt_cols_up + 1, cnt_cols + 1):
                L.append(i)
                
        print('M:', M)
        print('M2:', M2)
        print('C:', C)
        print("----------")
        M = []
    #print("")
    
    Cn = [1 for _ in range(len(C))]
    con = True
    for v in G.nodes():
        if G.degree[v] == 0:
            con = False
        else:
            Cn[v] = C[v] + 1

    if con:
        return C
    else:
        return Cn

# ----------------------------------------------------------------
# Save color to graph
def color_graph(graph, coloring):
    if not coloring:
        try:
            coloring = graph.graph['color']
        except:
            print('No coloring available!')
    return graph

# ----------------------------------------------------------------
# Test

