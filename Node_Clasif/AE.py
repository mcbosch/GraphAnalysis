import torch
from torch_geometric.datasets import Planetoid

dataset = Planetoid(root='/tmp/Cora', name='Cora')

print('==========================================')
print('         Exploration Analysis             ')
print('')
print(f'Number of Graphs: {len(dataset)}')
print(f'Number of features: {dataset.num_features}')
print(f'Number of classes: {dataset.num_classes}')

print('_____________________')
print('Analysis of the graph')

G = dataset[0]
print(f'    > Graph nº of nodes: {G.num_nodes}')
print(f'    > Graph nº of edges: {G.num_edges}')
print(f'    > Averege node degree: {G.num_edges/G.num_nodes:.2f}')

# As we have only 1 graph we take it so we can analyze it