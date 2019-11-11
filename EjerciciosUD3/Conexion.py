import csv

import mysql.connector
from mysql.connector import Error, cursor


class Conexion:

    insertDeportista = "INSERT INTO Deportista (id_deportista,nombre,sexo,peso,altura) VALUES (%s,%s,%s,%s,%s)"
    insertDeporte = "INSERT INTO Deporte (nombre) VALUES (%s)"
    insertEquipo = "INSERT INTO Equipo (nombre, iniciales) VALUES (%s,%s)"

    def __init__(self):
        try:
            self.connection = mysql.connector.connect(host='localhost',
                                                 user='dm2',
                                                 password='dm2')
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("MySQL connection is open")
        except Error as e:
            print("Error while connecting to MySQL", e)

    def existeBBDD(self):
        encontrado = False
        self.cursor.execute("SHOW DATABASES")
        for base in self.cursor:
            if base == ('olimpiadas',):
                encontrado = True
        return encontrado

    def borrarBBDD(self):
        self.cursor.execute("DROP DATABASE olimpiadas")
        print("bbdd borrada")

    def crearBBDD(self):
        self.cursor.execute("CREATE DATABASE olimpiadas")
        self.connection.commit()
        print("base de datos creada")
        self.conectarBBDD()


    def conectarBBDD(self):
        try:
            self.connection = mysql.connector.connect(host='localhost',
                                                      user='dm2',
                                                      password='dm2',
                                                      database='olimpiadas')
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("Conectado a olimpiadas")
                self.crearTablas()
        except Error as e:
            print("Error while connecting to MySQL", e)

    def crearTablas(self):
        file = open("olimpiadas.sql")
        sql = file.read()
        resultSet = self.cursor.execute(sql, multi=True)
        for rs in resultSet:
            if rs.with_rows:
                self.cursor.fetchall()
        self.connection.commit()
        print("Tablas creadas")
        self.cargarDatos()

    def cargarDatos(self):
        print("inicio carga")
        olimpiadas = []
        print("leer archivo")
        with open('athlete_events-sort.csv') as lectura:
            reader = csv.DictReader(lectura)
            for row in reader:
                olimpiadas.append(row)
        print("cargar colecciones personalizadas")
        deportistas = []
        ids = []
        deportes = []
        nocs = []
        equipo = []
        for row in olimpiadas:
            if row["ID"] not in ids:
                ids.append(row["ID"])
                deportistas.append([row["ID"], row["Name"], row["Sex"], row["Weight"], row["Height"]])

            if [row["Sport"]] not in deportes:
                deportes.append([row["Sport"]])

            if row["NOC"] not in nocs:
                nocs.append(row["NOC"])
                equipo.append([row["Team"], row["NOC"]])
        print("insertar")
        self.cursor.executemany(self.insertDeportista, deportistas)
        self.connection.commit()
        print("deportistas cargados")
        self.cursor.executemany(self.insertDeporte, deportes)
        self.connection.commit()
        print("deportes cargados")
        self.cursor.executemany(self.insertEquipo, equipo)
        self.connection.commit()
        print("equipos cargados")


    def cerrar(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("MySQL connection is closed")



    # def __init__(self):
    #     try:
    #         connection = mysql.connector.connect(host='localhost',
    #                                              user='dm2',
    #                                              password='dm2')
    #
    #         if connection.is_connected():
    #             db_Info = connection.get_server_info()
    #             print("Connected to MySQL Server version ", db_Info)
    #             cursor = connection.cursor()
    #             cursor.execute("select database();")
    #             record = cursor.fetchone()
    #             print("You're connected to database: ", record)
    #             cursor.execute("CREATE DATABASE mydatabase")
    #             cursor.execute("DROP DATABASE mydat")
    #             connection.commit()
    #             connection = mysql.connector.connect(host='localhost',
    #                                              user='dm2',
    #                                              password='dm2',
    #                                              database='mydatabase')
    #             cursor = connection.cursor()
    #             cursor.execute("select database();")
    #             record = cursor.fetchone()
    #             print("You're connected to database: ", record)
    #
    #     except Error as e:
    #         print("Error while connecting to MySQL", e)
    #     finally:
    #         if connection.is_connected():
    #             cursor.close()
    #             connection.close()
    #             print("MySQL connection is closed")
