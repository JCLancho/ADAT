import pyexistdb.db as db

# creo la conexion con la base de datos
conexion = db.ExistDB("http://admin:admin@localhost:8080/exist")

# creo la collecion a la que voy a subir los documentos con la informacion necesaria
conexion.createCollection("ventas", overwrite=True)

# leo cada archivo para subirlo a exist
file = open("ColeccionVentas/clientes.xml", encoding="ISO-8859-1")
xml = file.read()
conexion.load(xml, "ventas/clientes.xml")
file.close()

file = open("ColeccionVentas/detallefacturas.xml", encoding="ISO-8859-1")
xml = file.read()
conexion.load(xml, "ventas/detallefacturas.xml")
file.close()

file = open("ColeccionVentas/productos.xml", encoding="ISO-8859-1")
xml = file.read()
conexion.load(xml, "ventas/productos.xml")
file.close()

file = open("ColeccionVentas/facturas.xml", encoding="ISO-8859-1")
xml = file.read()
conexion.load(xml, "ventas/facturas.xml")
file.close()

print("Coleccion 'Ventas' creada y cargada correctamente")
