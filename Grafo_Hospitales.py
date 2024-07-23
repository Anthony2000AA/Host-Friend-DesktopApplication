import networkx as nx
import math 
import matplotlib.pyplot as plt
from Dataset_Hospitales import archivo

def all_hospitales():
  
  
  
  main=archivo('CSV_Hospitales_V2.csv')
  
  #main=archivo('Prueba2CSV.csv')
  return main



def create_grafo_general():
    main = all_hospitales()
    grafo_general = nx.Graph()
    
    

    # Agregar nodos al grafo_general
    for hospital in main:
        id_hospital = hospital.id
        longitud = hospital.longitud
        latitud = hospital.latitud
        grafo_general.add_node(id_hospital, pos=(longitud, latitud))

    # Agregar aristas basadas en la distancia entre los nodos
    #for nodo1 in grafo_general.nodes:
    #    for nodo2 in grafo_general.nodes:
    #        if nodo1 != nodo2:
    #            pos_nodo1 = grafo_general.nodes[nodo1]["pos"]
    #            pos_nodo2 = grafo_general.nodes[nodo2]["pos"]
    #            distancia = haversine(pos_nodo1[1], pos_nodo1[0], pos_nodo2[1], pos_nodo2[0])
    #            distanciaenKM = int(distancia)
    #            grafo_general.add_edge(nodo1, nodo2, weight=distanciaenKM)

    return grafo_general
  

