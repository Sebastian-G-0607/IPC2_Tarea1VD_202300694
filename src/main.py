import time
from clases.Biblioteca import Biblioteca
from clases.Libro import Libro
from clases.Video import Video
from clases.Revista import Revista

nuevaBiblioteca = Biblioteca()

def ingresarLibro():
    print("")
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    anio = int(input("Ingrese el año de la publicación del libro: "))
    genero = input("Ingrese el genero del libro: ")
    numPag = int(input("Ingrese el número de páginas del libro: "))
    nuevoLibro = Libro(titulo, autor, anio, genero, numPag)
    nuevaBiblioteca.agregarRecurso(nuevoLibro)

def ingresarRevista():
    print("")
    titulo = input("Ingrese el título de la revista: ")
    autor = input("Ingrese el autor de la revista: ")
    anio = int(input("Ingrese el año de la publicación de la revista: "))
    edicion = int(input("Ingrese el número de edición de la revista: "))
    frecuencia = input("Ingrese la frecuencia de publicación de la revista: ")
    nuevaRevista = Revista(titulo, autor, anio, edicion, frecuencia)
    nuevaBiblioteca.agregarRecurso(nuevaRevista)

def ingresarVideo():
    print("")
    titulo = input("Ingrese el título del video: ")
    autor = input("Ingrese el autor del video: ")
    anio = int(input("Ingrese el año de la publicación del video: "))
    duracion = int(input("Ingrese la duración del video: "))
    formato = input("Ingrese el formato del video: ")
    nuevoVideo = Video(titulo, autor, anio, duracion, formato)
    nuevaBiblioteca.agregarRecurso(nuevoVideo)


def ingresarRecurso():
    opcion = 0
    while opcion != 4:
        print("")
        print("|" + "-"*23 + " Nuevo Recurso " + "-"*22 + "|")
        print("| -1.  Libro" + " "*49 + "|")
        print("| -2.  Revista" + " "*47 + "|")
        print("| -3.  Video" + " "*49 + "|")
        print("| -4.  Salir" + " "*49 + "|")
        print("|" + "-"*60 + "|")
        print("")
        opcion = int(input("Ingrese una opción: "))

        match opcion:
            case 1:
                ingresarLibro()
            case 2:
                ingresarRevista()
            case 3:
                ingresarVideo()
            case 4:
                pass
            case _:
                print("")
                print("Opción no válida, intente de nuevo...")
                time.sleep(1)

def buscarPorAutor():
    print("")
    autor = input("Ingrese el autor de la(s) obra(s): ")
    nuevaBiblioteca.buscarPorAutor(autor)
    
def buscarPorTipo():
    print("")
    tipo = input("Ingrese el tipo de la(s) obra(s): ")
    nuevaBiblioteca.buscarPorTipo(tipo)

def buscarRecurso():
    opcion = 0
    while opcion != 3:
        print("")
        print("|" + "-"*22 + " Buscar Recurso " + "-"*22 + "|")
        print("| -1.  Buscar por autor" + " "*38 + "|")
        print("| -2.  Buscar por tipo" + " "*39 + "|")
        print("| -3.  Salir" + " "*49 + "|")
        print("|" + "-"*60 + "|")
        print("")
        opcion = int(input("Ingrese una opción: "))

        match opcion:
            case 1:
                buscarPorAutor()
            case 2:
                buscarPorTipo()
            case 3:
                pass
            case _:
                print("")
                print("Opción no válida, por favor intente de nuevo")
                time.sleep(1)
        
def eliminarRecurso():
    print("")
    eliminar = input("Ingrese el nombre del recurso que se va a eliminar: ")
    nuevaBiblioteca.eliminarRecurso(eliminar)

def prestarRecurso():
    print("")
    nombreObra = input("Ingrese el nombre del recurso a prestar: ")
    nuevaBiblioteca.prestarRecurso(nombreObra)
    print("Recurso prestado con éxito...")
    time.sleep(1)

def devolverRecurso():
    print("")
    nombreObra = input("Ingrese el nombre del recurso a devolver: ")
    nuevaBiblioteca.devolverRecurso(nombreObra)
    print("Recurso devuelto con éxito...")
    time.sleep(1)

def menu():
    opcion = 0

    while opcion != 7:
        print("")
        print("|" + "-"*60 + "|")
        print(f"|{"Biblioteca IPC2":^60}|")
        print("|" + "-"*60 + "|")
        print(f"|{"  1. Ingresar recurso":<60}|")
        print(f"|{"  2. Buscar recurso":<60}|")
        print(f"|{"  3. Eliminar recurso":<60}|")
        print(f"|{"  4. Listar recurso":<60}|")
        print(f"|{"  5. Prestar recurso":<60}|")
        print(f"|{"  6. Devolver recurso":<60}|")
        print(f"|{"  7. Salir":<60}|")
        print("|" + "-"*60 + "|")
        print("")
        opcion = int(input("> Ingrese una opción: "))

        match opcion:
            case 1:
                ingresarRecurso()
            case 2:
                buscarRecurso()
            case 3:
                eliminarRecurso()
            case 4:
                nuevaBiblioteca.mostrarRecursosDisponibles()
            case 5: 
                prestarRecurso()
            case 6:
                devolverRecurso()
            case 7:
                print("")
                print("Hasta pronto...")
                print("")
                time.sleep(1)
            case _:
                print("")
                print("Opción no válida, por favor intente de nuevo")
                time.sleep(1) 

menu()