import igraph as ig
import pandas as pd

# Cargar los datos desde el archivo CSV
filename = "./graphdata_hsa/data/individuals/hsa/hsa_mDAG.graphml" 
hsa1 = ig.Graph._construct_graph_from_graphmlz_file(filename)

ig.plot(hsa1, target='./images/hsa1.png')


