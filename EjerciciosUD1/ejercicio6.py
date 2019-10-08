class Criptografo:

    @staticmethod
    def encriptar(texto):
        textoEncriptado = ""
        for car in texto:
            textoEncriptado += chr(ord(car)+1)
        return textoEncriptado

    @staticmethod
    def desencriptar(texto):
        textoDesencriptado = ""
        for car in texto:
            textoDesencriptado += chr(ord(car) - 1)
        return textoDesencriptado


cripto = Criptografo()
print(cripto.encriptar("hola"))
print(cripto.desencriptar(cripto.encriptar("hola")))
