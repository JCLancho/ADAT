from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, Enum
Base = declarative_base()


class Deporte(Base):
    __tablename__ = 'Deporte'
    id_deporte = Column(Integer, primary_key=True)
    nombre = Column(String)


class Deportista(Base):
    __tablename__ = 'Deportista'
    id_deportista = Column(Integer, primary_key=True)
    nombre = Column(String)
    sexo = Column(Enum)
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
    id_olimpiada = Column(Integer)
    id_deporte = Column(Integer)


class Olimpiada(Base):
    __tablename__ = 'Olimpiada'
    id_olimpiada = Column(Integer, primary_key=True)
    nombre = Column(String)
    anio = Column(Integer)
    temporada = Column(Enum)
    ciudad = Column(String)


class Participacion(Base):
    __tablename__ = 'Participacion'
    id_deportista = Column(Integer, primary_key=True)
    id_evento = Column(Integer, primary_key=True)
    id_equipo = Column(Integer)
    edad = Column(Integer)
    medalla = Column(String)


