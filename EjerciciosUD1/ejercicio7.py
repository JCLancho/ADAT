from random import randint


class Persona:

    sexoDefault = 'H'

    def __init__(self, nombre="", edad=0, sexo=sexoDefault, peso=0, altura=0.0):
        self.__dni = self.__generaDNI()
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    nombre = property(getNombre, setNombre)

    def getEdad(self):
        return self.__edad

    def setEdad(self, edad):
        self.__edad = edad

    edad = property(getEdad, setEdad)

    def getSexo(self):
        return self.__sexo

    def setSexo(self, sexo):
        self.__sexo = sexo

    sexo = property(getSexo, setSexo)

    def getPeso(self):
        return self.__peso

    def setPeso(self, peso):
        self.__peso = peso

    peso = property(getPeso, setPeso)

    def getAltura(self):
        return self.__altura

    def setAltura(self, altura):
        self.__altura = altura

    altura = property(getAltura, setAltura)

    def calcularIMC(self):
        indice = self.getPeso() / (self.getAltura() * self.getAltura())
        bajoPeso = -1
        pesoIdeal = 0
        sobrePeso = 1
        if indice < 20:
            return bajoPeso
        elif 20 <= indice <= 25:
            return pesoIdeal
        else:
            return sobrePeso

    def esMayorDeEdad(self):
        if self.getEdad() > 17:
            return True
        else:
            return False

    def toString(self):
        return """Objeto %s:
            DNI: %s
            Nombre: %s
            Edad: %g
            Sexo: %s
            Peso: %g
            Altura: %g""" % (self.__class__.__name__, self.__dni, self.nombre, self.edad, self.sexo, self.peso, self.altura)

    @staticmethod
    def __generaDNI():
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        digitos = ""
        for contador in range(8):
            digitos += randint(0, 9).__str__()
        letra = letras[int(digitos) % 23]
        return digitos + "-" + letra


persona1 = Persona("Carlos", 27, 'H', 70, 1.75)
persona2 = Persona("Rodrigo", 24, 'H', 65, 1.70)
persona3 = Persona("Ander", 35,  altura=1.80, peso=75)

print(persona1.toString())
print(persona1.calcularIMC())
print(persona1.esMayorDeEdad())

print(persona2.toString())
print(persona2.calcularIMC())
print(persona2.esMayorDeEdad())

print(persona3.toString())
print(persona3.calcularIMC())
print(persona3.esMayorDeEdad())
