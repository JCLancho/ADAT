from sqlalchemy import create_engine
from Examen2401.Mapeo import asignaturas, alumnos, notas
from sqlalchemy.orm import sessionmaker

############################################################################
# BLOQUE COMUN CREACION DE LA CONEXION A LA BASE DE DATOS
engine = create_engine("mysql://ex2:adat@172.20.132.130/examen2", echo=False)

Session = sessionmaker(bind=engine)
session = Session()
############################################################################

# Muestra por pantalla las notas de las asignaturas de cada alumno
result = session.query(alumnos, asignaturas, notas).filter(alumnos.DNI == notas.DNI,
                    asignaturas.COD == notas.COD).order_by(alumnos.APENOM.desc())

# almaceno los nombres de los alumnos para mostrarlos solo una vez como cabecera
arrayAlumnos = []
for alumno, asignatura, nota in result: #recorro y muestro la información del alumno
    if alumno.APENOM not in arrayAlumnos: #compruebo si ya he mostrado el nombre
        arrayAlumnos.append(alumno.APENOM)
        print()
        print(alumno.APENOM)
        print("---------------------")
    print(asignatura.ABREVIATURA, "\t", nota.NOTA)

session.close()



