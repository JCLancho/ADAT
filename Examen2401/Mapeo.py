from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
Base = declarative_base()

# clase encargada de relacionar los elementos de la base de datos con los objetos
# se mapea cada uno con su correspondiente, construyendo las relaciones


class alumnos(Base):
    __tablename__ = 'alumnos'
    DNI = Column(String, primary_key=True)
    APENOM = Column(String)
    POBLA = Column(String)
    TELEF = Column(String)


class asignaturas(Base):
    __tablename__ = "asignaturas"
    COD = Column(Integer, primary_key=True)
    NOMBRE = Column(String)
    ABREVIATURA = Column(String)


class notas(Base):
    __tablename__ = "notas"
    DNI = Column(String,  ForeignKey('alumnos.DNI'), primary_key=True)
    COD = Column(Integer, ForeignKey('asignaturas.COD'), primary_key=True)
    NOTA = Column(Integer)
    alumnos = relationship("alumnos", back_populates="notas")
    asignaturas = relationship("asignaturas", back_populates="notas")


alumnos.notas = relationship("notas", back_populates="alumnos")
asignaturas.notas = relationship("notas", back_populates="asignaturas")

