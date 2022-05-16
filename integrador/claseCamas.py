class Cama():
    __idCama=0
    __habitacion=0
    __estado=""
    __NYApaciente=""
    __diagnostico=""
    __fechaInt=""
    __fechaAlta=""
    __medicamentos=[]
    
    
    
    def __init__(self, id, hab, diag, fecInt, fecAlt, est='false', nya='none'):
        self.idCama=id
        self.__habitacion=hab
        self.__estado=est
        self.__NYApaciente=nya
        self.__diagnostico=diag
        self.__fechaInt=fecInt
        self.__fechaAlta=fecAlt
        
       
        
    def setMed(self, medicamento):
       self.__medicamentos.append(medicamento)
       
    
    def getId(self):
        return self.__idCama 
    
    def getPac(self):
        return self.__NYApaciente
        
    def getDiagn(self):
        return self.__diagnostico
        
    def getFecAlta(self):
        return self.__fechaAlta
        
    def getFecInt(self):
        return self.__fechaInt
    def getHab(self):
        return self.__habitacion
    
    
    def getTotalMed(self):
        total=0
        for i in range(len(self.__medicamentos)):
           total+=self.__medicamentos[i].getTotal
        
    def setestado(self):
        self.__estado
        
    def getMedicamento(self):
        
       return self.__medicamentos