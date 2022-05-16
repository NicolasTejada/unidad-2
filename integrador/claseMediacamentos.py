class Medicamento():
    __idCama=0
    __idMedicamento=0
    __nombreComercial=''
    __monodroga=''
    __presentacion=''
    __cantidadAplicada=''
    __precio=0.0
    
    def __init__(self, cama, medica, nom, monodr, presentacion, cantidad, precio):
        self.__idCama=cama
        self.__idMedicamento=0
        self.__nombreComercial=nom
        self.__monodroga=monodr
        self.__presentacion= presentacion
        self.__cantidadAplicada= cantidad
        self.__precio=precio
    
    def getId(self):
        return self.__idCama
    
    def getcant(self):
        return self.__cantidadAplicada
    def getM(self):
        return self.__monodroga
    def getPres(self):
        return self.__presentacion
    def getPrecio(self):
        return self.__precio
    def getTotal(self):
        return (self.__cantidadAplicada * self.__precio)