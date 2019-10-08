import os
import shutil


class sistemaArchivos:

    menu = """
    ¿Qué desea hacer?
        1.- Crear un directorio nuevo
        2.- Listar un directorio
        3.- Copiar un archivo
        4.- Mover un archivo
        5.- Eliminar un archivo/directorio
        6.- Salir del programa
        """

    def crear(self):
        ruta = input("Introduce la ruta del directorio que quieres crear")
        nombre = input("Introduce el nombre del nuevo directorio")
        rutaCompleta = ruta+"/"+nombre
        try:
            if os.path.exists(rutaCompleta):
                print("El directorio ya existe")
            else:
                os.makedirs(rutaCompleta)
                print("Directorio creado")
        except OSError:
            print("Ruta no valida")

    def listar(self):
        ruta = input("Introduce la ruta del directorio que quieres mostrar")
        try:
            lista = os.listdir(ruta)
            if lista.__len__() == 0:
                print("<-- CARPETA VACIA --> ")
            else:
                for archivo in lista:
                    rutaCompleta = ruta+"/"+archivo
                    if os.path.isfile(rutaCompleta):
                        print("ARCHIVO --> %s" % archivo)
                    else:
                        print("DIRECTORIO --> %s" % archivo)
        except OSError:
            print("Ruta no valida")

    def copiar(self):
        ruta = input("Introduce la ruta completa hasta el archivo que quieres copiar")
        rutaDestino = input("Introduce la ruta de destino con el nombre de la copia que vas a crear")
        try:
            shutil.copyfile(ruta, rutaDestino)
        except OSError:
            print("Ruta no valida")

    def mover(self):
        ruta = input("Introduce la ruta completa hasta el archivo que quieres mover")
        rutaDestino = input("Introduce la ruta de destino completa con el nombre del archivo incluido")
        try:
            shutil.move(ruta, rutaDestino)
        except OSError:
            print("Ruta no valida")

    def eliminar(self):
        ruta = input("Ruta del archivo/directorio a eliminar")
        try:
            if os.path.isfile(ruta):
                os.remove(ruta)
                print("Archivo eliminado")
            else:
                lista = os.listdir(ruta)
                if lista.__len__() == 0:
                    os.removedirs(ruta)
                    print("Directorio eliminado")
                else:
                    print("El directorio esta lleno, no se eliminará")
        except OSError:
            print("Ruta no valida")


sa = sistemaArchivos()
options = {"1": sa.crear,
           "2": sa.listar,
           "3": sa.copiar,
           "4": sa.mover,
           "5": sa.eliminar
           }
opcion = input(sa.menu)
while opcion != "6":
    try:
        options[opcion]()
    except KeyError:
        print("Elige una opcion del menu")
    opcion = input(sa.menu)






