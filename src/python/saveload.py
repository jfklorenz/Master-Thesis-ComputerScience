# SAVE / LOAD - JSON
""" 
Functions:
- load_json_graph
- load_json_graphs
- save_json_graph
- save_json_graphs
- update_graph (graph -> update -> save)
- update_json_graph (load -> update -> save) TODO

"""

# ----------------------------------------------------------------
# Imports
import json
import networkx as nx
from globals import PATH
from tqdm import tqdm
from logger import createLogger
import logging

import os
os.chdir(PATH)

log_save = createLogger('Save / Load')
log_save.setLevel(logging.INFO)

# ----------------------------------------------------------------
# Save a graph to json
def save_json_graph(graph, filename):
    g_json = nx.node_link_data(graph)    
    json.dump(g_json,open(filename,'w+'),indent=2)
    
    _, file = filename.split('_')
    file, _ = file.split('.')
    
    log_save.info('Graph' + file + ' saved successfully!')
    return 

# ----------------------------------------------------------------
# Save a list of graphs to json
def save_json_graphs(graphs):
    print('Saving', len(graphs), 'graphs:') 
    for i in tqdm(range(len(graphs))):
        graph = graphs[i]
        file = str(graph.number_of_nodes()) + '_' + str(i)
        filename = 'json/' + str(graph.number_of_nodes()) + '/' + file + '.json'
        graph.graph['file'] = file
        g_json = nx.node_link_data(graph)    
        json.dump(g_json,open(filename,'w+'),indent=2)
    
    
    print('------------------------------')
    print('All graphs saved successfully!')
    print('')
    return

# ----------------------------------------------------------------
# Load a graph from json
def load_json_graph(file, folder):
    filename = 'json/' + str(folder) + '/' + str(folder) + '_' + str(file) + '.json'
    with open(filename) as f:
        js_graph = json.load(f)
    
    log_save.info('File ' + filename + ' loaded successfully!')
    return nx.node_link_graph(js_graph)

# ----------------------------------------------------------------
# Load a folder of graphs from json
def load_json_graphs(folder):
    print('Loading all graphs from folder', folder)
    print('------------------------------')
    graphs = []
    dir = 'json/' + str(folder)
    for i in tqdm(range(len(os.listdir(dir)))):
        filename = 'json/' + str(folder) + '/' + str(folder) + '_' + str(i) + '.json'
        with open(filename) as f:
            js_graph = json.load(f)
        g = nx.node_link_graph(js_graph)
        graphs.append(g)
    
    print('------------------------------')
    print('All files loaded successfully!')
    print('')
    return graphs

# ----------------------------------------------------------------
# Update graph
def update_graph(graph, attribute, value):
    
    dir = 'json/' + str(graph.number_of_nodes())
    
    graph.graph[attribute] = value
    
    file = graph.graph['file']
    filename = 'json/' + str(graph.number_of_nodes()) + '/' + file + '.json'
    
    g_json = nx.node_link_data(graph)    
    json.dump(g_json,open(filename,'w+'),indent=2)
    
    log_save.info('File', filename, 'updated successfully!')
    return

# ----------------------------------------------------------------
# Test

# ----------------------------------------------------------------