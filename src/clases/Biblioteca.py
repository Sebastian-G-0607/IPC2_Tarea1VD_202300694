from .Recurso import Recurso
from .Libro import Libro
from .Revista import Revista
from .Video import Video

class Biblioteca:

    __recursos = []

    def agregarRecurso(self, recurso):
        self.__recursos.append(recurso)

    def mostrarRecursosDisponibles(self):
        for recurso in self.__recursos: 
            if recurso.getDisponibilidad() == True:
                recurso.informacionDetallada()

    def buscarPorAutor(self, autor):
        for recurso in self.__recursos:
            if recurso.getAutor() == autor:
                recurso.informacionDetallada()

    def buscarPorTipo(self, tipo):
        for recurso in self.__recursos:
            if tipo == "Libro" or tipo == "libro":
                if isinstance(recurso, Libro):
                    recurso.informacionDetallada()
            elif tipo == "Revista" or tipo == "revista":
                if isinstance(recurso, Revista):
                    recurso.informacionDetallada()
            elif tipo == "Video" or tipo == "video":
                if isinstance(recurso, Video):
                    recurso.informacionDetallada()


    def eliminarRecurso(self, Recurso):
        for recurso in self.__recursos:
            if recurso.getTitulo() == Recurso:
                self.__recursos.remove(recurso)

    def prestarRecurso(self, Recurso):
        for recurso in self.__recursos:
            if recurso.getTitulo() == Recurso:
                recurso.prestar()

    def devolverRecurso(self, Recurso):
        for recurso in self.__recursos:
            if recurso.getTitulo() == Recurso:
                recurso.devolver()

    def getRecursos(self):
        return self.__recursos
