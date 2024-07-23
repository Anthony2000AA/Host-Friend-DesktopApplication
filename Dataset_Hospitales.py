from Hospitales import Hospitales
import csv



def archivo(file):
    aux=''
   
    hospitalesLeidos=[]
    with open(file, newline='') as f:
        data=csv.reader(f,delimiter=';')
        next(data,None)#Omite el encabezado
        aux=list(data)
    #print(aux)    
    for fila in aux:
           id=int(fila[0])
           nombre=str(fila[1])
           id_ubigeo=int(fila[2])
           direccion=str(fila[3])
           codigo_renaes=str(fila[4])
           longitud=float(fila[5])
           latitud=float(fila[6])
           capacidad=int(fila[7])
           
           hospitalesLeidos.append(Hospitales(id,nombre,id_ubigeo,direccion,codigo_renaes,longitud,latitud,capacidad))   
     
    #print(hospitalesLeidos[20])    
    return hospitalesLeidos

#archivo('archivo2.csv')