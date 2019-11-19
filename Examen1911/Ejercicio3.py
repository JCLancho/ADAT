import mysql.connector
from mysql.connector import Error, cursor


class Ejercicio3:
    """Clase para el ejercicio 3"""

    # select para encontrar un alumno
    selectAlumno = """select alumnos.APENOM
    from alumnos
    where alumnos.DNI = %s"""

    # select para mostrar todas las asignaturas
    selectAsignatura = """SELECT asignaturas.COD, asignaturas.NOMBRE, asignaturas.ABREVIATURA
FROM `asignaturas`"""

    # select para saber si un alumno ya tiene nota en una asignatura o no
    # devuelve 0 si no tiene nota en esa asignatura (insertar)
    # devuelve 1 si ya tiene una nota (actualizar)
    selectCount = """SELECT count(*)
from notas
where notas.DNI = %s
and notas.COD = %s"""

    # actualizar la nota de un alumno
    updateNota = """update notas set notas.NOTA = %s where notas.DNI = %s and notas.COD = %s"""

    # insertar una nueva nota para una nueva asignatura para un alumno
    insertNota = """insert into notas (DNI, COD, NOTA) values (%s, %s, %s)"""

    def __init__(self):
        """Constructor, crea la conexion y el cursor para la base de datos"""
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
        """Metodo que se encarga de actualizar o insertar una nota"""
        # muestro la informacion del alumno que busco
        dni = input("Escribe el DNI del alumno que deseas modificar")
        self.cursor.execute(self.selectAlumno, (dni,))
        resultado = self.cursor.fetchone()
        print(resultado[0])
        # muestro la informacion de las asignaturas disponibles
        print("Listado de asignaturas disponibles:")
        self.cursor.execute(self.selectAsignatura)
        for row in self.cursor:
            print(row[0], "-. ", row[1], " ", row[2])
        # me quedo con la asignatura seleccionada
        codAsignatura = input("Escribe el código de la asignatura a evalura:")
        # introduzco una nota para ese alumno y asignatura
        nota = input("Escribe la nota del alumno:")
        # compruebo si tengo que hacer un update o un insert
        self.cursor.execute(self.selectCount, (dni, codAsignatura))
        resultado = self.cursor.fetchone()
        if resultado[0] == 1:  # si el resultado es 1, es un update
            self.cursor.execute(self.updateNota, (nota, dni, codAsignatura))
            self.connection.commit()
            print("La nota se ha modificado")
        else:  # si el resultado es 0, es un insert (y no hay mas opciones, o 0 o 1)
            self.cursor.execute(self.insertNota, (dni, codAsignatura, nota))
            self.connection.commit()
            print("La nota se ha añadido")
        self.cerrar()

    def cerrar(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("MySQL connection is closed")


e3 = Ejercicio3()
e3.calificacion()
