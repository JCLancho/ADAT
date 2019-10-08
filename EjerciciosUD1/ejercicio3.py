lista = []
while lista.__len__() < 3:
    try:
        numero = int(input("introduce un numero impar"))
        while numero % 2 == 0:
            numero = int(input("introduce un numero impar"))
        lista.append(numero)
    except ValueError:
        pass

print(lista.__str__())

print("La suma es",sum(lista))

print("La media es",sum(lista)/lista.__len__())
