from sqlalchemy import create_engine
from sqlalchemy.orm.exc import NoResultFound

from Examen2401.Mapeo import alumnos
from sqlalchemy.orm import sessionmaker


############################################################################
# BLOQUE COMUN CREACION DE LA CONEXION A LA BASE DE DATOS
engine = create_engine("mysql://ex2:adat@172.20.132.130/examen2", echo=False)

Session = sessionmaker(bind=engine)
session = Session()
############################################################################

# Metodo que cambia el nombre a1 alumno seleccionado

# capturo la excepcion generada por el .one() que devuelve un objeto
# si no lo encuentra no puedo mostrarlo y finalizo el programa
# no tiene sentido continuar si no tengo un alumno que actualizar
try:
    dni = input("Escribe el DNI del alumno que deseas modificar")
    # busco y muestro el nombre actual del alumno encontrado
    alumno = session.query(alumnos).filter(alumnos.DNI == dni).one()
    print(alumno.APENOM)
    # pido un nuevo nombre
    nuevoNombre = input("Escribe el nuevo nombre para el alumno")
    # compruebo que el nuevo nombre no este vacio
    if nuevoNombre != "":
        # actualizo el nombre en la BBDD
        session.query(alumnos).filter(alumnos.DNI == dni).update({alumnos.APENOM: nuevoNombre},
                                                                 synchronize_session=False)

        session.commit()
        print("Nombre actualizado correctamente")

except NoResultFound:
    print("Ningun alumno encontrado con ese DNI")
    print("Fin del programa")

session.close()



