# EXAMPLE GRAPHS
# ----------------------------------------------------------------
# Imports
import networkx as nx
import numpy as np
from plot import plot_graph
from saveload import *
from cr2 import color_refinement
import random
# ----------------------------------------------------------------
# Example Graphs
"""
R2_1 = [
    [0,1,1,0,0,0],
    [1,0,1,0,0,0],
    [1,1,0,0,0,0],
    [0,0,0,0,1,1],
    [0,0,0,1,0,1],
    [0,0,0,1,1,0],
]

R2_2 = [
    [0,1,0,0,0,1],
    [1,0,1,0,0,0],
    [0,1,0,1,0,0],
    [0,0,1,0,1,0],
    [0,0,0,1,0,1],
    [1,0,0,0,1,0],
]

R3 = [
    [0,1,0,1,0,0],
    [1,0,1,0,1,0],
    [0,1,0,0,0,1],
    [1,0,0,0,1,0],
    [0,1,0,1,0,1],
    [0,0,1,0,1,0],
]

R4 = [
    [0,1,1,0,0,0],
    [1,0,1,0,0,0],
    [1,1,0,1,0,0],
    [0,0,1,0,1,1],
    [0,0,0,1,0,1],
    [0,0,0,1,1,0],
]

G1 = nx.from_numpy_array(np.array(R2_1))
G2 = nx.from_numpy_array(np.array(R2_2))

G5 = nx.from_numpy_array(np.array(R3))
G6 = nx.from_numpy_array(np.array(R4))

#plot_graph(G1)
#plot_graph(G2)

c1 = color_refinement(G1)
c2 = color_refinement(G2)

print(c1 == c2)

G3 = load_json_graph(74,6)
G4 = load_json_graph(76,6)
c3 = color_refinement(G5)
c4 = color_refinement(G6)

b = nx.adjacency_matrix(G3).todense()
print(b)
plot_graph(G3)
plot_graph(G5)
print(c3.sort() == c4.sort())
"""
# ----------------------------------------------------------------
# Test


n = random.randrange(2,20)
A = np.zeros((n, n), dtype=int)
for i in range(n):
    for j in range(i+1, n):
        r = random.randint(0,1)
        A[i][j] = r 
        A[j][i] = r
    A[i][i] = 0
print(A)
g = nx.from_numpy_array(A)





# ----------------------------------------------------------------