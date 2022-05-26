#Ejercicio warm up
class Ballena:
    def __init__(self, nombre, edad, sexo, peso, mamifero):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.mamifero = mamifero

    def nadar(self):
        return f"{self.nombre} esta nadando"
    def saltar(self):
        return f"{self.nombre} esta saltando"
    def alimentar(self):
        return f"{self.nombre} esta comiendo"
    def descansar(self):
        return f"{self.nombre} esta descansando"

    def estado(self):
        return f"\n Nombre:{self.nombre}" \
               f"\n Edad: {self.edad}" \
               f"\n Sexo: {self.sexo}" \
               f"\n Peso: {self.peso}" \
               f"\n Es mamifero: {'SI' if self.mamifero else 'NO'}"

willy = Ballena('Willy', 9, 'M', 2000, True)
willy_clon = Ballena('Willy', 9, 'M', 2000, True)

print(f' Mi ballena es: {willy}')
print(willy.nadar())
print(willy.saltar())
print(willy.alimentar())
print(willy.descansar())

print(willy.estado())

print(willy == willy_clon)