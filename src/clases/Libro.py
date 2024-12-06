from .Recurso import Recurso

class Libro(Recurso):
    def __init__(self, titulo, autor, anioPublicacion, genero, numeroPaginas):
        super().__init__(titulo, autor, anioPublicacion)
        self.__genero = genero
        self.__numeroPaginas = numeroPaginas

    def informacionDetallada(self):
        super().informacionDetallada("Libro")
        print(f"|{"Genero":<30}|{self.__genero:<30}|")
        print(f"|{"Número de páginas":<30}|{self.__numeroPaginas:<30}|")
        print("|" + "-"*61 + "|")
        print("")

    #SETTERS
    def setGenero(self, genero):
        self.__genero = genero

    def setNumeroPaginas(self, numero):
        self.__numeroPaginas = numero
    
    #GETTERS
    def getGenero(self):
        return self.__genero
    
    def getNumeroPaginas(self):
        return self.__numeroPaginas