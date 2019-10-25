class Batalla:
    """Clase batalla, contendra su constructor y el metodo para imprimir"""

    def __init__(self, id, nombre, anio, region, localizacion, rey_atacante, rey_defensor, gana_atacante):
        """Constructor con todos los parametros de la batalla"""
        self.id = id
        self.nombre = nombre
        self.anio = anio
        self.region = region
        self.localizacion = localizacion
        self.rey_atacante = rey_atacante
        self.rey_defensor = rey_defensor
        self.gana_atacante = gana_atacante

    def __str__(self):
        """Metodo que devuelve una cadena de caracteres para ser imprimido"""
        return "The " + self.nombre + " took place in " + self.localizacion + " " \
            "(" + self.region + ") in the year " + self.anio + ". The King(s) " \
            "" + self.rey_atacante + " fought against " + self.rey_defensor + " and he/they " + self.gana_atacante

