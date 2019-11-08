import mysql.connector
from mysql.connector import Error, cursor

class Conexion:

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
        self.crearTablas()


    def conectarBBDD(self):
        try:
            self.connection = mysql.connector.connect(host='localhost',
                                                      user='dm2',
                                                      password='dm2',
                                                      database='olimpiadas')
            if self.connection.is_connected():
                self.cursor = self.connection.cursor()
                print("Conectado a olimpiadas")
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
