import pandas as pd
import igraph as ig
import numpy as np
import sgraph as sg
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os
from scipy.linalg import expm


G = ig.Graph(directed = False)
nod = [0,1,2,3]
ar = [(0,1),(1,2),(0,2),(2,3)]

G.add_vertices(nod)
G.add_edges(ar)

L=sg.Laplacian(G)
LN = sg.NormLaplacian(G)
visual_style = {
        "vertex_size": 20,  # Tamaño de los nodos
        "bbox": (200, 200),  # Tamaño del gráfico
        "margin": 20
    }

# Mostrar el grafo
ig.plot(G, **visual_style, target='playexample.png')
print(L)
print(LN)

startsig = [20,3,10,2]
def conv(h1, h2, h3, h4,L):
    n = len(L)
    Id = np.identity(n)
    L2 = np.dot(L,L)
    L3 = np.dot(L,L)
    H = h1*Id + h2*L + h3*L2 +h4*L3
    return H

H = conv(1,-1.5,1,0.25,LN)

it = 10
f2 = np.array(startsig)
print(f2)
f2 = np.dot(H,f2)

print(f2)
f2 = np.array(startsig)
print(f2)

E2 = expm(-5*LN)

print(E2)
f2 = np.dot(E2,f2)
print(f2)