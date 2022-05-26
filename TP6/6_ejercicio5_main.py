from ejercicio5 import Serie, Pelicula
CATEGORIA_ACCION = "Accion"
CATEGORIA_ANIME = "Anime"
CATEGORIA_COMEDIA = "Comedia"
CATEGORIA_DOCUMENTAL = "Docuemntal"
CATEGORIA_CIENCIA_FICCION = "Ciencia Ficcion"
CATEGORIA_ROMANCE = "Romance"

CALIFICACION_APT = "Apta para todo publico"
CALIFICACION_MAS_13 = "Para mayores de 13 años"
CALIFICACION_MAS_16 = "Para mayores de 16 años"
CALIFICACION_MAS_18 = "Para mayores de 18 años"

glee = Serie(CATEGORIA_COMEDIA, "Glee", "Los integrantes...", 2012, "Ryan Murphy",CALIFICACION_MAS_13, 6)
divergente = Pelicula(CATEGORIA_ACCION, "Divergente", "Nacio con..", 2014, "Neil Burger", CALIFICACION_MAS_13, "2 hs 19 min")

print(glee)
print('\n-----------------\n')
print(glee.agregar_temporadas())
print('\n-----------------')
print(glee)
print('\n-----------------')
print(divergente)

