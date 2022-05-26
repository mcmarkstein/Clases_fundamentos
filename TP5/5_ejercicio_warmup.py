#Ejercicio warming up
sportsmen = []

def save_sportsmen(sportsman, sport):
    sportsman_dict = {}
    sportsman_dict['sportsman'] = sportsman
    sportsman_dict['sport'] = sport

    sportsmen.append(sportsman_dict)

def print_sportsmen(lista_deportistas):
    for deportista_dict  in lista_deportistas:
        print(f"El/La deportista {deportista_dict['sportsman']}, juega {deportista_dict['sport']}")

while True:
    print('(1) agregar deportista')
    print('(2) Ver deposrtistas')

    option = input('>> ')

    if option == '1':
        print('Nombre del deportista: ')
        sportsman = input('>> ')
        print('Deporta que pratcica')
        sport = input('>> ')

        save_sportsmen(sportsman, sport)

    if option == '2':
        print_sportsmen(sportsmen)

    else:
        print("Opcion invalida")