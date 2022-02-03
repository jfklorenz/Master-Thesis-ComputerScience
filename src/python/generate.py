# GENERATE ALL GRAPHS
# ----------------------------------------------------------------
# Imports
import matplotlib.pyplot as plt 
import networkx as nx 
import itertools
from globals import NONISO

# ----------------------------------------------------------------
# Generate all graphs with n nodes
def gen_graphs(n = 3):
    
    print('Generating all graphs with', n, 'nodes:')
    print('------------------------------')
    
    graphs = [] 
    all_nodes = list( range( 0, n ) ) 
    all_edges = list( itertools.combinations( all_nodes, r=2 ) )
    cnt = 0
    cnt_max = NONISO[n]
    
    for num_edges in range( 0, n*(n-1)//2 + 1): 
        new_graphs = [] 
        for edge_set in itertools.combinations( all_edges, r=num_edges ): 
            g = nx.Graph() 
            g.add_nodes_from( all_nodes ) 
            g.add_edges_from( edge_set ) 
            found = False 
            for existing in new_graphs: 
                if nx.is_isomorphic( g, existing ): 
                    found = True
                    break 
            if not found:
                cnt += 1
                print('Graph', cnt, '/', cnt_max)
                new_graphs.append( g ) 
        graphs.extend( new_graphs )
    
    print('------------------------------')
    print('All graphs generated successfully!')
    print('')
    
    return graphs

# ----------------------------------------------------------------
# Test
