class Esfera:
    def __init__(self, radio):
        self.nombre = 'Esfera'
        self.radio = radio

    def dar_nombre(self):
        return f" El nombre es: {self.nombre}"

    def dar_radio(self):
        return f"El radio es: {self.radio}"

    def print_propiedades(self):
        return f"{self.nombre} con propiedades radio: {self.radio}"

class Cubo:
    def __init__(self, lado):
        self.nombre = 'Cubo'
        self.lado = lado

    def dar_nombre(self):
        return f" El nombre es: {self.nombre}"

    def dar_lado(self):
        return f"El lado es: {self.lado}"

    def print_propiedades(self):
        return f"{self.nombre} con propiedades lado: {self.lado}"


class PrismaRectangular:
    def __init__(self, base, altura, profundidad):
        self.nombre = 'Prisma rectangular'
        self.base = base
        self.altura = altura
        self.profundidad = profundidad

    def dar_nombre(self):
        return f" El nombre es: {self.nombre}"

    def dar_dimensiones(self):
        return [self.base, self.altura, self.profundidad]
