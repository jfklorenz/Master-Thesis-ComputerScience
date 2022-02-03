# PLOT GRAPHS
# ----------------------------------------------------------------
# Imports
import matplotlib.pyplot as plt 
import networkx as nx
from globals import *
import os
os.chdir(PATH)

# ----------------------------------------------------------------
# Plot graph
def plot_graph(graph):
    nx.draw_circular(graph, with_labels=False, node_size=[800 for _ in graph.nodes()])     
    plt.show() 
    return

# ----------------------------------------------------------------
# Plot all graphs from a list of graphs
def plot_graphs(graphs):
    columns = min( len( graphs), 7 ) 
    rows = (len( graphs ) + columns - 1) // columns 
    
    for i, g in enumerate( graphs ): 
        ax = plt.subplot( rows, columns, i+1 ) 
        ax.axis( 'off' ) 
        #pos = nx.drawing.layout.circular_layout( g ) 
        #nx.drawing.nx_pylab.draw_networkx( g, node_size=30, with_labels=False, pos=pos )
        cm = []
        cr = g.graph['color-refinement']

        for c in range(len(g)):
            cm.append(COLORS[cr[c]])
        nx.draw(g, node_color=cm, with_labels=True)     
    plt.show() 
    return

# ----------------------------------------------------------------
def plot_color(graph, coloring = False, save = False, show=True, layout='circular', out='test'):
    if not coloring:
        coloring = graph.graph['color-refinement']
    
    cm = []
    for i in range(len(coloring)):

        cm.append(COLORS[coloring[i] - 1])
    
    plt.figure()
    try:
        name = graph.graph['file']
        tw = graph.graph['treewidth']
        plt.title('Graph: ' + name + '   Treewidth: ' + str(tw), fontsize=22)
    except:
        print("No file")
    #pos = nx.circular_layout(graph)
    if layout == 'spring':
        pos = nx.spring_layout(graph)
    elif layout == 'circular':
        pos = nx.circular_layout(graph)
    nx.draw(graph, pos=pos, node_color=cm, with_labels=True, node_size=800, font_size=22, font_color="whitesmoke")

    
    if save:
        try:
            plt.savefig('img/' + str(graph.number_of_nodes()) + '/' + name + '.png')
        except:
            plt.savefig('img/' + out + '.png')
    if show:
        plt.show()
    
    return

# ----------------------------------------------------------------
# Fix Grid
def plot_fix(graphs, save = False, show=True):
    """ 40 Fields """
    columns = min( len( graphs), 6 ) 
    rows = (len( graphs ) + columns - 1) // columns 
    
    for i, g in enumerate( graphs ): 
        ax = plt.subplot( rows, columns, i+1 ) 
        ax.axis( 'off' ) 
        #pos = nx.drawing.layout.circular_layout( g ) 
        #nx.drawing.nx_pylab.draw_networkx( g, node_size=30, with_labels=False, pos=pos )
        cm = []
        cr = g.graph['color-refinement']
        if max(cr) > 6:
            print(g.graph['file'])
        for c in range(len(cr)):
            cm.append(COLORS[cr[c] - 1])
        
        pos = nx.circular_layout(g)
        
        name = g.graph['file']
        #plt.figure()
        #plt.title('Graph: ' + name, fontsize=22)
        nx.draw(g, pos=pos, with_labels=True, node_color=cm, node_size=50, font_size=8,font_color="whitesmoke")     
    plt.tight_layout()
    #plt.subplots_adjust(left=0.2, bottom=0.2, right=0.8, top=0.8, wspace=0.4, hspace=0.4)
    
    if save:
        plt.savefig('img/' + save + '.png')
    if show:
        plt.show() 
    
    
    return
# ----------------------------------------------------------------
# Test


# ----------------------------------------------------------------