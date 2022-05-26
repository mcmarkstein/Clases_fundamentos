#Ejercicio 5
# Hay algo que no puedo resolver con las primeras dos opciones de acreditar,
# me sale un error de tipo de datos.


usuario_1 = {'user_id': 'melina', 'password': '123',
     'saving_bank' : {'account_num': 'CA-000-111', 'amount' : 100},
     'current_bank': {'account_num' : 'CC-000-111', 'amount': 200},
    'last_trxs': [10.0, 65.5]}
usuario_2 ={'user_id': 'maria', 'password': '456',
     'saving_bank' : {'account_num': 'CA-000-111', 'amount' : 100},
     'current_bank': {'account_num' : 'CC-000-111', 'amount': 200},
    'last_trxs': [10.0, 65.5]}
usuario_3 = {'user_id': 'melina', 'password': '789',
     'saving_bank' : {'account_num': 'CA-000-111', 'amount' : 100},
     'current_bank': {'account_num' : 'CC-000-111', 'amount': 200},
    'last_trxs': [10.0, 65.5]}
accounts = [usuario_1, usuario_2, usuario_3]

def acreditar_ca(usuario_activo):
    print('Monto a acreditar en CA ')
    cantidad = ingresar_cantidad()
    usuario_activo['saving_bank']['amount'] += cantidad
    usuario_activo['last_trxs'].append(cantidad)
    print('++ CA actualizada ++')
    print('----------------------------')

def acreditar_cc(usuario_activo):
    print('Monto a acreditar en CC ')
    cantidad = ingresar_cantidad()
    usuario_activo['cuerrent_bank']['amount'] += cantidad
    usuario_activo['last_trxs'].append(cantidad)
    print('++ CC actualizada ++')
    print('----------------------------')

def ingresar_cantidad():
    cantidad = 0.0
    while True:
        try:
            print('>> La$ ')
            cantidad = float(input())
            break
        except Exception:
            print('Debe ingresar numeros, no letras')

def consultar_saldo_ca(usuario_activo):
    account_num = usuario_activo['saving_bank']['account_num']
    amount = usuario_activo['saving_bank']['amount']
    print('++Resumen de CA ++')
    print('Número de la cuenta ', account_num)
    print('Saldo: La$ ', amount)
    print('----------------------------')


def consultar_saldo_cc(usuario_activo):
    account_num = usuario_activo['current_bank']['account_num']
    amount = usuario_activo['current_bank']['amount']
    print('++Resumen de CC ++')
    print('Numero de la cuenta ', account_num)
    print('Saldo: La$ ', amount)
    print('----------------------------')

def consultar_trx(usuario_activo):
    print('Ultimas transacciones realizadas: ')
    trxs = usuario_activo['last_trxs']
    for t in trxs:
        print('\t La$ ',  t)
    print('-------------------------')

def salir(user_id):
    print('Gracias ', user_id, ' por utilizar nuestro sistema ')
    user = ''
    password = ''
    cuenta = {}
    print('Saliendo....')

ACRED_CA = 1
ACRED_CC = 2
SALDO_CA = 3
SALDO_CC = 4
CONS_TRX = 5
SALIR = 6

def operaciones_disponibles():
    opcion= 0
    while opcion not in [ACRED_CA, ACRED_CC, SALDO_CA, SALDO_CC, CONS_TRX,SALIR]:
        print('Operaciones disponibles')
        print('\t (1) Acreditar en CA')
        print('\t (2) Acreditar en CC')
        print('\t (3) Consultar saldo CA')
        print('\t (4) Consultar saldo CC')
        print('\t (5) Consultar TRX')
        print('\t (6) Salir')
        opcion = int(input('>> '))
    return opcion



while True:

    print('\t\t @@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('\t\t @@   Banco Digital LA   @@')
    print('\t\t @@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('\n Ingrese su ID')
    user_id = input('>> ')
    print('Ingrese su clave')
    password = input('>> ')

    for account in accounts:
        if account['user_id'] == user_id and account['password'] == password:
            usuario_activo = account
            if usuario_activo:
                while usuario_activo != SALIR:
                    opcion = operaciones_disponibles()
                    if opcion == ACRED_CA:
                        acreditar_ca(usuario_activo)
                    elif opcion == ACRED_CC:
                        acreditar_cc(usuario_activo)
                    elif opcion == SALDO_CA:
                        consultar_saldo_ca(usuario_activo)
                    elif opcion == SALDO_CC:
                        consultar_saldo_cc(usuario_activo)
                    elif opcion == CONS_TRX:
                        consultar_trx(usuario_activo)
                    elif opcion == SALIR:
                        salir(user_id)
                        break
        else:
            print('\n Procesando...')
            print('\n Permiso denegado - Usuario invalido')

