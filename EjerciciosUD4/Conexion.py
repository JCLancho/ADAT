from sqlalchemy import create_engine, text, select
from EjerciciosUD4.Mapeo import Deporte, Deportista, Equipo, Evento, Olimpiada, Participacion
from sqlalchemy.orm import sessionmaker


class Conexion:

    def __init__(self):

        self.engine = create_engine("mysql://dm2:dm2@localhost/olimpiadas", echo=True)

    def menu1(self):
        temporada = input("Selecciona la temporada Winter o Summer (W/S)")
        if temporada == 'W':
            temporada = "Winter"
        elif temporada == 'S':
            temporada = "Summer"
        Session = sessionmaker(bind=self.engine)
        session = Session()
        result = session.query(Olimpiada).filter(Olimpiada.temporada == temporada)
        for row in result:
            print(row.id_olimpiada, row.nombre)

        idOlimpiada = input("Introduce el codigo de la edición olimpica que desea")
        nombreOlimpiada = (session.query(Olimpiada.nombre).filter(Olimpiada.id_olimpiada == idOlimpiada).one())[0]

        result = session.query(Deporte).filter(Deporte.id_deporte == Evento.id_deporte, Evento.id_olimpiada == idOlimpiada)
        for row in result:
            print(row.id_deporte, row.nombre)

        idDeporte = input("Introduce el codigo del deporte seleccionado")
        nombreDeporte = (session.query(Deporte.nombre).filter(Deporte.id_deporte == idDeporte).one())[0]

        result = session.query(Evento).filter(Evento.id_deporte == idDeporte, Evento.id_olimpiada == idOlimpiada)
        for row in result:
            print(row.id_evento, row.nombre)

        idEvento = input("Introduce el codigo del evento seleccionado")
        nombreEvento = (session.query(Evento.nombre).filter(Evento.id_evento == idEvento).one())[0]

        print("""Resumen:
            Temporada: %s
            Edición olimpica: %s
            Deporte: %s
            Evento: %s""" % (temporada, nombreOlimpiada, nombreDeporte, nombreEvento))

        print("Deportistas participantes:")
        result = session.query(Deportista, Participacion, Equipo).filter(Participacion.id_evento == Evento.id_evento,
                                                                         Participacion.id_deportista == Deportista.id_deportista,
                                                                         Participacion.id_equipo == Equipo.id_equipo)
        for deportista, participacion, equipo in result:
            print("\t", deportista.nombre, deportista.altura, deportista.peso,
                  participacion.edad, participacion.medalla, equipo.nombre)


        session.close()

