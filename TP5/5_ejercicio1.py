#Ejercicio 1
shopping_cart = []

def agregar_producto(nombre_producto, cantidad):
    productos_dict = {}
    productos_dict['nombre_producto'] = nombre_producto
    productos_dict['cantidad'] = cantidad

    shopping_cart.append(productos_dict)

def ver_compra(shopping_cart):
    for producto_dict  in shopping_cart:
        print(f"Tenes {producto_dict['cantidad']} de {producto_dict['nombre_producto']}")

while True:
    print('(1) Agregar productos')      #Agregar
    print('(2) Comprar productos')      #Visualizar
    print('(3) Salir')

    option = input('>> ')

    if option == '1':
        print('Nombre del producto: ')
        nombre_producto = input('>> ')
        print('Cantidad: ')
        cantidad = input('>> ')
        agregar_producto(nombre_producto, cantidad)

    if option == '2':
        ver_compra(shopping_cart)

    if option == '3':
        break

    else:
        print("Opcion invalida")