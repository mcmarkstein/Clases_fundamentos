#Ejercicio 2

vehiculos = {
'moto':  10,
'auto': 20,
'camioneta': 25,
'camion': 60,
'camion con acoplado': 90,
'emmett brown': 200
}

def print_ticket(categoria):
    try:
        precio_vehiculo = vehiculos[categoria]
        print('Imprimiendo...')
        print(f' Vehiculo {categoria.upper()} tarifa: ${precio_vehiculo}')
    except KeyError:
        print(f'No se pudo encontrar la categoria {categoria}')

def user_menu():
    while True:
        print('1 - Moto')
        print('2 - Auot')
        print('3 - Camioneta')
        print('4 - Camion')
        print('5 - Camion con Acoplado')
        print('6 - Emmett Brown')
        opcion = input('>> ')

        if opcion  == '1':
            print_ticket('moto')
        if opcion  == '2':
            print_ticket('auto')
        if opcion  == '3':
            print_ticket('camioneta')
        if opcion  == '4':
            print_ticket('camion')
        if opcion  == '5':
            print_ticket('camion con acoplado')
        if opcion == '6':
            print_ticket('emmett brown')
        else:
            print('Opcion invalida')

user_menu()