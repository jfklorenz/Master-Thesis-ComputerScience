# Source Code





---

## NetworkX

### Snippets

Graphs:
- Graph, DiGraph, MultiGraph
- subgraph(G, H) induced subgraph by G in H
- complete_graph(n)
- G = nx.Graph(attribite = 'name') / G.graph['attribute']='name'

Draw:
- import matplotlib.pyplot as plt
- ax1 = plt.subplot(r, c, p) - rows, columns, position
- sharex = ax1
- nx.draw(G, with_labels=True, font_weight='bold')
- plt.show()
- options = {
    'node_color': 'black',
    'node_size': 100,
    'width': 3,
}
- pos = nx.layout(G), bipartite_layout, circular_layout, planar_layout, random_layout, spring_layout, spiral_layout
- draw(G, pos=pos, with_labels=True, node_size, node_color, node_shape, font_size/color/weight/family, label), draw_random, draw_circular, draw_spectral, draw_shell
- plt.savefig("path.png")
- complete_graph, cycle_graph, path_graph, star_graph
- node_color = color_map, color_map = ['red' if node == user_id else 'green' for node in G]
- A = nx.adjacency_matrix(G).todense()
- A = nx.from_numpy_array(A, create_using = nx.MultiGraph)

