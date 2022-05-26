class Lampara:
    def __int__(self, fabricante, cod_fabricante, modelo, amparaje, potencia, diametro, efi_energetica, precio):
        self.__fabricante = fabricante
        self.__cod_fabricante = cod_fabricante
        self.modelo = modelo
        self.amparaje = amparaje
        self.potencia = potencia
        self.diametro = diametro
        self.efi_energetica = efi_energetica
        self.precio = precio

    def dar_fab_mod_diam(self):
        return f"\n\t Fabricante: {self.__fabricante}" \
               f"\n\t Codigo de fabricante: {self.__cod_fabricante}" \
               f"\n\t Modelo: {self.modelo}" \
               f"\n\t Diametro: {self.diametro}" \


    def dar_precio(self):
        return f"\n\t Precio: {self.precio}"

    def dar_caracteristicas(self):
        return f"\n\t Caracterisitcas de consumo:" \
               f"\n\t\t Amparaje: {self.amparaje}" \
               f"\n\t\t Potencia: {self.potencia}" \
               f"\n\t\t Eficiencia energetica: {self.efi_energetica}" \


    def ajustar_precios(self):
        porcentaje_de_aumento = int(input("Porcentaje que quiere aumentar el precio: >>"))
        self.precio += (self.precio * porcentaje_de_aumento)
        return f"El precio de la lampara {self.modelo} es: {self.precio}"


class NPN731 (Lampara):
    def __init__(self, fabricante, cod_fabricante, modelo, amparaje, potencia, diametro, efi_energetica, precio):
        super().__int__(fabricante, cod_fabricante, modelo, amparaje, potencia, diametro, efi_energetica, precio)
        self.__certificado_iso = "ISO 9023"

    def dar_certificado_iso(self):
        return f"El certificado ISO es: {self.__certificado_iso}"


class NPN923 (Lampara):
    def __init__(self, fabricante, cod_fabricante, modelo, amparaje, potencia, diametro, efi_energetica, precio):
        super().__int__(fabricante, cod_fabricante, modelo, amparaje, potencia, diametro, efi_energetica, precio)


class NPN328 (Lampara):
    def __init__(self, fabricante, cod_fabricante, modelo, amparaje, potencia, diametro, efi_energetica, precio):
        super().__int__(fabricante, cod_fabricante, modelo, amparaje, potencia, diametro, efi_energetica, precio)


class NPN021 (Lampara):
    def __init__(self, fabricante, cod_fabricante, modelo, amparaje, potencia, diametro, efi_energetica, precio):
        super().__int__(fabricante, cod_fabricante, modelo, amparaje, potencia, diametro, efi_energetica, precio)
