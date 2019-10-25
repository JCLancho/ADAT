import csv
import xml.sax
from lxml import etree as tree

from EjerciciosUD2.ClaseSax import ClaseSax


class gestorXML:

    menu = """
    ¿Qué desea hacer?
        1.- Crear fichero XML de olimpiadas
        2.- Crear un fichero XML de deportistas
        3.- Listado de olimpiadas
        4.- Salir del programa
        """

    def crearXMLOlimpiadas(self):
        coleccion = []
        with open('athlete_events.csv') as lectura:
            reader = csv.DictReader(lectura)
            for row in reader:
                coleccion.append({'Games': row["Games"],
                                     "Year": row["Year"],
                                     "Season": row["Season"],
                                     "City": row["City"]})
        olimpiadas = tree.Element("olimpiadas")

        for row in coleccion:
            olimpiada = tree.SubElement(olimpiadas, "olimpiada", year=row["Year"])
            juegos = tree.SubElement(olimpiada, "juegos")
            juegos.text = row["Games"]
            temporada = tree.SubElement(olimpiada, "temporada")
            temporada.text = row["Season"]
            ciudad = tree.SubElement(olimpiada, "ciudad")
            ciudad.text = row["City"]

        with open("olimpiadas.xml", "w+") as xml:
            arbolXML = tree.tostring(olimpiadas, pretty_print=True, xml_declaration='utf-8')
            xml.write(arbolXML.decode('utf-8'))

        print("Archivo creado")

    def crearXMLDeportistas(self):
        with open("athlete_events.csv") as lectura:
            reader = csv.DictReader(lectura)
            deportistas = tree.Element("deportistas")
            coleccionIDs = set()
            deporteActual = ""
            for row in reader:
                if not (coleccionIDs.__contains__(row["ID"])):
                    deportista = tree.SubElement(deportistas, "deportista")
                    deportista.set("id", row["ID"])
                    nombre = tree.SubElement(deportista, "nombre")
                    nombre.text = row["Name"]
                    sexo = tree.SubElement(deportista, "sexo")
                    sexo.text = row["Sex"]
                    altura = tree.SubElement(deportista, "altura")
                    altura.text = row["Height"]
                    peso = tree.SubElement(deportista, "peso")
                    peso.text = row["Weight"]
                    coleccionIDs.add(row["ID"])
                    participaciones = tree.SubElement(deportista, "participaciones")

                if not (row["Sport"] == deporteActual):
                    deporte = tree.SubElement(participaciones, "deporte")
                    deporte.set("nombre", row["Sport"])
                    deporteActual = row["Sport"]

                participacion = tree.SubElement(deporte, "participacion")
                equipo = tree.SubElement(participacion, "equipo")
                equipo.text = row["Team"]
                juegos = tree.SubElement(participacion, "juegos")
                juegos.text = row["Games"] + " - " + row["City"]
                evento = tree.SubElement(participacion, "evento")
                evento.text = row["Event"]
                medalla = tree.SubElement(participacion, "medalla")
                medalla.text = row["Medal"]

        with open("deportistas.xml", "w+") as xml:
            arbolXML = tree.tostring(deportistas, pretty_print=True, xml_declaration='utf-8')
            xml.write(arbolXML.decode('utf-8'))

        print("Archivo creado")

    def listarOlimpiadas(self):
        source = open("olimpiadas.xml")
        xml.sax.parse(source, ClaseSax())
        source.close()


gestor = gestorXML()
options = {"1": gestor.crearXMLOlimpiadas,
           "2": gestor.crearXMLDeportistas,
           "3": gestor.listarOlimpiadas
           }
opcion = input(gestor.menu)
while opcion != "4":
    try:
        options[opcion]()
    except KeyError:
        print("Elige una opcion del menu")
    opcion = input(gestor.menu)






