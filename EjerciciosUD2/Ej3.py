import csv
import xml.sax
from ClaseSax import ClaseSax
import lxml.etree as lxmlET


class GestorXML:

    @staticmethod
    def crearXMLOlimpiadas():

        elolimpiadas = lxmlET.Element("olimpiadas")

        with open("olimpiadas.csv") as fichero_olimpiadas:
            reader = csv.DictReader(fichero_olimpiadas)

            with open("olimpiadas.xml", "w+") as fichero_xml:

                for linea in reader:

                    elolimpiada = lxmlET.SubElement(elolimpiadas, "olimpiada")

                    elolimpiada.set("anio", linea["Year"])

                    eljuegos = lxmlET.SubElement(elolimpiada, "juegos")
                    eljuegos.text = linea["Games"]
                    eltemporada = lxmlET.SubElement(elolimpiada, "temporada")
                    eltemporada.text = linea["Season"]
                    elciudad = lxmlET.SubElement(elolimpiada, "ciudad")
                    elciudad.text = linea["City"]

                datosxml = lxmlET.tostring(elolimpiadas, pretty_print=True, xml_declaration='utf-8')
                fichero_xml.write(datosxml.decode('utf-8'))

    @staticmethod
    def crearXMLDesportistas():

        conjunto_id = set()
        last_sport = ""

        with open("Datos_Olimpiadas/athlete_events.csv") as fichero_olimpiadas:
            reader = csv.DictReader(fichero_olimpiadas)

            with open("deportistas.xml", "w+") as fichero_xml:

                eldeportistas = lxmlET.Element("deportistas")

                for linea in reader:

                    if not (conjunto_id.__contains__(linea["ID"])):
                        eldeportista = lxmlET.SubElement(eldeportistas, "deportista")

                        eldeportista.set("id", linea["ID"])

                        elnombre = lxmlET.SubElement(eldeportista, "nombre")
                        elnombre.text = linea["Name"]
                        elsexo = lxmlET.SubElement(eldeportista, "sexo")
                        elsexo.text = linea["Sex"]
                        elaltura = lxmlET.SubElement(eldeportista, "altura")
                        elaltura.text = linea["Height"]
                        elpeso = lxmlET.SubElement(eldeportista, "peso")
                        elpeso.text = linea["Weight"]
                        conjunto_id.add(linea["ID"])

                        elparticipaciones = lxmlET.SubElement(eldeportista, "participaciones")

                    if not (linea["Sport"] == last_sport):
                        eldeporte = lxmlET.SubElement(elparticipaciones, "deporte")
                        eldeporte.set("nombre", linea["Sport"])
                        last_sport = linea["Sport"]

                    elparticipacion = lxmlET.SubElement(eldeporte, "participacion")
                    elequipo = lxmlET.SubElement(elparticipacion, "equipo")
                    elequipo.text = linea["Team"]
                    eljuegos = lxmlET.SubElement(elparticipacion, "juegos")
                    eljuegos.text = linea["Games"]+" - "+linea["City"]
                    elevento = lxmlET.SubElement(elparticipacion, "evento")
                    elevento.text = linea["Event"]
                    elmedalla = lxmlET.SubElement(elparticipacion, "medalla")
                    elmedalla.text = linea["Medal"]

                datosxml = lxmlET.tostring(eldeportistas, pretty_print=True, xml_declaration='utf-8')

                fichero_xml.write(datosxml.decode('utf-8'))

    @staticmethod
    def crearListadoOlimpiadas():
        source = open("olimpiadas.xml")
        xml.sax.parse(source, ClaseSax())
