import networkx as nx
#import matplotlib.pyplot as plt

from Dataset_Pacientes import archivo



def all_pacientes():
  
  #main=archivo('CSV_Oficial_Pacientes.csv')
  
  #main=archivo('CSV_Pacientes_V2.csv')
  main=archivo('CSV_Pacientes_V2.csv')
  return main


def create_grafo_general():
 main=all_pacientes()         
 grafo_general = nx.Graph()


 #Agregar nodos al grafo_general
 for paciente in main:
    
    id_persona = paciente.id
    grafo_general.add_node(id_persona)

 #Agregar aristas basadas en la relación de sintomas en comun
 for paciente1 in main:
    for paciente2 in main:
        id_persona1, sintoma11, sintoma12  = paciente1.id, paciente1.sintoma1, paciente1.sintoma2
        id_persona2, sintoma21, sintoma22  = paciente2.id, paciente2.sintoma1, paciente2.sintoma2
        if (sintoma11 == sintoma21 or sintoma12 == sintoma22 or sintoma11 == sintoma22 or sintoma21 == sintoma12) and id_persona1 != id_persona2:
            
            if(sintoma11==sintoma21):
             grafo_general.add_edge(id_persona1, id_persona2, sintoma=sintoma11)
             
            if(sintoma12==sintoma22):
             grafo_general.add_edge(id_persona1, id_persona2, sintoma=sintoma12)
             
            if(sintoma11==sintoma22):
             grafo_general.add_edge(id_persona1, id_persona2, sintoma=sintoma11)
             
            if(sintoma21==sintoma12):
             grafo_general.add_edge(id_persona1, id_persona2, sintoma=sintoma21)
             
            if(sintoma11==sintoma21 and sintoma12==sintoma22) or (sintoma11==sintoma22 and sintoma12==sintoma21):
             grafo_general.add_edge(id_persona1, id_persona2, sintoma=sintoma11+ " / "+sintoma22) 
  
 return grafo_general              
   
   
   



