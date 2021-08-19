# minimum elimination ordering width
# https://codegolf.stackexchange.com/questions/129417/calculate-treewidth

import itertools
def elimination_width(graph):
    max_neighbors = 0
    for i in sorted(set(itertools.chain.from_iterable(graph))):
        neighbors = set([a for (a, b) in graph if b == i] + [b for (a, b) in graph if a == i])
        max_neighbors = max(len(neighbors), max_neighbors)
        graph = [edge for edge in graph if i not in edge] + [(a, b) for a in neighbors for b in neighbors if a < b]
    return max_neighbors

def treewidth(graph):
    vertices = list(set(itertools.chain.from_iterable(graph)))
    min_width = len(vertices)
    for permutation in itertools.permutations(vertices):
        new_graph = [(permutation[vertices.index(a)], permutation[vertices.index(b)]) for (a, b) in graph]
        min_width = min(elimination_width(new_graph), min_width)
    return min_width

if __name__ == '__main__':
    graph = [('a', 'b'), ('a', 'c'), ('b', 'c'), ('b', 'e'), ('b', 'f'), ('b', 'g'),
            ('c', 'd'), ('c', 'e'), ('d', 'e'), ('e', 'g'), ('e', 'h'), ('f', 'g'), ('g', 'h')]
    print(treewidth(graph))
