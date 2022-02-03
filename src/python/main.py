# Test

from turtle import color
from tw import *
from globals import *
from cr import *
from saveload import *
from plot import *
from generate import *
import json
import os
os.chdir(PATH)


"""
# Compare all color refinement results
for i in range(1,8):
    dic = {}
    gs = load_json_graphs(i)
    
    for g in gs:
        col = g.graph['color-refinement']
        col.sort()
        col = repr(col)
        
        file = g.graph['file']
        
        if not (col in dic):
            dic[col] = [file]
        else:
            dic[col].append(file)
    
    with open('json/cr_' + str(i) + '.json', 'w+', encoding='utf-8') as f:
        json.dump(dic, f, ensure_ascii=False, indent=4)
"""

"""
# Update CR [1-7]
for i in range(1,8):
    gs = load_json_graphs(i)
    for g in gs:
        c = colorrefinement(g)
        update_graph(g, 'color-refinement', c)
"""

"""
# Save single plots [1-6]
for i in range(1,7):
    gs = load_json_graphs(i)
    for g in gs:
        plot_color(g, save = True, show=False)
"""


"""
# Fixed Pictures
for n in range(1,6):

    gs = load_json_graphs(n)
    plot_fix(gs, save=str(n), show=False)
"""

"""
# Example
A1 = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 1],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0]
]

A2 = [
    [0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 0], 
    [0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 0]
]

G1 = nx.from_numpy_array(np.array(A1))
G2 = nx.from_numpy_array(np.array(A2))

c1 = colorrefinement(G1)
c2 = colorrefinement(G2)

print(c1, c2)

plot_color(G1, c1, layout='spring', save=True, out='test1')
plot_color(G2, c2, layout='spring', save=True, out='test2')

"""

gs = load_json_graphs(3)

for g in gs:
    plot_graph(g)
    print("tw:",treewidth(graph_edges(g)))
    print(nx.is_forest(g) & (g.number_of_edges() > 0))
    print("edges:",g.number_of_edges())
    print("=====")