import pyexistdb.db as db

# creo la conexion con la base de datos
conexion = db.ExistDB("http://admin:admin@localhost:8080/exist")

# almaceno la consulta
consulta = """xquery version '3.1';
for $factura in collection('/db/ventas')/facturas/factura
return <facturasclientes>
    {collection('/db/ventas')/clientes/clien[@numero = $factura/numcliente]/nombre}
    <nufac>{$factura/@numero/data()}</nufac>
    </facturasclientes>"""

# ejecuto la consulta
result_id = conexion.executeQuery(consulta)

# recorro cada resultado y lo muestro
for resultado in range(conexion.getHits(result_id)):
    print(conexion.retrieve_text(result_id, resultado))

