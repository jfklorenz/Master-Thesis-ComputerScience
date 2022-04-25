# PyTest - Treewidth
# ----------------------------------------------------------------
# Imports
import sys
sys.path.append("..")

import pytest
import networkx as nx
from treewidth import *
from saveload import *
import numpy as np
import random

# ----------------------------------------------------------------
# Trees vs Non-Trees
@pytest.mark.parametrize("nodes", [i for i in range(1,6)])
def test_tree(nodes):
    gs = load_json_graphs(nodes)
    for g in gs:
        if nx.is_forest(g) & (g.number_of_edges() > 0):
            assert treewidth(g) == 1
        else:
            assert treewidth(g) != 1

# ----------------------------------------------------------------
# Networkx Fix
@pytest.mark.parametrize("nodes", [i for i in range(1,6)])
def test_networkx_all(nodes):
    gs = load_json_graphs(nodes)
    for g in gs:
        assert treewidth(g) == nx.algorithms.approximation.treewidth.treewidth_min_degree(g)[0]

# ----------------------------------------------------------------
# Networkx Random
@pytest.mark.parametrize("reps", [5])
def test_networkx_random(reps):
    for _ in range(reps):
        n = random.randrange(2,10)
        A = np.zeros((n, n), dtype=int)
        for i in range(n):
            for j in range(i+1, n):
                r = random.randint(0,1)
                A[i][j] = r 
                A[j][i] = r
            A[i][i] = 0
        g = nx.from_numpy_array(A)
        assert treewidth(g) == nx.algorithms.approximation.treewidth.treewidth_min_degree(g)[0]