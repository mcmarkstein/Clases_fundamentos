#Ejercicio 4
receta1 = {}
receta2 = {}
receta3 = {}
recetas_favoritas=[receta1, receta2, receta3]

ingredientes = []

def recipe_recommender():
    recetas_recomendadas = []
    for input_ingrediente in ingredeintes:
        for receta_dict in recetas:
            for ingredientes_receta in receta_dict['ingredientes']:
                if input_ingrediente == ingredientes_receta:
                    if not(receta_dict in recetas_recomendadas):
                        recetas_recomendadas.append(receta_dict)

    return recetas_recomendadas

def print_recetas(recetas):
    for receta in recetas:
        print(f"Receta: {receta['receta']}")
        for ingrediente in receta['ingredientes']:
            print('\t {ingrediente} ')

def menu_principal():

    print('Que cocino hoy?')

    while True:

        print('1 - Agregar ingrediente')
        print('2 - Buscar receta')
        print('3 - A cocinar...')
        opcion = input('>> ')

        if opcion == '1':
            print('Ingresar ingredeinte: ')
            ingrediente = input('>> ')
            ingredientes.append(ingrediente)

        elif opcion == '2':
            if len(ingredientes) >=2:
                receta = recipe_recommender()
                print_recetas(receta)
            else:
                print('Debes tener por lo menos 2 ingredientes')

        elif opcion == '3':
            break

        else:
            print('Opcion invalida')

menu_principal()