import lxml.etree as lxmlET
import pickle


class Olimpiada:

    def __init__(self, anio, juegos, temporada, ciudad):
        self.anio = anio
        self.juegos = juegos
        self.temporada = temporada
        self.ciudad = ciudad


class GestorBinario:

    @staticmethod
    def crearFichSerializable():

        olimpiadas = []

        tree = lxmlET.parse('olimpiadas.xml')
        root = tree.getroot()

        file = open('pickle.txt', 'wb')

        for element in root:

            anio = element.attrib["anio"]

            juegos = element[0].text

            temporada = element[1].text

            ciudad = element[2].text

            olimpiada = Olimpiada(anio, juegos, temporada, ciudad)

            olimpiadas.append(olimpiada)

        pickle.dump(olimpiadas, file)

        file.close()

    @staticmethod
    def aniadirEdicion():
        file = open('pickle.txt', 'rb')
        datos = pickle.load(file)
        file.close()

        file = open('pickle.txt', 'wb')

        anio = input("Introduce año")

        juegos = input("Introduce juegos")

        temporada = input("Introduce temporada")

        ciudad = input("Introduce ciudad")

        olimpiada = Olimpiada(anio, juegos, temporada, ciudad)

        datos.append(olimpiada)

        pickle.dump(datos, file)

        file.close()

    @staticmethod
    def buscarPorSede(ciudad):
        file = open('pickle.txt', 'rb')
        datos = pickle.load(file)

        for item in datos:
            if item.ciudad == ciudad:
                print(item.ciudad, item.anio)

        file.close()

    @staticmethod
    def eliminarEdicion(anio, temporada):

        olimpiadas = []

        file = open('pickle.txt', 'rb')
        datos = pickle.load(file)

        for item in datos:
            if not item.anio == anio and not item.temporada == temporada:
                olimpiadas.append(item)

        file.close()

        file = open('pickle.txt', 'wb')

        pickle.dump(olimpiadas, file)

        file.close()
