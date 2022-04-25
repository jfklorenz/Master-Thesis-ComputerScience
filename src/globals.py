# GLOBAL VARIABLES
# ----------------------------------------------------------------
# Imports
import networkx as nx

# ----------------------------------------------------------------
# Path to directory (save/load)
PATH = 'C:/Users/jfklo/Git/Master-Thesis-ComputerScience/src/'

# ----------------------------------------------------------------
# Graphs
## Paths
P2 = nx.path_graph(2)
P3 = nx.path_graph(3)
P4 = nx.path_graph(4)
P5 = nx.path_graph(5)
## Complete
K2 = nx.complete_graph(2)
K3 = nx.complete_graph(3)
K4 = nx.complete_graph(4)
K5 = nx.complete_graph(5)
K6 = nx.complete_graph(6)
K7 = nx.complete_graph(7)
## Cycles
C4 = nx.cycle_graph(4)
## Stars
S3 = nx.star_graph(2)
S4 = nx.star_graph(3)
## Other
K3s = nx.complete_graph(3)
K3s.add_edge(0,3)
K4s = nx.complete_graph(4)
K4s.add_edge(0,4)
K5s = nx.complete_graph(5)
K5s.add_edge(0,5)

# ----------------------------------------------------------------
# Colors for Color-Refinement
COLORS = [
    'red', 'blue', 'green', 'gold', 'purple', 'navy', 'black'
]

# ----------------------------------------------------------------
# Number of non-isomorphic graphs with n nodes
NONISO = {
    0: 1,
    1: 1,
    2: 2,
    3: 4,
    4: 11,
    5: 34,
    6: 156,
    7: 1044,
    8: 12346,
    9: 274668
}
# ----------------------------------------------------------------
