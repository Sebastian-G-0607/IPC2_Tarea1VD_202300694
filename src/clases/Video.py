from .Recurso import Recurso

class Video(Recurso):
    def __init__(self, titulo, autor, anioPublicacion, duracion, formato):
        super().__init__(titulo, autor, anioPublicacion)
        self.__duracion = duracion
        self.__formato = formato

    def informacionDetallada(self):
        super().informacionDetallada("Video")
        print(f"|{"Duración del video":<30}|{self.__duracion:<30}|")
        print(f"|{"Formato del video":<30}|{self.__formato:<30}|")
        print("|" + "-"*61 + "|")
        print("")

    #SETTERS
    def setDuracion(self, duracion):
        self.__duracion = duracion

    def setFormato(self, formato):
        self.__formato = formato
    
    #GETTERS
    def getDuracion(self):
        return self.__duracion
    
    def getFormato(self):
        return self.__formato