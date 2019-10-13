import xml.sax


class ClaseSax(xml.sax.ContentHandler):

    imprimir = False

    def __init__(self):
        xml.sax.ContentHandler.__init__(self)

    def startElement(self, name, attrs):
        if name == "olimpiada":
            print("Año: " + attrs.getValue("year"), end=", ")
        if name == "juegos":
            self.imprimir = True

    def characters(self, content):
        if self.imprimir:
            print("Juegos: "+content)
            self.imprimir = False
