class Pacientes:
    #El excel_prubea.csv, por este cambie id_eess por descripcion
    def __init__(self, id, edad, tipo_edad,sexo, fecha_atencion, diagnostico,tipo_dx,descripcion,sintoma1,sintoma2,id_eess):
        self.id=id
        self.edad= edad
        self.tipo_edad=tipo_edad
        self.sexo=sexo
        self.fecha_atencion=fecha_atencion
        self.diagnostico=diagnostico
        self.tipo_dx=tipo_dx
        self.descripcion=descripcion
        self.sintoma1=sintoma1
        self.sintoma2=sintoma2
        self.id_eess=id_eess
    
    
    def __str__(self):
       
        return  "ID: %d Edad: %d  Tipo_edad: %s Sexo: %s Fecha atencion: %s Diagnostico: %s Tipo_dx: %s descripcion: %s Sintoma 1: %s Sintoma 2: %s Hospital: %d" % (self.id, self.edad, self.tipo_edad,self.sexo, self.fecha_atencion, self.diagnostico,self.tipo_dx,self.descripcion, self.sintoma1, self.sintoma2, self.id_eess)   
    
    