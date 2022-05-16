import csv 

from claseMediacamentos import Medicamento


class manejadorMedicamentos():
    __listaMedicam=[]
    
    def __init__(self):
        self.__listaMedicam=[]
        
    def agregarMedicamento(self, medic):
        self.__listaMedicam.append(medic)
        
    def getCama(self, med):
        return self.__listaMedicam[med].getId()
    
        
        
    def testMedica(self):
        archivo=open("medicamentos.csv")
        reader= csv.reader(archivo, delimiter=';')
        bandera='true'
        for fila in reader :
            if bandera:
                '''saltear cabezera'''
                bandera='false'
            else:
                numCama=fila[0]
                medi=fila[1]
                nombre=fila[2]
                mdroga=fila[3]
                present=fila[4]
                cant=fila[5]
                precio=fila[6]
            
            unMedicamento=Medicamento(numCama, medi,nombre, mdroga, present, cant, precio)
            self.agregarMedicamento(unMedicamento)
            
            
        archivo.close()