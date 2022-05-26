#from shapes import *
from shapes import Cubo, PrismaRectangular, Esfera

cubo = Cubo(4)


def user_menu():

    print('Que figuras imprimir:')
    print('1) Esfera')
    print('2) Cubo')
    print('3) Prisma rectangular')

    opcion = input('>> ')

    if opcion == '1':
        radio = input('>> ')
        esfera  =Esfera(radio)
        print(f"Imprimiendo {esfera.nombre} por favor espere")
        print(esfera.print_propiedades())

    elif opcion == '2':
        lado = input('>> ')
        cubo = Cubo(lado)
        print(f"Imprimiendo {cubo.nombre} por favor espere").
        print(cubo.print_propiedades())

    elif opcion == '3':
        radio = input('>> ')
        prisma_rectangular = PrismaRectangular()

    else:
        print('Opcion ivnalida')

user_menu()