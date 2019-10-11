import xml.sax


class ClaseSax(xml.sax.ContentHandler):

    elvalido = 0

    def __init__(self):
        xml.sax.ContentHandler.__init__(self)

    def startElement(self, name, attrs):
        if name == "juegos":
            self.elvalido = 1
        if name == "olimpiada":
            self.elvalido = 1
            print("Año :" + attrs.getValue("anio"), end=", ")

    def endElement(self, name):
        self.elvalido = 0

    def characters(self, content):
        if self.elvalido == 1:
            print("Juegos :"+content)
