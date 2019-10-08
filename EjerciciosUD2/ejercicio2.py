import csv


class gestionarCSV:

    menu = """
    ¿Qué desea hacer?
        1.- Generar fichero csv de olimpiadas
        2.- Buscar deportista
        3.- Buscar deportistas por deporte y olimpiada
        4.- Añadir deportista
        5.- Salir
        """

    def generarCSV(self):
        with open('athlete_events.csv') as lectura:
            reader = csv.DictReader(lectura)
            with open('olimpiadas.csv', 'w+') as escritura:
                fieldnames = ['Games', 'Year', 'Season', 'City']
                writer = csv.DictWriter(escritura, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    writer.writerow({'Games': row["Games"],
                                     "Year": row["Year"],
                                     "Season": row["Season"],
                                     "City": row["City"]})
        print("Archivo creado")

    def buscarDeportista(self):
        cadena = input("¿Qué nombre desea buscar?")
        with open('athlete_events.csv', 'w+') as lectura:
            reader = csv.DictReader(lectura)
            deportistasCumplenPatron = []
            deportistasMostrados = []
            for row in reader:
                if cadena in row["Name"]:
                    deportistasCumplenPatron.append(row)
            if deportistasCumplenPatron.__len__() > 0:
                for d in deportistasCumplenPatron:
                    if d.get("Name") not in deportistasMostrados:
                        deportistasMostrados.append(d.get("Name"))
                for d in deportistasMostrados:
                    print("\n"+d)
                    for info in deportistasCumplenPatron:
                        if d == info["Name"]:
                            print("\tJuego: "+info["Games"] +
                                  "\t Evento: "+info["Event"] +
                                  "\t Sexo: "+info["Sex"] +
                                  "\t Edad: "+info["Age"] +
                                  "\t Altura: "+info["Height"] +
                                  "\t Peso: "+info["Weight"])
            else:
                print("Ningun resultado encontrado")




    def buscarDeportistaPorDeporteOlimpiada(self):
        sport = input("¿Qué deporte busca?")
        year = input("¿De qué año?")
        season = input("¿De qué estación? Summer o Winter")
        deportistas = []
        with open('athlete_events.csv') as lectura:
            reader = csv.DictReader(lectura)
            for row in reader:
                if sport == row["Sport"] and year == row["Year"] and season == row["Season"]:
                    deportistas.append(row)
            if deportistas.__len__() > 0:
                print(deportistas[0].get("Games")+" "+deportistas[0].get("City")+" "+deportistas[0].get("Sport"))
                for d in deportistas:
                    print("\tNombre: " + d["Name"] +
                          "\t Evento: " + d["Event"] +
                          "\t Medalla: " + d["Medal"])
            else:
                print("Ningun deportista encontrado")

    def aniadirDeportista(self):
        nombre = input("Introduce el nombre")
        sexo = input("Introduce el sexo")
        edad = input("Introduce la edad")
        height = input("Introduce la altura")
        weight = input("Introduce el peso")
        team = input("Introduce el equipo")
        noc = input("Introduce el NOC")
        games = input("Introduce los juegos")
        year = input("Introduce el año")
        season = input("Introduce la estacion")
        city = input("Introduce la ciudad")
        sport = input("Introduce el deporte")
        event = input("Introduce el evento")
        medal = input("Introduce la medalla")
        with open('athlete_events.csv', 'w+') as escritura:
            fieldnames = ["ID", "Name", "Sex", "Age", "Height",
                          "Weight", "Team", "NOC", "Games",
                          "Year", "Season", "City", "Sport", "Event", "Medal"]
            writer = csv.DictWriter(escritura, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({"ID": 135572,
                             "Name": nombre,
                             "Sex": sexo,
                             "Age": edad,
                             "Height": height,
                             "Weight": weight,
                             "Team": team,
                             "NOC": noc,
                             "Games": games,
                             "Year": year,
                             "Season": season,
                             "City": city,
                             "Sport": sport,
                             "Event": event,
                             "Medal": medal})


gestor = gestionarCSV()
options = {"1": gestor.generarCSV,
           "2": gestor.buscarDeportista,
           "3": gestor.buscarDeportistaPorDeporteOlimpiada,
           "4": gestor.aniadirDeportista
           }
opcion = input(gestor.menu)
while opcion != "5":
    try:
        options[opcion]()
    except KeyError:
        print("Elige una opcion del menu")
    opcion = input(gestor.menu)






