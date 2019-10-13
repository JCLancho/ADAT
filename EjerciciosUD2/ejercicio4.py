import lxml.etree as lxmlET
import pickle

#crearemos objetos olimpiada segun los leemos del xml
class Olimpiada:

    def __init__(self, anio, juegos, temporada, ciudad):
        self.anio = anio
        self.juegos = juegos
        self.temporada = temporada
        self.ciudad = ciudad


class ficheroBinario:

    menu = """
    ¿Qué desea hacer?
        1.- Crear fichero serializable de olimpiadas
        2.- Añadir edición olímpica
        3.- Buscar olimpiadas por sede
        4.- Eliminar edición olímpica
        5.- Salir del programa
        """

    def crearFicheroSerializableOlimpiadas(self):
        arrayOlimpiadas = []
        tree = lxmlET.parse('olimpiadas.xml')
        root = tree.getroot()
        archivoObjetos = open('pickle.obj', 'wb')
        for element in root:
            anio = element.attrib["year"]
            juegos = element[0].text
            temporada = element[1].text
            ciudad = element[2].text
            olimpiada = Olimpiada(anio, juegos, temporada, ciudad)
            arrayOlimpiadas.append(olimpiada)
        pickle.dump(arrayOlimpiadas, archivoObjetos)
        archivoObjetos.close()
        print("Archivo creado")

    def anadirEdicionOlimpica(self):
        archivoObjetos = open('pickle.obj', 'rb')
        objetos = pickle.load(archivoObjetos)
        archivoObjetos.close()

        archivoObjetos = open('pickle.obj', 'wb')
        print("Introduce los valores de la nueva edicion olimpia:")
        anio = input("\tAño: ")
        temporada = input("\tTemporada: ")
        juegos = anio + " " + temporada
        ciudad = input("\tCiudad: ")
        olimpiada = Olimpiada(anio, juegos, temporada, ciudad)
        objetos.append(olimpiada)
        pickle.dump(objetos, archivoObjetos)
        archivoObjetos.close()

        print("Edición añadida")

    def buscarOlimpiadasSede(self):
        ciudad = input("¿En base a qué ciudad desea buscar?")
        archivoObjetos = open('pickle.obj', 'rb')
        objetos = pickle.load(archivoObjetos)
        encontrado = False

        for obj in objetos:
            if obj.ciudad == ciudad:
                print(obj.ciudad, obj.anio)
                encontrado = True

        if not encontrado:
            print("Ninguna olimpiada con esa sede")

        archivoObjetos.close()

    def eliminarEdicionOlimpica(self):
        year = input("¿De qué año es la edicion que desea borrar?")
        season = input("¿De qué estación?")
        busqueda = year + " " + season
        arrayOlimpiadas = []
        archivoObjetos = open('pickle.obj', 'rb')
        objetos = pickle.load(archivoObjetos)
        encontrado = False

        for obj in objetos:
            if not busqueda == obj.juegos:
                arrayOlimpiadas.append(obj)
            else:
                encontrado = True

        archivoObjetos.close()

        if not encontrado:
            print("No se ha podido borrar, ninguna edición encontrada")
        else:
            file = open('pickle.obj', 'wb')
            pickle.dump(arrayOlimpiadas, file)
            file.close()
            print("Edición borrada")




fichero = ficheroBinario()
options = {"1": fichero.crearFicheroSerializableOlimpiadas,
           "2": fichero.anadirEdicionOlimpica,
           "3": fichero.buscarOlimpiadasSede,
           "4": fichero.eliminarEdicionOlimpica
           }
opcion = input(fichero.menu)
while opcion != "5":
    try:
        options[opcion]()
    except KeyError:
        print("Elige una opcion del menu")
    opcion = input(fichero.menu)






