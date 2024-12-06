from .Recurso import Recurso

class Revista(Recurso):
    def __init__(self, titulo, autor, anioPublicacion, numeroEdicion, frecuenciaPublicacion):
        super().__init__(titulo, autor, anioPublicacion)
        self.__numeroEdicion = numeroEdicion
        self.__frecuenciaPublicacion = frecuenciaPublicacion

    def informacionDetallada(self):
        super().informacionDetallada("Revista")
        print(f"|{"Numero de edición":<30}|{self.__numeroEdicion:<30}|")
        print(f"|{"Frecuencia de publicación":<30}|{self.__frecuenciaPublicacion:<30}|")
        print("|" + "-"*61 + "|")
        print("")

    #SETTERS
    def setNumeroEdicion(self, edicion):
        self.__numeroEdicion = edicion

    def setFrecuenciaPublicacion(self, frecuencia):
        self.__frecuenciaPublicacion = frecuencia

    #GETTERS
    def getNumeroEdicion(self):
        return self.__numeroEdicion
    
    def getFrecuenciaPublicacion(self):
        return self.__frecuenciaPublicacion