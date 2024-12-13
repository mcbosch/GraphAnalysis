#-----------------------------------------------------------------------
#
#             paquete sgraph.py para análisis de grafos
#
#   Este archivo .py es un conjunto de funciones que se apoya en el 
#   paquete igraph de python para un análisis de grafos. Lo enfocaremos
#   a la clasificación de grafos a partir de una base de datos in-out
#
#------------------------------------------------------------------------

import igraph as ig
import numpy as np
import pandas as pd

#   esta clase es para la lectura de archivos y guardar grafos
class arxiv:

    example_format = pd.DataFrame({
        'source': ['node1', 'node3', 'node5', 'node7'],
        'destination': ['node4', 'node2', 'node6', 'node1']
    })

    def readsgraph(filename, directed = False):
        try:
            data = pd.read_csv(filename, delimiter=";", usecols=["source", "destination"]) 

            N = len(data)
            nodes = list(set(data['source'].astype(str)).union(set(data['destination'].astype(str))))
            aristas = [(data.iloc[i,0].encode().decode(), data.iloc[i,1].encode().decode()) for i in range(N)]

            g = ig.Graph(directed = directed)
            g.add_vertices(nodes)
            g.add_edges(aristas)
            return g
        except:
            try:
                data = pd.read_csv(filename, delimiter=";", usecols=["source", "destination"]) 

                N = len(data)
                nodes = list(set(data['source'].astype(str)).union(set(data['destination'].astype(str))))
                aristas = [(data.iloc[i,0].astype(str).encode().decode(), data.iloc[i,1].astype(str).encode().decode()) for i in range(N)]

                g = ig.Graph(directed = directed)
                g.add_vertices(nodes)
                g.add_edges(aristas)
                return g
            except:
                print("ERROR: can't read the document")
                print(f'Your document should be a .csv with this format:\n{arxiv.example_format}')
                print(f"With this format we don't consider isolated vertices")

    def save(G, path):
        pass             
        

# This function consider the Laplacian of a graph
def Laplacian(G):
    A = G.get_adjacency()
    D = np.diag([sum(A[i]) for i in range(len(A))])
    return D - A

def NormLaplacian(G):
    L = Laplacian(G)
    A = G.get_adjacency()
    inv = lambda x: 1/x
    D = list(map(np.sqrt,[sum(A[i]) for i in range(len(A))]))
    D1 = list(map(inv,D))
    D1 = np.diag(D1)
    L = np.dot(D1,L)
    L = np.dot(L,D1)
    return L

# The following equation calculates the matrix of the heat diffussion in t
def HeatEq(M, t): 
    tol = 10^(-8)
    finish = False
    n = len(M)
    E = np.identity(n)+t*M
    A = M
    i = 1
    fact = i
    
    while not finish:
        i += 1
        fact = fact*i
        t = t*t
        A = np.dot(A,M)
        e =  (t/fact)*np.max(abs(A))
        if e<tol:
            return E
        else:
            E = E + (t/fact)*A  
        
        if i > 10: 
            finish = True
            print('Too much iterations')
            return E
