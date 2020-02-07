import pyexistdb.db as db

# creo la conexion con la base de datos
conexion = db.ExistDB("http://admin:admin@localhost:8080/exist")

#insertar datos de la factura
print("Vamos a introducir los datos de la factura")
numFactura = input("Introduce el numero de la factura")
fecha = input("Introduce la fecha de la factura")
importe = input("Introduce el importe de la factura")
numCliente = input("Introduce el numero del cliente asociado a la factura")

#valido que el cliente exista
consulta = """exists(collection("/db/ventas")/clientes/clien[@numero = %s]) """ % numCliente
result_id = conexion.executeQuery(consulta)
existe = conexion.retrieve_text(result_id, 0)
while existe == "false":
    print("El cliente introducido no existe")
    numCliente = input("Introduce el numero del cliente asociado a la factura")
    consulta = """exists(collection("/db/ventas")/clientes/clien[@numero = %s]) """ % numCliente
    result_id = conexion.executeQuery(consulta)
    existe = conexion.retrieve_text(result_id, 0)

# creo la factura
factura = """   <factura numero='%s'>
    <fecha>%s</fecha>
    <importe>%s</importe>
    <numcliente>%s</numcliente>
</factura>""" % (numFactura, fecha, importe, numCliente)

# hago el insert en el xml de facturas
consulta = "update insert %s into /facturas" % factura
conexion.executeQuery(consulta)

print("factura insertada correctamente")


#insertar datos del detalle de la factura
print("Vamos a introducir los detalles de la factura")
codigoFactura = input("Introduce el codigo de la factura")

# creo el detalle de la factura
detalle = """   <factura numero='%s'>
    <codigo>%s</codigo>
</factura>""" % (numFactura, codigoFactura)


# hago el insert en el xml de detalle facturas
consulta = "update insert %s into /detallefacturas" % detalle
conexion.executeQuery(consulta)

print("detalle factura insertado correctamente")

# productos asociados al detalle de la factura
print("Vamos a introducir los productos asociados a la factura")
codigoProducto = input("Introduce el codigo del producto")
while codigoProducto != "0":

    #validar que el codigo del producto no sea 0 y exista en la BBDD
    consulta = """exists(collection("/db/ventas")/productos/product[codigo = %s]) """ % codigoProducto
    result_id = conexion.executeQuery(consulta)
    existe = conexion.retrieve_text(result_id, 0)
    while existe == "false":
        print("El producto introducido no existe")
        codigoProducto = input("Introduce el codigo del producto")
        consulta = """exists(collection("/db/ventas")/productos/product[codigo = %s]) """ % codigoProducto
        result_id = conexion.executeQuery(consulta)
        existe = conexion.retrieve_text(result_id, 0)

    descuento = input("Introduce el descuento del producto")
    unidades = input("Introduce el stock del producto")

    # creo el producto
    producto = """  <product descuento='%s'>
        <codigo>%s</codigo>
        <unidades>%s</unidades>
    </product>""" % (descuento, codigoProducto, unidades)

    # hago el insert en el xml de detalle facturas
    consulta = "update insert %s into /detallefacturas/factura[@numero = %s]" % (producto, numFactura)
    conexion.executeQuery(consulta)

    print("Producto agregado correctamente")
    codigoProducto = input("Introduzca el codigo del siguiente producto")
