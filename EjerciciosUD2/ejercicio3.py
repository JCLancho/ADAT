import csv

from lxml import etree as tree

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

        xml = tree.ElementTree(olimpiadas)
        xml.write("olimpiadas.xml")
        #print(tree.tostring(olimpiadas, pretty_print=True))

    def crearXMLDeportistas(self):
        pass

    def listarOlimpiadas(self):
        pass


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






