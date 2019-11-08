from EjerciciosUD3.Conexion import Conexion


class Olimpiadas:

    menu = """
    ¿Qué desea hacer?
        1.- Crear BBDD MySQL
        2.- Crear BBDD SQLite
        3.- Listado de deportistas en diferentes deportes
        4.- Listado de deportistas participantes
        5.- Modificar medalla deportista
        6.- Añadir deportista/participación
        7.- Eliminar participación
        0.- Salir
        """

    def crearBbddMySql(self):
        c = Conexion()
        if c.existeBBDD():
            c.borrarBBDD()
        c.crearBBDD()
        c.cerrar()

    def crearBbddSqlite(self):
        pass

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


o = Olimpiadas()
options = {"1": o.crearBbddMySql,
           "2": o.crearBbddSqlite,
           "3": o.listadoDeportistasDiferentes,
           "4": o.listadoDeportistasParticipantes,
           "5": o.modificarMedallaDeportista,
           "6": o.anadirDeportistaParticipacion,
           "7": o.eliminarParticipacion
           }
opcion = input(o.menu)
while opcion != "0":
    try:
        options[opcion]()
    except KeyError:
        print("Elige una opcion del menu")
    opcion = input(o.menu)
