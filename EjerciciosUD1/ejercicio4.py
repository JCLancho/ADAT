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

opcion = input("""¿Qué desea hacer con la lista?
    1. Sumatorio
    2. Media
    3. Máximo
    4. Minimo
    
    0. Salir""")

if opcion == "1":
    print("La suma es", sum(lista))
elif opcion == "2":
    print("La media es", sum(lista)/lista.__len__())
elif opcion == "3":
    print("El valor maximo es", max(lista))
elif opcion == "4":
    print("El valor minimo es", min(lista))



