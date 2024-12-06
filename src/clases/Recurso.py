class Recurso:
    def __init__(self, titulo, autor, anioPublicacion):
        self.__titulo = titulo
        self.__autor = autor
        self.__anioPublicacion = anioPublicacion
        self.__disponibilidad = True

    def informacionDetallada(self, tipo):
        print("")
        print("|" + "-"*61 + "|")
        print(f"|{"Recurso":^61}|")
        print(f"|{"Recurso":<30}|{tipo:<30}|")
        print(f"|{"Título":<30}|{self.__titulo:<30}|")
        print(f"|{"Autor":<30}|{self.__autor:<30}|")
        print(f"|{"Año de publicación":<30}|{self.__anioPublicacion:<30}|")
        print(f"|{"Disponibilidad":<30}|{str(self.__disponibilidad):<30}|")


    def prestar(self):
        self.__disponibilidad = False
    
    def devolver(self):
        self.__disponibilidad = True

    #SETTERS
    def setTitulo(self, titulo):
        self.__titulo = titulo
    
    def setAutor(self, autor): 
        self.__autor = autor

    def setAnioPublicacion(self, anio):
        self.__anioPublicacion = anio

    #GETTERS
    def getTitulo(self):
        return self.__titulo
    
    def getAutor(self):
        return self.__autor
    
    def getAnioPublicacion(self):
        return self.__anioPublicacion
    
    def getDisponibilidad(self):
        return self.__disponibilidad