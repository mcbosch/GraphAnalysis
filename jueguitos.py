import pandas as pd
import igraph as ig
import numpy as np
import sgraph as sg
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from scipy.linalg import expm


filename = "./graphdata_hsa/data/individuals/hsa/hsa_R_adj.csv" 
g = sg.arxiv.readsgraph(filename)
L = sg.NormLaplacian(g)
print(np.linalg.det(L))
# Vamos a suavizar una senyal

N = g.vcount()
intensity = np.linspace(0,1,100)
f = np.random.rand(N)

# Normalizar las intensidades a un rango de colores de azul a rojo
cmap = mcolors.LinearSegmentedColormap.from_list("blue_red", ["blue", "red"])
norm = mcolors.Normalize(vmin=0, vmax=1)  # Normalizamos las intensidades de 0 a 1

# Asignar un color a cada nodo basado en su intensidad
colores = [(1,0,0,i) for i in f]

# Asignar colores a los nodos
g.vs["color"] = colores

visual_style = {
    "vertex_color": g.vs["color"],  # Usamos el atributo de color para los nodos
    "vertex_size": 20,  # Tamaño de los nodos
    "bbox": (600, 600),  # Tamaño del gráfico
    "margin": 20
}



# Mostrar el grafo
ig.plot(g, **visual_style, target='coloredgraph.png')
it = 10
f2 = np.array(f)

E = expm(-4*L)

f2 = np.dot(E,f2)

    # Aplicamos el laplaciano a la senyal
    
suavizado = f2.tolist()

colores = [(1,0,0,i) for i in suavizado]
g.vs['color'] = colores
visual_style = {
        "vertex_color": g.vs["color"],  # Usamos el atributo de color para los nodos
        "vertex_size": 20,  # Tamaño de los nodos
        "bbox": (600, 600),  # Tamaño del gráfico
        "margin": 20
    }

# Mostrar el grafo
ig.plot(g, **visual_style, target='coloredgraphs.png')

