from claseViajerosFrecuentes import ViajeroFrecuente

from ManejadorViajeros import manejadorViajero


def menu():
    print('Menu viajeros ')
    print('1- Consultar la Cantidad de Millas ')
    print('2- Acumular Millas')
    print('3- Canjear Millas ')
    print('0- Salir')
    op=input('Ingrese la opcion elegida: ')


    return op


if __name__=='__main__':

    mv=manejadorViajero()
    mv.testViajeros()


    print('********Bienvenido*********')
    codigo=input('Ingrese el codigo del Viajero: ')

    viajero=mv.getViajero(codigo)

    op=menu()

    if op==1:
        print('cantidad Total de millas acumuladas:  {} '.format(mv.__listaViajeros[viajero].getcantidadTotalMillas))

    elif op==2:
        millas=input('Ingrese la cantidad de millas:  ')
        mv.acumularMillas(millas, viajero)

    elif op==3:
        millas=input('Ingrese la cantidad de millas:  ')
        mv.canjearMillas(viajero,millas)
    
    elif op==0:
        exit()
    else: print('La opcion ingresada no es correcta ')

