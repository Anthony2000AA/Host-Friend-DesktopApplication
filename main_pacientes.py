from Grafo_Pacientes import create_grafo_general
from Grafo_Pacientes import all_pacientes
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt






pacientes = all_pacientes()#global
# Función para realizar la búsqueda BFS en el grafo
def BFS(grafo, inicio, sintoma_busqueda1, sintoma_busqueda2):
    visitados = set()
    queue = deque()
    queue.append(inicio)  # Almacenar el nodo y su nodo padre en la cola
    while queue:
        paciente = queue.popleft()
        if paciente not in visitados:
            visitados.add(paciente)
            sintoma1 = pacientes[paciente-1].sintoma1
            sintoma2 = pacientes[paciente-1].sintoma2
            if sintoma1 == sintoma_busqueda1 or sintoma1 == sintoma_busqueda2 or sintoma2 == sintoma_busqueda1 or sintoma2 == sintoma_busqueda2:
                return paciente

            vecinos = list(grafo.neighbors(paciente))
            queue.extend(vecinos)
            # for vecino in vecinos:
            #    if vecino != padre and vecino not in visitados:  # Evitar volver al nodo padre
            #        queue.append((vecino, paciente))  # Almacenar el vecino y su nodo padre
    return None


def filtrad_sintomas(sintoma_busqueda1,sintoma_busqueda2):
    grafo = create_grafo_general()
    # Agregar nodos al Sub-grafo basado en los sintomas(2) ingresados por el paciente
    # sintoma_busqueda1 = input("Ingrese el primer síntoma: ")
    # sintoma_busqueda2 = input("Ingrese el segundo síntoma: ")
    #sintoma_busqueda1 = 'Rotacion de la pierna'
    #sintoma_busqueda2 = 'Sangre en la orina'
    #sintoma_busqueda1 = 'vomito'
    #sintoma_busqueda2 = 'gripe'

    # cuando pongo el set(0, me indica o le indico que es un conjunto que no admite duplicados)
    pacientes_encontrados = set()
    for nodo in grafo.nodes:
        resultado = BFS(grafo, nodo, sintoma_busqueda1, sintoma_busqueda2)
        if resultado is not None:

            pacientes_encontrados.add(pacientes[resultado-1])

    if not pacientes_encontrados:
        print("No existe paciente con los sintomas ingresados.")
        return set()#validar en el formulario que muestre un mensaje si el conjunto esta vacio
    else:
        print("Pacientes encontrados:")

      # Imprimir los pacientes encontrados
        for paciente in pacientes_encontrados:
            # paciente = main[paciente_id-1]
            print("ID: {}, Sintoma1: {}, Sintoma2: {}".format(
                paciente.id, paciente.sintoma1, paciente.sintoma2))

        # print(pacientes_encontrados)
        return pacientes_encontrados
   


def main():
   grafo_general = create_grafo_general() 
#Crear Sub-grafo de sintomas ingresados
   filtrado = list(filtrad_sintomas())
   if filtrado:
     subgrafo = nx.Graph()
     for i in range(len(filtrado)-1):
            subgrafo.add_edge(filtrado[i].id, filtrado[i+1].id)
   
   
   #Crear formulario
   
   plt.figure(figsize=(15,8))
   
   # Dibujar el grafo_general
   pos = nx.random_layout(grafo_general)
   nx.draw_networkx_nodes(grafo_general, pos, node_size=150, node_color='yellow',alpha=0.9 )
   nx.draw_networkx_labels(grafo_general, pos, font_size=5,alpha=0.5)
   #nx.draw_networkx_edges(grafo_general, pos)
   #edge_labels = nx.get_edge_attributes(grafo_general, 'sintoma')  # Reemplaza 'weight' por el atributo que quieras mostrar
   #nx.draw_networkx_edge_labels(grafo_general, pos, edge_labels=edge_labels,font_size=5)
   
   #Dibujar el sub-grafo
   if filtrado:
      nx.draw(subgrafo, pos, with_labels=True, node_color='green',node_size=50, edge_color='red', alpha=1,font_size=5)
      nx.draw_networkx_labels(subgrafo, pos, font_size=5)
      #nx.draw_networkx_edge_labels( subgrafo, pos, edge_labels=edge_labels, font_size=6)
   
   
   
   plt.title("Red de pacientes por sintomas")
   # Mostrar el grafo_general
   # plt.axis('off')
   plt.tight_layout()
   plt.show()
   plt.close()

#grafo_general = create_grafo_general()   

   