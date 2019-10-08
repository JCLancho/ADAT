lista = []
for contador in range(3):
    numero = int(input("introduce un numero"))
    lista.append(numero)

print(lista.__str__())

print("La suma es", sum(lista))

print("La media es", sum(lista)/lista.__len__())
