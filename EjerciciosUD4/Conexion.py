import csv

import mysql.connector
from mysql.connector import Error
from sqlalchemy import create_engine, text
import sqlalchemy.dialects.mysql


class Conexion:

    insertDeportista = "INSERT INTO Deportista (id_deportista,nombre,sexo,peso,altura) VALUES (%s,%s,%s,%s,%s)"
    insertDeporte = "INSERT INTO Deporte (id_deporte, nombre) VALUES (%s,%s)"
    insertEquipo = "INSERT INTO Equipo (id_equipo, nombre, iniciales) VALUES (%s,%s,%s)"
    insertOlimpiada = "INSERT INTO Olimpiada (id_olimpiada, nombre, anio, temporada, ciudad) VALUES (%s,%s,%s,%s,%s)"
    inserEvento = "INSERT INTO Evento (id_evento, nombre, id_olimpiada, id_deporte) VALUES (%s,%s,%s,%s)"
    insertParticipacion = "INSERT INTO Participacion (id_deportista, id_evento, id_equipo, edad, medalla) " \
                          "VALUES (%s,%s,%s,%s,%s)"

    updateMedalla = """UPDATE participacion set participacion.medalla = %s WHERE participacion.id_deportista = %s AND participacion.id_evento = %s"""

    selectOlimpiadas = "SELECT olimpiada.id_olimpiada, olimpiada.nombre, olimpiada.ciudad from olimpiada where olimpiada.temporada = %s"

    selectEventosDeportista = """select evento.id_evento, evento.nombre
from evento
WHERE EXISTS
	(SELECT *
     from participacion
     where participacion.id_evento = evento.id_evento
     AND participacion.id_deportista = %s
    )"""

    selectDeportes = """SELECT deporte.id_deporte, deporte.nombre
FROM deporte
WHERE EXISTS
	(SELECT *
     FROM evento
     WHERE deporte.id_deporte = evento.id_deporte
     AND EXISTS 
     		(SELECT *
             FROM olimpiada
             WHERE olimpiada.id_olimpiada = evento.id_olimpiada
             AND olimpiada.id_olimpiada = %s
            )
    )"""

    selectEvento = """SELECT evento.id_evento, evento.nombre
from evento
WHERE evento.id_olimpiada = %s
and evento.id_deporte = %s"""

    selectDeportistas = """SELECT deportista.nombre, deportista.peso, deportista.altura, participacion.edad, equipo.nombre, participacion.medalla
from deportista, participacion, equipo
WHERE deportista.id_deportista = participacion.id_deportista
and participacion.id_equipo = equipo.id_equipo
and participacion.id_evento = %s"""

    selectDeportistaNombre = """SELECT deportista.id_deportista, deportista.nombre
from deportista
where deportista.nombre LIKE  concat('%',%s,'%')"""

    selectDeportistasDistintosDeportes = """SELECT de.id_deportista, de.nombre, de.sexo, de.peso, de.altura, p.edad, p.medalla, eq.nombre equipo, e.nombre evento, d.nombre deporte, o.nombre olimpiada
from deportista de, deporte d, participacion p, evento e, equipo eq, olimpiada o
WHERE de.id_deportista = p.id_deportista
AND p.id_evento = e.id_evento
and e.id_deporte = d.id_deporte
and p.id_equipo = eq.id_equipo
and o.id_olimpiada = e.id_olimpiada
AND EXISTS
	(SELECT *
     from deportista, deporte, participacion, evento
    WHERE deportista.id_deportista = participacion.id_deportista
    AND participacion.id_evento = evento.id_evento
    and evento.id_deporte = deporte.id_deporte
     and de.id_deportista = deportista.id_deportista
     and d.id_deporte != deporte.id_deporte
    )  
ORDER BY de.id_deportista, o.anio"""

    def __init__(self):

        engine = create_engine("MySQLdb://dm2:dm2@localhost/olimpiadas", echo = True)

        conn = engine.connect()

        # select = deporte.select()
        select = text("SELECT * FROM DEPORTE")

        result = conn.execute(select)
        print(result)
        for row in result:
            print(row)

        conn.close()

        # try:
        #     self.connection = mysql.connector.connect(host='localhost',
        #                                          user='dm2',
        #                                          password='dm2')
        #     if self.connection.is_connected():
        #         self.cursor = self.connection.cursor()
        #         print("MySQL connection is open")
        # except Error as e:
        #     print("Error while connecting to MySQL", e)

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
        except Error as e:
            print("Error while connecting to MySQL", e)

    def crearTablas(self):
        print("Creando tablas")
        file = open("olimpiadas.sql",encoding="utf8")
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
        aiDeportes = 1
        deportesDistintos = []
        dicDeportes = {}
        deportes = []
        aiEquipos = 1
        nocs = []
        equipos = []
        dicEquipos = {}
        olimpiada = []
        olimpiadasDistintas = []
        aiOlimpiadas = 1
        dicOlimpiadas = {}
        eventosDistintos = []
        eventos = []
        aiEventos = 1
        dicEventos = {}
        participaciones = []
        for row in olimpiadas:
            if row["ID"] not in ids:
                ids.append(row["ID"])
                deportistas.append([row["ID"], row["Name"], row["Sex"], row["Weight"], row["Height"]])

            if row["Sport"] not in deportesDistintos:
                deportesDistintos.append(row["Sport"])
                deportes.append([aiDeportes, row["Sport"]])
                dicDeportes.setdefault(row["Sport"], aiDeportes)
                aiDeportes += 1

            if row["NOC"] not in nocs:
                nocs.append(row["NOC"])
                equipos.append([aiEquipos, row["Team"], row["NOC"]])
                dicEquipos.setdefault(row["NOC"], aiEquipos)
                aiEquipos += 1

            if row["Games"] not in olimpiadasDistintas:
                olimpiadasDistintas.append(row["Games"])
                olimpiada.append([aiOlimpiadas, row["Games"], row["Year"], row["Season"], row["City"]])
                dicOlimpiadas.setdefault(row["Games"], aiOlimpiadas)
                aiOlimpiadas += 1

            if [row["Event"], row["Games"]] not in eventosDistintos:
                eventosDistintos.append([row["Event"], row["Games"]])
                eventos.append([aiEventos, row["Event"], dicOlimpiadas.get(row["Games"]), dicDeportes.get(row["Sport"])])
                dicEventos.setdefault(tuple([row["Event"], dicOlimpiadas.get(row["Games"]), dicDeportes.get(row["Sport"])]), aiEventos)
                aiEventos += 1

            participaciones.append([row["ID"],
                dicEventos.get(tuple([row["Event"], dicOlimpiadas.get(row["Games"]), dicDeportes.get(row["Sport"])])),
                dicEquipos.get(row["NOC"]), row["Age"], row["Medal"]])


        print("insertar")
        self.cursor.executemany(self.insertDeportista, deportistas)
        self.connection.commit()
        print("deportistas cargados")
        self.cursor.executemany(self.insertDeporte, deportes)
        self.connection.commit()
        print("deportes cargados")
        self.cursor.executemany(self.insertEquipo, equipos)
        self.connection.commit()
        print("equipos cargados")
        self.cursor.executemany(self.insertOlimpiada, olimpiada)
        self.connection.commit()
        print("olimpiadas cargadas")
        self.cursor.executemany(self.inserEvento, eventos)
        self.connection.commit()
        print("eventos cargadas")
        self.cursor.executemany(self.insertParticipacion, participaciones)
        self.connection.commit()
        print("participaciones cargadas")


    def listarDeportistasDiferentesDeportes(self):
        self.cursor.execute(self.selectDeportistasDistintosDeportes)
        resultado = self.cursor.fetchall()
        deportistas = []
        for result in resultado:
            if result[0] not in deportistas:
                deportistas.append(result[0])
                print()
                print("Deportista: " + result[1] + ", Sexo: " + result[2] + ", Peso: " + str(result[3]) + ", Altura: " + str(result[4]))
            print("\tEdad: %s, Olimpiada: %s, Equipo: %s, Deporte: %s, Evento: %s, Medalla: %s"
                  % (str(result[5]), result[10], result[7], result[9], result[8], result[6]))

    def listarDeportistasFiltro(self):
        temporada = input("Selecciona Winter o Summer (W/S)")
        if temporada == "W":
            temporada = "Winter"
        elif temporada == "S":
            temporada = "Summer"
        print("Ediciones olimpicas para la temporada: %s" % temporada)
        self.cursor.execute(self.selectOlimpiadas, (temporada,))
        for row in self.cursor:
            print(row[0], " ", row[1], " ", row[2])
        olimpiada = input("Selecciona una olimpiada por su codigo")
        print("Deportes celebrados en dicha edicion olimpica")
        self.cursor.execute(self.selectDeportes, (olimpiada,))
        for row in self.cursor:
            print(row[0], " ", row[1])
        deporte = input("Selecciona un deporte por su codigo")
        print("Eventos celebrados en el deporte y edición olímpica seleccionados")
        self.cursor.execute(self.selectEvento, (olimpiada, deporte))
        for row in self.cursor:
            print(row[0], " ", row[1])
        evento = input("Selecciona un evento por su codigo")
        print("Deportistas participantes en el eventos seleccionado:")
        self.cursor.execute(self.selectDeportistas, (evento,))
        for row in self.cursor:
            print(row[0]," ", row[1], " ", row[2], " ", row[3], " ", row[4], " ", row[5])

    def modificarMedalla(self):
        nombre = input("Introduce el nombre del deportista a buscar, o parte de él")
        self.cursor.execute(self.selectDeportistaNombre, (nombre,))
        for row in self.cursor:
            print(row[0], " ", row[1])
        deportista = input("Selecciona el codigo del deportista que desea modificar")
        print("Mostrando los eventos en los que ha participado dicho deportista")
        self.cursor.execute(self.selectEventosDeportista, (deportista,))
        for row in self.cursor:
            print(row[0], " ", row[1])
        evento = input("Seleccion el evento por su codigo")
        medalla = input("Introduce el nuevo valor de la medalla")
        self.cursor.execute(self.updateMedalla, (medalla, deportista, evento))
        self.connection.commit()
        print("Actualizacion realizada correctamente")




    def cerrar(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("MySQL connection is closed")
