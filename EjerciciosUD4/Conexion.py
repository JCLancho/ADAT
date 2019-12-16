from sqlalchemy import create_engine, text, select
from EjerciciosUD4.Mapeo import Deporte, Deportista, Equipo, Evento, Olimpiada, Participacion
from sqlalchemy.orm import sessionmaker


class Conexion:

    def __init__(self):

        self.engine = create_engine("mysql://dm2:dm2@localhost/olimpiadas", echo=True)

    def menu1(self):
        temporada = input("Selecciona la temporada Winter o Summer (W/S)")
        if temporada== 'W':
            temporada = "Winter"
        elif temporada == 'S':
            temporada = "Summer"
        Session = sessionmaker(bind=self.engine)
        session = Session()
        result = session.query(Olimpiada).filter(Olimpiada.temporada == temporada)
        for row in result:
            print(row.id_olimpiada, row.nombre)

        edicionOlimpica = input("Introduce el codigo de la edición olimpica que desea")
        result = session.query(Evento).filter(Evento.id_olimpiada == edicionOlimpica)
        for row in result:
            print(row.id_olimpiada, row.nombre)

        session.close()

