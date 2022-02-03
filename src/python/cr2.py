# COLOR REFINEMENT
# ----------------------------------------------------------------
# Imports
from collections import Counter
from globals import COLORS
import networkx as nx
from multiset import *
from saveload import *
from plot import *

from logger import createLogger
log_cr = createLogger('Color-Refinement')
log_cr.setLevel(logging.DEBUG)

# ----------------------------------------------------------------
# Ideas
# - Multisets
#   - vs List

# ----------------------------------------------------------------
# Color-Refinement Algorithm
def color_refinement(graph):
    
    log_cr.info('START')
        
    # Check if input is a Networkx graph
    if not isinstance(graph, nx.Graph):
        log_cr.error('Input not a valid Networkx graph.')
        return
    # ----------------------------------------------------------------
    log_cr.info('Parameter')
    
    # Constants
    n = graph.number_of_nodes()

    # Variables
    iterations = 0
    C = []
    Cn = [1 for _ in range(n)]
    d = []
    dn = list_equal_elements(Cn)
   
    log_cr.debug('Number of Nodes: ' + str(n))
    log_cr.debug('Initial Coloring: ' + str(Cn)) 
    
    # ----------------------------------------------------------------
    # Loop    

    while d != dn:
        C = Cn.copy()
        d = dn.copy()
        
        for v in graph.nodes():
            c = []
            for w in graph.neighbors(v):
                c.append(C[w])
            Cn[v] = c
        
        dn = list_equal_elements(Cn)
        iterations += 1
    
    log_cr.debug('Iterations: ' + str(iterations - 1))
    log_cr.debug('Final Coloring: ' + str(Cn))
    log_cr.info('END')
    
    
    return Cn #coloring

def list_equal_elements(lst): 
    d = []
    for l in lst:
        d.append([i for i, e in enumerate(lst) if e == l])
    return d


#ac = list_equal_elements(a)
#bc = list_equal_elements(b)
#print(ac, bc)

g = load_json_graph(22,5)
c = color_refinement(g)
#print(c)
#plot_graph(g)

#gs = load_json_graphs(7)
