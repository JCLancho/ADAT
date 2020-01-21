from EjerciciosUD4.Conexion import Conexion


class Orm:
    """Clase que gestiona y muestra el menu, llamando a los metodos correspondientes"""
    menu = """
    ¿Qué desea hacer?
        1.- Listado de deportistas participantes
        2.- Modificar medalla deportista
        3.- Añadir deportista/participación
        4.- Eliminar participación
        0.- Salir
        """

    def listadoDeportistasParticipantes(self):
        c = Conexion()
        c.menu1()

    def modificarMedallaDeportista(self):
        c = Conexion()
        c.menu2()

    def anadirDeportistaParticipacion(self):
        c = Conexion()
        c.menu3()

    def eliminarParticipacion(self):
        c = Conexion()
        c.menu4()


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
