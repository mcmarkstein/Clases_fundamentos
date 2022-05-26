#Ejercicio 3
orders = []

while True:

    print('Farmacia - Opciones')
    print('(1) Agregar')
    print('(2) Listar')
    print('(3) Salir')

    option = input('>> ')
    if option == '3':
        break

    if option == '1':
        medicine = input('Nombre del medicamento: \n >>> ')
        lab = input('Lab del medicamento: \n >>> ')
        quantity = input('Quantity del medicamento: \n >>> ')

        item = {}
        item['medicamento'] = medicine
        item['laboratorio'] = lab
        item['cantidad'] = quantity

        if item in orders:
            print('Medicamento existente')
        else:
            orders.append(item)

    elif option == '2':
        print(orders)
    else:
        print('La opcion {option} no es valida')