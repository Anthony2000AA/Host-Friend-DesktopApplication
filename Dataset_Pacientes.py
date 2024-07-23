from Pacientes import Pacientes
import csv

import networkx as nx
import matplotlib.pyplot as plt

def archivo(file):
    aux=''
   
    pacientesLeidos=[]
    with open(file, newline='') as f:
        data=csv.reader(f,delimiter=';')
        next(data,None)#Omite el encabezado
        aux=list(data)
    #print(aux)    
    for fila in aux:
           id=int(fila[0])
           edad=int(fila[1])
           tipo_edad=str(fila[2])
           sexo=str(fila[3])
           fecha_atencion=str(fila[4])
           diagnostico=str(fila[5])
           tipo_dx=str(fila[6])
           descripcion= str((fila[7]))#Cambie id_eess por descripcion
           sintoma1=str((fila[8]))
           sintoma2= str((fila[9]))
           id_eess= int((fila[10]))
          
           pacientesLeidos.append(Pacientes(id, edad, tipo_edad,sexo, fecha_atencion, diagnostico,tipo_dx,descripcion,sintoma1,sintoma2,id_eess))   
     
    #print(pacientesLeidos[18])    
    return pacientesLeidos
 
   







   
#print(archivo('Prueba2CSV.csv') )