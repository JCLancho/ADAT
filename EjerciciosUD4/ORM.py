class Orm:

    menu = """
    ¿Qué desea hacer?
        1.- Listado de deportistas participantes
        2.- Modificar medalla deportista
        3.- Añadir deportista/participación
        4.- Eliminar participación
        0.- Salir
        """

    def listadoDeportistasDiferentes(self):
        pass

    def listadoDeportistasParticipantes(self):
        pass

    def modificarMedallaDeportista(self):
        pass

    def anadirDeportistaParticipacion(self):
        pass

    def eliminarParticipacion(self):
        pass


o = Orm()
options = {"1": o.listadoDeportistasParticipantes,
           "2": o.modificarMedallaDeportista,
           "3": o.anadirDeportistaParticipacion,
           "4": o.eliminarParticipacion
           }
opcion = input(o.menu)
while opcion != "0":
    try:
        options[opcion]()
    except KeyError:
        print("Elige una opcion del menu")
    opcion = input(o.menu)
