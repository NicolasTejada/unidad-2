import csv

import numpy as np

from claseCamas import Cama

from manejadorMedicamentos import  manejadorMedicamentos

class arregloCamas():
    __cantidad=0
    __dimension=0
    __incremento=1
    
    def __init__(self, dimension=30, incremento=1):
        self.__Camas= np.empty(dimension,dtype=(Cama))
        self.__cantidad=0
        self.__dimension=dimension
    
    def setcamas(self):
        for i in len(self.__Camas):
            self.__Camas[i]=Cama(i)
            
        
    def agregarCama(self,unaCama,c ):
        self.__Camas[c-1]=unaCama
        self.__Camas[c-1].setestado="true"
        self.__cantidad+=1
        
    def medicamentos(self):
        
        mM= manejadorMedicamentos()
        
        for i in len(mM.listaMedicam):
            if mM.getCama(i) == self.__Camas[i].getId():
                self.__Camas[i].setMed(mM.__listaMedicam[i])
                
    def totalMedicame(self):
        total=0
        for i in range(len(self.listaMedicam)):
            total+= self.listaMedicam[i].getTotal
                
    def buscarCama(self, paciente):
       
        bandera= 'false' 
        i=0
        while bandera == 'false':
                                   
            if self.__Camas[i].getPac()==paciente:
                bandera=='true'
                
            else:
                i+=1
    

                
        return i
        
    def listarMed(self):
        
        
        for i in len(self.__Camas.getMed()):
            print(self.__)

    def testCamas(self):
        self.setcamas()
        
        archivo=open("camas.csv")
        reader= csv.reader(archivo, delimiter=';')
        bandera='true'
        for fila in reader :
            if bandera:
                '''saltear cabezera'''
                bandera='false'
            else:
                numCama=fila[0]
                hab=fila[1]
                est=fila[2]
                nya=fila[3]
                diag=fila[4]
                fecInt=fila[5]
                fecAlt=fila[6]
            
            unaCama= Cama(numCama, hab, est, nya, diag, fecInt, fecAlt)
            self.agregarCama(unaCama, numCama)
            
            
        archivo.close()
        
        