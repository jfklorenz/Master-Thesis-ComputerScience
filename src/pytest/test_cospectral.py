# PyTest - Cospectral
# ----------------------------------------------------------------
# Imports
import sys
sys.path.append("..")

import pytest
from cospectral import *
from globals import *
import networkx as nx
import random

# ----------------------------------------------------------------
# Manual Input
def test_manual():
    A = [
        [0,0,1,0,1],
        [0,0,0,0,0],
        [1,0,0,1,0],
        [0,0,1,0,1],
        [1,0,0,1,0]
    ]

    B = [
        [0,1,0,0,0],
        [1,0,1,1,1],
        [0,1,0,0,0],
        [0,1,0,0,0],
        [0,1,0,0,0]
    ]
    assert areCospectral(A, B) == True

# ----------------------------------------------------------------
# Random graph from Atlas
def test_random():
    for _ in range(100):
        g1 = nx.graph_atlas(random.randint(25, 100))
        g2 = nx.spectral_graph_forge(g1, 1)
        assert areCospectral(g1, g2) == True