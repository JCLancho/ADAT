import csv
import lxml.etree as lxmlET
import pickle
from lxml import etree as tree

from Examen2510.Batalla import Batalla


class GameOfThrones:
    """Clase Game Of Thones, gestionara las batallas de la serie, con xml, csv y archivo binario"""

    menu = """
    
    ¿Qué desea hacer?
        1.- Buscar batallas por región
        2.- Crear XML batallas
        3.- Crear fichero binario objetos
        4.- Eliminar batalla fic. Binario objetos
        
        0.- Salir
        
        """

    def bucarBatallasRegion(self):
        """Busca batallas por la region introdudicida """
        region = input("¿Las batallas de qué región desea buscar?")
        ganador = ""
        with open('battles.csv') as lectura:
            reader = csv.DictReader(lectura)
            for row in reader:
                if region == row["region"]:
                    if row["attacker_outcome"] == "win":
                        ganador = "Gana atacante"
                    elif row["attacker_outcome"] == "loss":
                        ganador = "Gana defensor"
                    else:
                        ganador = "Nadie gana"
                    print("\tRegiṕn: "+row["region"] +
                          "\t Localización: "+row["location"] +
                          "\t Nombre de la batalla: "+row["name"] +
                          "\t Año: "+row["year"] +
                          "\t Rey atacante: "+row["attacker_king"] +
                          "\t Rey defensor: "+row["defender_king"] +
                          "\t Resultado de la batalla: " + ganador)
        if ganador == "":
            print("Ninguna batalla encontrada para esa region")

    def crearXML(self):
        """Crear xml usando la clase lxml"""
        juego_tronos = tree.Element("juego_tronos")
        with open('battles.csv') as lectura:
            reader = csv.DictReader(lectura)
            for row in reader:
                batalla = tree.SubElement(juego_tronos, "batalla", id=row["battle_number"])
                nombre = tree.SubElement(batalla, "nombre")
                nombre.text = row["name"]
                anio = tree.SubElement(batalla, "anio")
                anio.text = row["year"]
                region = tree.SubElement(batalla, "region")
                region.text = row["region"]
                localizacion = tree.SubElement(batalla, "localizacion")
                if row["location"] == "":
                    localizacion.text = "no_place"
                else:
                    localizacion.text = row["location"]

                resultadoAtacante = ""
                resultadoDefensor = ""
                if row["attacker_outcome"] == "win":
                    resultadoAtacante = "S"
                    resultadoDefensor = "N"
                else:
                    resultadoAtacante = "N"
                    resultadoDefensor = "S"
                ataque = tree.SubElement(batalla, "ataque", tamanio=row["attacker_size"], gana=resultadoAtacante)
                rey = tree.SubElement(ataque, "rey")
                if row["attacker_king"] == "":
                    rey.text = "no_king"
                else:
                    rey.text = row["attacker_king"]
                comandante = tree.SubElement(ataque, "comandante")
                comandante.text = row["attacker_commander"]
                i = 1
                while i <= 4:
                    campo = "attacker_"+i.__str__()
                    if row[campo] != "":
                        familia = tree.SubElement(ataque, "familia")
                        familia.text = row[campo]
                    i += 1

                defensa = tree.SubElement(batalla, "defensa", tamanio=row["defender_size"], gana=resultadoDefensor)
                rey = tree.SubElement(defensa, "rey")
                if row["defender_king"] == "":
                    rey.text = "no_king"
                else:
                    rey.text = row["defender_king"]
                comandante = tree.SubElement(defensa, "comandante")
                comandante.text = row["defender_commander"]
                i = 1
                while i <= 4:
                    campo = "defender_" + i.__str__()
                    if row[campo] != "":
                        familia = tree.SubElement(defensa, "familia")
                        familia.text = row[campo]
                    i += 1
        print("Archivo generado correctamente")


        with open("battles.xml", "w+") as xml:
            arbolXML = tree.tostring(juego_tronos, pretty_print=True, xml_declaration='utf-8')
            xml.write(arbolXML.decode('utf-8'))


    def crearFicheroBinario(self):
        """crea el fichero binario basandonos en el xml creado anteriormente"""
        arrayBatallas = []
        tree = lxmlET.parse('battles.xml')
        root = tree.getroot()
        archivoObjetos = open('battles.bin', 'wb')
        for element in root:
            id = element.attrib["id"]
            nombre = element[0].text
            anio = element[1].text
            region = element[2].text
            localizacion = element[3].text
            rey_atacante = element[4].text
            rey_defensor = element[5].text
            gana_atacante = element[4].attrib["gana"]
            batalla = Batalla(id, nombre, anio, region, localizacion, rey_atacante, rey_defensor, gana_atacante)
            arrayBatallas.append(batalla)
        pickle.dump(arrayBatallas, archivoObjetos)
        archivoObjetos.close()
        print("Archivo creado")


    def eliminarBatalla(self):
        """Elimina una batalla segun el ID introducido"""
        id = input("Introduce el identificador de la batalla?")
        arrayBatallas = []
        archivoObjetos = open('battles.bin', 'rb')
        objetos = pickle.load(archivoObjetos)
        encontrado = False
        for obj in objetos:
            if not id == obj.id:
                arrayBatallas.append(obj)
            else:
                encontrado = True

        archivoObjetos.close()

        if not encontrado:
            print("No se ha podido borrar, ninguna batalla encontrada")
        else:
            borrar = input("Batalla encontrada ¿Desea borrarla? S/N")
            if borrar == "S":
                file = open('battles.bin', 'wb')
                pickle.dump(arrayBatallas, file)
                file.close()
                print("Batalla borrada")





got = GameOfThrones()
options = {"1": got.bucarBatallasRegion,
           "2": got.crearXML,
           "3": got.crearFicheroBinario,
           "4": got.eliminarBatalla
           }
opcion = input(got.menu)
while opcion != "0":
    try:
        options[opcion]()
    except KeyError:
        print("Elige una opcion del menu")
    opcion = input(got.menu)






