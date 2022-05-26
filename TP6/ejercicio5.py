class Video:
    def __int__(self, categoria, nombre, descripcion, fecha_publicacion, director, calificacion):
        self.categoria = categoria
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_publicacion = fecha_publicacion
        self.director = director
        self.calificacion = calificacion

    def __str__(self):
        return f"\n\tNombre: {self.nombre}" \
                f"\n\tTipo: {self.tipo}"\
                f"\n\tCategoria: {self.categoria}" \
                f"\n\tDescripcion: {self.descripcion}" \
                f"\n\tFecha de publicacion: {self.fecha_publicacion}" \
                f"\n\tDirector: {self.director}" \
                f"\n\tCalificacion: {self.calificacion}" \



class Serie (Video):

    def __init__(self, categoria, nombre, descripcion, fecha_publicacion, director, calificacion, cant_temporadas):
        super().__int__(categoria, nombre, descripcion, fecha_publicacion, director, calificacion)
        self.tipo = "Serie"
        self.cant_temporadas = cant_temporadas

    def agregar_temporadas(self):
        nueva_cant_temporadas = input("Agregue la nueva cantidad de temporadas: >>")
        self.cant_temporadas = nueva_cant_temporadas
        return f"\n\tLa cantidad de temporadas es: {self.cant_temporadas}"

    def __str__(self):
        agrego = f"\n\tCantidad de temporadas: {self.cant_temporadas}"
        return super().__str__() + agrego


class Pelicula (Video):

    def __init__(self, categoria, nombre, descripcion, fecha_publicacion, director, calificacion, tiempo_reproduccion):
        super().__int__(categoria, nombre, descripcion, fecha_publicacion, director, calificacion)
        self.tipo = "Pelicula"
        self.tiempo_reproduccion = tiempo_reproduccion

    def __str__(self):
        agrego = f"\n\tTiempo total de reproduccion: {self.tiempo_reproduccion}"
        return super().__str__() + agrego
