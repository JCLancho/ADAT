lista = []
for contador in range(0,10):
    numero = input("introduce un numero")
    lista.append(numero)

for elemento in lista:
    print(elemento)

print(lista.__str__())