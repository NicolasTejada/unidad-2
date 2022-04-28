

class Email():

    __idCuenta= ""
    __dominio= ""
    __tipoDominio= ""
    __contrase = ""

    def __init__(self, id, dom, tipo, cont):
        self.__idCuenta = id
        self.__dominio = dom
        self.__tipoDominio= tipo
        self.__contrase=cont
        pass

    def getDominio(self):
        return self.__dominio


    def retornaEmail(self):
        print("%s@%s.%s" %(self.__idCuenta, self.__dominio, self.__tipoDominio))

    def crearCuenta(self, mail):
        cadena= mail.split("@")
        dom = cadena[1].split(".")

        nuevo= Email(cadena[0], dom[0], dom[1])
        

def funcion1():
        nombre = input('Ingrese su nombre: ')
        idCu= input('Ingrese el id de la cuenta: ') 
        dominio= input('Ingrese el dominio: ')
        tipoD= input('Ingrese el tipo de dominio de la cuenta ')
        cont= input("ingrese su contraseña")
        nuevo = Email(idCu, dominio, tipoD, cont)

        print("Estimado %s te enviaremos mensajes a %s " %(nombre , Email.retornaEmail(nuevo)))


if __name__ == "__main__":

     
       funcion1()



    



    


