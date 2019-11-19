import mysql.connector
from mysql.connector import Error, cursor


class Ejercicio4:
    """Clase para el ejercicio 4, es identico al ejercicio 3"""

    selectAlumno = """select alumnos.APENOM
    from alumnos
    where alumnos.DNI = %s"""

    selectAsignatura = """SELECT asignaturas.COD, asignaturas.NOMBRE, asignaturas.ABREVIATURA
FROM `asignaturas`"""

    # esta vez haremos el ejercicio 3 con una funcion almacenada en la base de datos, aqui como llamarla
    procedimiento = "SELECT insertar_nota(%s, %s, %s)"

    def __init__(self):
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

    def calificacion(self):
        dni = input("Escribe el DNI del alumno que deseas modificar")
        self.cursor.execute(self.selectAlumno, (dni,))
        resultado = self.cursor.fetchone()
        print(resultado[0])
        print("Listado de asignaturas disponibles:")
        self.cursor.execute(self.selectAsignatura)
        for row in self.cursor:
            print(row[0], "-. ", row[1], " ", row[2])
        codAsignatura = input("Escribe el código de la asignatura a evalura:")
        nota = input("Escribe la nota del alumno:")
        # lo unico que cambia con el ejercicio 3 es la query, por lo demas igual
        # ya se encarga la funcion de decirnos si añadimos o insertamos
        # rescatamos ese valor y lo mostramos
        self.cursor.execute(self.procedimiento, (codAsignatura, dni, nota))
        info = self.cursor.fetchone()
        print(info[0])
        self.connection.commit()
        self.cerrar()

    def cerrar(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("MySQL connection is closed")


e4 = Ejercicio4()
e4.calificacion()

