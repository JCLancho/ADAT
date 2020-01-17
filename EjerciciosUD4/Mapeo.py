from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, Enum, ForeignKey
from sqlalchemy.orm import relationship
Base = declarative_base()


class Deporte(Base):
    __tablename__ = 'Deporte'
    id_deporte = Column(Integer, primary_key=True)
    nombre = Column(String)


class Deportista(Base):
    __tablename__ = 'Deportista'
    id_deportista = Column(Integer, primary_key=True)
    nombre = Column(String)
    sexo = Column(Enum('M', 'F'))
    peso = Column(Integer)
    altura = Column(Integer)


class Equipo(Base):
    __tablename__ = 'Equipo'
    id_equipo = Column(Integer, primary_key=True)
    nombre = Column(String)
    iniciales = Column(String)


class Evento(Base):
    __tablename__ = 'Evento'
    id_evento = Column(Integer, primary_key=True)
    nombre = Column(String)
    id_olimpiada = Column(Integer, ForeignKey('Olimpiada.id_olimpiada'))
    id_deporte = Column(Integer, ForeignKey('Deporte.id_deporte'))
    Olimpiada = relationship("Olimpiada", back_populates="Evento")
    Deporte = relationship("Deporte", back_populates="Evento")


class Olimpiada(Base):
    __tablename__ = 'Olimpiada'
    id_olimpiada = Column(Integer, primary_key=True)
    nombre = Column(String)
    anio = Column(Integer)
    temporada = Column(Enum('Summer', 'Winter'))
    ciudad = Column(String)


class Participacion(Base):
    __tablename__ = 'Participacion'
    id_deportista = Column(Integer, ForeignKey('Deportista.id_deportista'), primary_key=True)
    id_evento = Column(Integer, ForeignKey('Evento.id_evento'), primary_key=True)
    id_equipo = Column(Integer, ForeignKey('Equipo.id_equipo'))
    edad = Column(Integer)
    medalla = Column(String)
    Deportista = relationship("Deportista", back_populates="Participacion")
    Evento = relationship("Evento", back_populates="Participacion")
    Equipo = relationship("Equipo", back_populates="Participacion")


Olimpiada.Evento = relationship("Evento", order_by = Evento.id_evento, back_populates = "Olimpiada")
Deporte.Evento = relationship("Evento", order_by = Evento.id_evento, back_populates = "Deporte")
Deportista.Participacion = relationship("Participacion", back_populates="Deportista")
Evento.Participacion = relationship("Participacion",  back_populates="Evento")
Equipo.Participacion = relationship("Participacion",  back_populates="Equipo")