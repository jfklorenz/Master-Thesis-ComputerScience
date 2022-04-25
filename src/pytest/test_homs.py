# PyTest - Hom / Emb / Surj / Iso / Sub / matrices
# ----------------------------------------------------------------
# Imports
import sys
sys.path.append("..")

import pytest
from homs import *
from spasm import *
from globals import *
import networkx as nx
import math
import random

# ----------------------------------------------------------------
# Tests - Complete
@pytest.mark.parametrize("n", range(2, 7))
def test_complete(n):
    Kn = nx.complete_graph(n)
    assert Hom(Kn, Kn) == math.factorial(n)
    assert Emb(Kn, Kn) == math.factorial(n)
    assert Surj(Kn, Kn) == math.factorial(n)
    
# ----------------------------------------------------------------
# Tests - Paths
def test_paths_22():
    assert Hom(P2, P2) == 2
    assert Emb(P2, P2) == 2
    assert Surj(P2, P2) == 2
# ----------------    
def test_paths_23():
    assert Hom(P2,P3) == 4
    assert Emb(P2, P3, ) == 4
    assert Surj(P2, P3) == 0
# ----------------
def test_paths_24():
    assert Hom(P2,P4) == 6
    assert Emb(P2, P4, ) == 6
    assert Surj(P2, P4) == 0
# ----------------
def test_paths_32():
    assert Hom(P3,P2) == 2
    assert Emb(P3, P2, ) == 0
    assert Surj(P3, P2) == 2
# ----------------
def test_paths_33():
    assert Hom(P3,P3) == 6
    assert Emb(P3, P3, ) == 2
    assert Surj(P3, P3) == 2
# ----------------
def test_paths_34():
    assert Hom(P3,P4) == 10
    assert Emb(P3, P4, ) == 4
    assert Surj(P3, P4) == 0
# ----------------
def test_paths_42():
    assert Hom(P4,P2) == 2
    assert Emb(P4, P2, ) == 0
    assert Surj(P4, P2) == 2
# ----------------
def test_paths_43():
    assert Hom(P4,P3) == 8
    assert Emb(P4, P3, ) == 0
    assert Surj(P4, P3) == 4
# ----------------
def test_paths_44():
    assert Hom(P4,P4) == 16
    assert Emb(P4, P4, ) == 2
    assert Surj(P4, P4) == 2

# ----------------------------------------------------------------
# Hom = sum_spasm Emb
def test_spasm_hom_emb():
    G =  [P2, P3, P4, K3, K3s, S4, C4, P5, K5]
    
    for i in G:
        for j in G:
            S = spasm(i)
            L = Hom(i, j)
            R = 0
            for s in S:
                R += Emb(s, j)
            assert L == R
            
# ----------------------------------------------------------------
# Dell - Homomorphisms are a good basis
def test_example_manual_1():
    Ks = [P5, K5, K5s, K6, K7]
    for K in Ks:
        L = Hom(P5, K)
        R = Emb(P5, K) + Emb(C4, K)
        R += Emb(S4, K) + 2*Emb(K3s, K)
        R += 2*Emb(P4, K) + 3*Emb(K3, K)
        R += 4*Emb(P3, K) + Emb(P2, K)
        assert L == R

# -------------------------------- 
def test_example_manual_2():
    Ks = [P5, K5, K5s, K6, K7]
    for K in Ks:
        L = Sub(P5, K)
        R = [0.5 * Hom(P5, K)]
        R.append(- 0.5* Hom(C4, K))
        R.append(- 0.5* Hom(S4, K))
        R.append(- Hom(K3s, K))
        R.append(-Hom(P4, K)) 
        R.append(3/2*Hom(K3, K))
        R.append(5/2*Hom(P3, K))
        R.append(- Hom(P2, K))
        
        R = sum(R)
        assert L == R
        
# -------------------------------- 
def test_example_1():
    H = P5
    Gs = [K5, K5s, K6, K7]

    for G in Gs:

        L = Sub(H, G) * Iso(H, H)
        S = spasm(H)
        R = 0
        
        # sum over all partitions p
        for s in S:
            n = H.number_of_nodes()
            m = s.number_of_nodes()
            
            val_1 = (-1)**(n - m)
            
            # prod over all Blocks B in p
            val_2 = 1

            for i in s.graph["p"]:
                val_2 *= math.factorial( abs(i) - 1)

            
            # Hom( H/p -> G)
            val_3 = Hom(s, G)

            R += (val_1 * val_2 * val_3)
        assert L == R
            
# -------------------------------- 
def test_example_2():
    # (13) Surj(H->F) = Aut(F) * sum_p [A] [ H/p iso F]
    H = P5
    Fs = [K3, P4, K4, P5, K5, K5s, K6, K7]

    for F in Fs:
        
        S = spasm(H)
        
        L = Surj(H, F)
        
        r1 = Iso(F, F)
        
        r2 = 0
        for s in S:
            if nx.is_isomorphic(s, F):
                r2 += 1
        R = r1 * r2
        assert L == R
        
# --------------------------------        
def test_matrices():
    GS = [P2, P3, K3, P4, K4]
    
    Homs = matrices(GS, Hom)
    Surjs = matrices(GS, Surj)
    Subs = matrices(GS, Sub)
    
    SurjSub = np.matmul(Surjs,Subs)
    
    for i in range(len(Homs)):
        for j in range(len(Homs[i])):
            assert Homs[i][j] == SurjSub[i][j]
    
# --------------------------------
def test_iso_random():
    for _ in range(25):
        g1 = nx.graph_atlas(random.randint(1, 100))
        g2 = nx.graph_atlas(random.randint(1, 100))
        
        assert Iso(g1, g2) == nx.is_isomorphic(g1, g2)
