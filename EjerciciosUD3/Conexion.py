import mysql.connector
from mysql.connector import Error


class Conexion:

    def __init__(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 user='dm2',
                                                 password='dm2')

            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)
                cursor.execute("CREATE DATABASE mydatabase")
                connection.commit()
                connection = mysql.connector.connect(host='localhost',
                                                 user='dm2',
                                                 password='dm2',
                                                 database='mydatabase')
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)

        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
