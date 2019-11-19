import mysql.connector
from mysql.connector import Error, cursor


class Ejercicio2:
    """Clase para el ejercicio 2"""

    # selecciono el alumno al que quiero cambiar el nombre, solo uno
    selectQuery = """select alumnos.APENOM
from alumnos
where alumnos.DNI = %s"""

    # actualizo el nombre del alumno encontrado
    updateQuery = """update alumnos set alumnos.APENOM = %s where alumnos.DNI = %s """

    def __init__(self):
        """Constructor, crea la conexion y el cursor para el acceso a la base de datos"""
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

    def cambiarNombre(self):
        """Metodo que cambia el nombre a 1 alumno"""
        dni = input("Escribe el DNI del alumno que deseas modificar")
        # muestro el nombre actual del alumno encontrado
        self.cursor.execute(self.selectQuery, (dni,))
        resultado = self.cursor.fetchone()
        print(resultado[0])
        # pido un nuevo nombre
        nuevoNombre = input("Escribe el nuevo nombre para el alumno")
        if nuevoNombre != "":
            # actualizo el nombre
            self.cursor.execute(self.updateQuery, (nuevoNombre, dni))
            print("Alumno modificado correctamente")
            self.connection.commit()
        print("Fin del programa.")
        self.cerrar()

    def cerrar(self):
        """Cierra la conexion y el cursor"""
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("MySQL connection is closed")


e2 = Ejercicio2()
e2.cambiarNombre()

