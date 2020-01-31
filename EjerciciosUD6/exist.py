import pyexistdb.db as db

# creo la conexion con la base de datos
conexion = db.ExistDB("http://admin:admin@localhost:8080/exist")

# creo la collecion a la que voy a subir los documentos con la informacion necesaria
conexion.createCollection("gimnasio", overwrite=True)

# leo cada archivo para subirlo a exist
file = open("ColeccionGimnasio/actividades_gim.xml", encoding="ISO-8859-1")
xml = file.read()
conexion.load(xml, "gimnasio/actividades_gim.xml")
file.close()

file = open("ColeccionGimnasio/socios_gim.xml", encoding="ISO-8859-1")
xml = file.read()
conexion.load(xml, "gimnasio/socios_gim.xml")
file.close()

file = open("ColeccionGimnasio/uso_gimnasio.xml", encoding="ISO-8859-1")
xml = file.read()
conexion.load(xml, "gimnasio/uso_gimnasio.xml")
file.close()

# cargo la consulta intermedia y la almaceno en una variable para poder ejecutarla
file = open("ColeccionGimnasio/consulta_intermedia.xquery", encoding="ISO-8859-1")
intermedio = file.read()
file.close()

# cargo la consulta final y la almaceno en una variable para poder ejecutarla
file = open("ColeccionGimnasio/consulta_final.xquery", encoding="ISO-8859-1")
final = file.read()
file.close()

# ejecuto la consulta intermedia y la subo
result_id = conexion.executeQuery(intermedio)
conexion.load(conexion.retrieve_text(result_id, 0), "gimnasio/cuotas_intermedias.xml")

# utilizando la consulta intermedia ejecuto la consulta final y la subo
result_id = conexion.executeQuery(final)
conexion.load(conexion.retrieve_text(result_id, 0), "gimnasio/cuotas_finales.xml")

# borro la consulta intermedia
conexion.removeDocument("gimnasio/cuotas_intermedias.xml")

print("Cuotas finales calculadas correctamente")
print("Se pueden consultar en la base de datos de exist, collecion 'gimansio'")

