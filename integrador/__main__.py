from manejadorCamas import arregloCamas


if __name__=='__main__':
    aCamas=arregloCamas()
    aCamas.testCamas()
    
    
    nya=input('Ingrese el nombre y el apellido del paciente: ')
    cama=aCamas.buscarCama(nya)
    
    print('PACIENTE: {}                  CAMA:{}  HABITACION:{} '.format(aCamas[cama].getPac(), cama+1, aCamas[cama].getHab()))
    print(' DIAGNOSTICO: {}              FECHA DE INTERNACION:{}'.format(aCamas[cama].getDiag(), aCamas[cama].getFecInt))
    print('FECHA DE ALTA: {}'.format(aCamas[cama].getFecAlt))
    print('*************MEDICAMENTOS***************************')
    print('Monodroga:    Presentacion:     Cantidad:  Precio: ')
    print(aCamas[cama].listarMed())
    
    
    
    