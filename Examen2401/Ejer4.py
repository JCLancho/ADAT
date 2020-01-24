from sqlalchemy import create_engine
from sqlalchemy.orm.exc import NoResultFound

from Examen2401.Mapeo import asignaturas, alumnos, notas
from sqlalchemy.orm import sessionmaker


############################################################################
# BLOQUE COMUN CREACION DE LA CONEXION A LA BASE DE DATOS
engine = create_engine("mysql://ex2:adat@172.20.132.130/examen2", echo=False)

Session = sessionmaker(bind=engine)
session = Session()
############################################################################


# Metodo que se encarga de actualizar o insertar una nota

# capturo la excepcion generada por el .one() que devuelve un objeto
# si no lo encuentra no puedo mostrarlo y finalizo el programa
# no tiene sentido continuar si no tengo un alumno que actualizar
try:
    # muestro la informacion del alumno que busco
    dni = input("Escribe el DNI del alumno que deseas modificar")
    alumno = session.query(alumnos).filter(alumnos.DNI == dni).one()
    print(alumno.APENOM)

    # muestro la informacion de las asignaturas disponibles
    result = session.query(asignaturas)
    for asignatura in result:
        print(asignatura.COD, "-.", asignatura.NOMBRE, "(", asignatura.ABREVIATURA, ")")

    # me quedo con la asignatura seleccionada
    codAsignatura = input("Escribe el código de la asignatura a evalura:")
    # introduzco una nota para ese alumno y asignatura
    nuevaNota = input("Escribe la nota del alumno:")
    # compruebo si tengo que hacer un update o un insert
    result = session.query(notas).filter(notas.DNI == dni, notas.COD == codAsignatura).count()
    if result == 1:  # si el resultado es 1, es un update
        session.query(notas).filter(notas.DNI == dni, notas.COD == codAsignatura)\
            .update({notas.NOTA: nuevaNota}, synchronize_session=False)
        print("La nota se ha modificado")
    else:  # si el resultado es 0, es un insert (y no hay mas opciones, o 0 o 1)
        insertarNota = notas(DNI=dni, COD=codAsignatura, NOTA=nuevaNota)
        session.add(insertarNota)
        print("La nota se ha añadido")
    session.commit()
except NoResultFound:
    print("Ningun alumno encontrado con ese DNI")
    print("Fin del programa")

session.close()



