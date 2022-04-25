# PyTest - Spasm
# ----------------------------------------------------------------
# Imports
import sys
sys.path.append("..")

import pytest
from spasm import *
from globals import *
import networkx as nx

# --------------------------------
# Complete Graphs
@pytest.mark.parametrize("n", range(2, 10))
def test_spasm_complete(n):
    g = nx.complete_graph(n)
    S = spasm(g)
    assert len(S) == 1
    assert nx.is_isomorphic(g, S[0])
        

# --------------------------------
# Path - 5
def test_spasm_P5():
    S = spasm(nx.path_graph(5))
    assert len(S) == 15
    G = [P2, P3, P4, K3, K3s, S4, C4, P5]
    for g in G:
        iso = False
        for s in S:
            if nx.is_isomorphic(s, g):
                iso = True
        assert iso == True
        
# --------------------------------
# K5s
def test_spasm_K5s():
    g = K5s
    S = spasm(g)
    assert len(S) == 5 # 4 merges & K5s
    for s in S:
        assert nx.is_isomorphic(s, K5) or nx.is_isomorphic(s, g)
    