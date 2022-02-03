import itertools
import networkx as nx

def elimination_width(graph_edges):
    max_neighbors = 0
    for i in sorted(set(itertools.chain.from_iterable(graph_edges))):
        neighbors = set([a for (a, b) in graph_edges if b == i] + [b for (a, b) in graph_edges if a == i])
        max_neighbors = max(len(neighbors), max_neighbors)
        graph_edges = [edge for edge in graph_edges if i not in edge] + [(a, b) for a in neighbors for b in neighbors if a < b]
    return max_neighbors

def treewidth(graph):
    # Check if input is a Networkx graph
    if isinstance(graph, nx.Graph):
        graph_edges = [e for e in graph.edges]
    else:
        graph_edges = graph
    
    vertices = list(set(itertools.chain.from_iterable(graph_edges)))
    min_width = len(vertices)
    for permutation in itertools.permutations(vertices):
        new_graph = [(permutation[vertices.index(a)], permutation[vertices.index(b)]) for (a, b) in graph_edges]
        min_width = min(elimination_width(new_graph), min_width)
    return min_width

def graph_edges(graph):
    return [e for e in graph.edges]