import mysql.connector
from mysql.connector import Error, cursor


class Ejercicio1:
    """Clase para el ejercicio 1"""

    # Es una consulta grande, necesito informacion de las 3 tablas
    query = """select alumnos.APENOM, asignaturas.ABREVIATURA, notas.NOTA 
from alumnos, asignaturas, notas 
where alumnos.DNI = notas.DNI
and notas.COD = asignaturas.COD
order by alumnos.APENOM desc"""

    def __init__(self):
        """Constructor de la clase, crea la conexion y el cursor"""
        try:
            self.connection = mysql.connector.connect(host='172.20.132.130',
                                                      user='ex2',
                                                      password='adat',
                                                      database='examen2')
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("MySQL connection is open")
        except Error as e:
            print("Error while connecting to MySQL", e)

    def notas(self):
        """Muestra por pantalla las notas de las asignaturas de cada alumno"""
        # Ejecuto la consulta
        self.cursor.execute(self.query)
        nombres = []
        # por cada tupla devuelta por la consulta muestro solo una vez el nombre del alumno
        # y todas sus asignaturas
        for row in self.cursor:
            if row[0] not in nombres:
                nombres.append(row[0])
                print()
                print(row[0])
                print("---------------------")
            print(row[1], "\t",  row[2])
        self.cerrar()

    def cerrar(self):
        """Se encarga de cerrar la conexion y el cursor"""
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("MySQL connection is closed")


e1 = Ejercicio1()
e1.notas()

