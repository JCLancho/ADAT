from sqlalchemy import create_engine, text, select
from EjerciciosUD4.Mapeo import Deporte, Deportista, Equipo, Evento, Olimpiada, Participacion
from sqlalchemy.orm import sessionmaker


class Conexion:
    """Clase que gestiona la conexón a la base de datos mediante el ORM"""

    def __init__(self):
        """Constructor de la clase, se define el conector 'engine'"""

        self.engine = create_engine("mysql://dm2:dm2@localhost/olimpiadas", echo=True)

    def menu1(self):
        """Listar deportistas participantes
        Coleccion de consultas para elegir un parametro que se ira arrastrando hasta la consulta final"""
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

        result = session.query(Deportista, Participacion, Equipo).filter(Participacion.id_evento == Evento.id_evento,
                                                                         Participacion.id_deportista == Deportista.id_deportista,
                                                                         Participacion.id_equipo == Equipo.id_equipo,
                                                                         Evento.id_evento == idEvento,
                                                                         Evento.id_deporte == idDeporte,
                                                                         Evento.id_olimpiada == idOlimpiada)
        print("Deportistas participantes:")
        for deportista, participacion, equipo in result:
            print("\t", deportista.nombre, deportista.altura, deportista.peso,
                  participacion.edad, participacion.medalla, equipo.nombre)

        session.close()

    def menu2(self):
        """Modificar medalla
        Coleccion de consultas para elegir un parametro que se ira arrastrando hasta la consulta final"""
        Session = sessionmaker(bind=self.engine)
        session = Session()

        patron = input("Introduce el nombre del deportista")
        result = session.query(Deportista).filter(Deportista.nombre.like("%"+patron+"%"))
        for deportista in result:
            print(deportista.id_deportista, deportista.nombre)

        idDeportista = input("Elige al deportista por su id")

        result = session.query(Participacion, Evento, Olimpiada).filter(
                                                    Evento.id_evento == Participacion.id_evento,
                                                    Olimpiada.id_olimpiada == Evento.id_olimpiada,
                                                    Participacion.id_deportista == idDeportista)

        for participacion, evento, olimpiada in result:
            print(evento.id_evento, evento.nombre, olimpiada.nombre, olimpiada.ciudad, participacion.medalla)

        id_evento = input("Elige un evento por su id")

        medalla = input("Introduce el nuevo valor para la  medalla (Gold,Silver,Bronze, NA): ")
        session.query(Participacion).filter(Participacion.id_deportista == idDeportista,
                                            Participacion.id_evento == id_evento) \
            .update({Participacion.medalla: medalla}, synchronize_session=False)
        session.commit()
        print("Medalla modificada correctamente")

        session.close()

    def menu3(self):
        """Añadir deportista/participación
        Coleccion de consultas para elegir un parametro que se ira arrastrando hasta la consulta final"""
        Session = sessionmaker(bind=self.engine)
        session = Session()
        idDeportista = 0
        patron = input("Introduce el nombre del deportista")
        result = session.query(Deportista).filter(Deportista.nombre.like("%" + patron + "%"))
        cantidad = result.count()
        if cantidad == 0:
            print("Ningun deportista encontrado para ese patron de busqueda. Se creará uno nuevo")
            nombre = input("Introduce el nombre completo: ")
            sexo = input("Introduce el sexo (M/F): ")
            peso = input("Introduce el peso: ")
            altura = input("Introduce la altura: ")

            idDeportista = (session.query(Deportista).count()+10)
            deportista = Deportista(id_deportista=idDeportista, nombre=nombre, sexo=sexo, peso=peso, altura=altura)
            session.add(deportista)
            session.commit()

        else:
            for deportista in result:
                print(deportista.id_deportista, deportista.nombre)
            idDeportista = input("Elige al deportista por su id")

        temporada = input("Selecciona la temporada Winter o Summer (W/S)")
        if temporada == 'W':
            temporada = "Winter"
        elif temporada == 'S':
            temporada = "Summer"
        result = session.query(Olimpiada).filter(Olimpiada.temporada.like(temporada))
        for olimpiada in result:
            print(olimpiada.id_olimpiada, olimpiada.nombre, olimpiada.ciudad)
        idOlimpiada = input("Introduce el codigo de la edición olimpica que desea")

        result = session.query(Deporte).filter(Evento.id_deporte == Deporte.id_deporte,
                                               Evento.id_olimpiada == idOlimpiada)
        for deporte in result:
            print(deporte.id_deporte, deporte.nombre)
        idDeporte = input("Introduce el codigo del deporte seleccionado")

        result = session.query(Evento).filter(Evento.id_deporte == idDeporte,
                                              Evento.id_olimpiada == idOlimpiada)
        for evento in result:
            print(evento.id_evento, evento.nombre)
        idEvento = input("Introduce el codigo del evento seleccionado")

        result = session.query(Equipo)
        for equipo in result:
            print(equipo.id_equipo, equipo.nombre)
        idEquipo = input("Introduce el codigo del equipo seleccionado")

        edad = input("Introduce la edad del participante: ")
        medalla = input("Introduce la  medalla obtenida en la participacion (Gold,Silver,Bronze, NA): ")

        participacion = Participacion(id_deportista=idDeportista,
                                      id_evento=idEvento,
                                      id_equipo=idEquipo,
                                      edad=edad,
                                      medalla=medalla)
        session.add(participacion)
        session.commit()
        print("Participacion añadida con exito")

        session.close()

    def menu4(self):
        """Eliminar participación
        Coleccion de consultas para elegir un parametro que se ira arrastrando hasta la consulta final"""
        Session = sessionmaker(bind=self.engine)
        session = Session()

        patron = input("Introduce el nombre del deportista")
        result = session.query(Deportista).filter(Deportista.nombre.like("%" + patron + "%"))
        for deportista in result:
            print(deportista.id_deportista, deportista.nombre)
        idDeportista = input("Elige al deportista por su id")

        result = session.query(Participacion, Evento, Olimpiada, Deportista).filter(
            Evento.id_evento == Participacion.id_evento,
            Olimpiada.id_olimpiada == Evento.id_olimpiada,
            Deportista.id_deportista == Participacion.id_deportista,
            Participacion.id_deportista == idDeportista)

        cantidad = result.count()
        if cantidad == 1:
            for participacion, evento, olimpiada, deportista in result:
                print(evento.nombre, olimpiada.nombre, olimpiada.ciudad, participacion.medalla)
                opcion = input("¿Desea borrar esta participación "
                               "y toda la información del deportista asociada? (S/N): ")
                if opcion == "S":
                    session.delete(participacion)
                    session.delete(deportista)
                    print("Deportista y participacion borradas")
                    break
        else:
            for participacion, evento, olimpiada, deportista in result:
                print(participacion.id_evento, evento.nombre, olimpiada.nombre, olimpiada.ciudad, participacion.medalla)
            idEvento = input("Introduce el codigo del evento seleccionado")

            result = session.query(Participacion).filter(Participacion.id_deportista == idDeportista,
                                                         Participacion.id_evento == idEvento)

            for participacion in result:
                session.delete(participacion)

        session.commit()
        print("Participacion borrada")

        session.close()

