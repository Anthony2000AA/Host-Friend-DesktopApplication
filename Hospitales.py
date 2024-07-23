class Hospitales:
  
    def __init__(self, id,nombre,id_ubigeo,direccion,codigo_renaes,longitud,latitud,capacidad):
        self.id=id
        self.nombre=nombre
        self.id_ubigeo=id_ubigeo
        self.direccion=direccion
        self.codigo_renaes=codigo_renaes
        self.longitud=longitud
        self.latitud=latitud
        self.capacidad=capacidad
       
    
    
    def __str__(self):
       
        return  "ID: %d Codigo_renaes: %s  Nombre: %s Direccion: %s Longitud: %f latitud: %f ID_ubigeo: %d capacidad: %d" % (self.id, self.codigo_renaes,self.nombre,self.direccion, self.longitud, self.latitud,self.id_ubigeo,self.capacidad)
       # return  "ID: %d Nombre: %s  ID_ubigeo: %d Direccion: %s Longitud: %f latitud: %f ID_ubigeo: %d" % (self.id, self.codigo_renaes,self.nombre,self.direccion, self.longitud, self.latitud,self.id_ubigeo)      
    
    