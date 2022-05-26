#Ejercicio 1
usuario= {'nombre':'Melina',
          'apellido':'Markstein',
          'DNI': '43081331',
          'sucursal':'005'}
print(usuario)

for key, value in usuario.items():
    print(f'{key.title()}: {value.title()}')
print('--------------\n')

#Ejercicio 2
animals_list = ['gato', 'paloma', 'leon']
animals_tupl = ('gato', 'paloma', 'leon')   #No se puede modificar
animals_set = {'gato', 'paloma', 'leon' }   #No hay elemento repetidos
animals_dicc = {'animal1': 'tigre', 'animal2':'pez', 'animal3':'araña'}

animals_list.append('python')
animals_set.add('python')
animals_dicc['animal4']= 'python'
print(animals_list)
print(animals_set)
print(animals_dicc)
print('\n-------------\n')

#Ejercicio 4
polling_original = {'anonimo1': '6', 'anonimo2': '9', 'anonimo3': '5', 'anonimo4': 'x', 'anonimo5': 'x', 'anonimo6': '8', 'anonimo7': '3', 'anonimo8': '10', 'anonimo9': '4', 'anonimo10': '5', 'anonimo11': 'x', 'anonimo12': '2', 'anonimo13': '7', 'anonimo14': '5', 'anonimo15': '2', 'anonimo16': '8', 'anonimo17': '10'}

# Empleados que no contestaron la encuesta = x
polling_reply = {}
not_reply = 0

for poll, value in polling_original.items():
    if value == "x":
        not_reply += 1
    else:
        polling_reply[poll] = value
print(f"\nEmpleados que no contestaron: {not_reply}")
print(f"Nuevo diccionario con respuesta: {polling_reply}")

#sumar valores de encuestas y calcular porcentajes
reply_sum = 0
MAX_VALUE_PROPOUSAL = 10
for value in polling_reply.values():
    reply_sum += int(value)
print(f"Total de encuestas reply: {len(polling_reply)}")
print(f"Suma total de aceptacion: {reply_sum}")
print(f"Procentaje de aceptacion: {(reply_sum * 100) / (MAX_VALUE_PROPOUSAL * len(polling_reply))}")

value_list = []
for value in polling_reply.values():
    if value not in value_list:
        value_list.append(value)
print(f' Las notas fueron: {value_list}')

#Ejercicio 5
eeuu = {'country': 'Esatdos Unidos',
        'cities': ['New York', 'Miami'],
        'currency': 'dolar',
        'language': 'Ingles'}
costa_rica = {'country': 'Costa Rica',
        'cities': ['San Jose', 'Sanat Teresa'],
        'currency': 'CRC',
        'language': 'Español'}

countries = [eeuu, costa_rica]
suecia_ok= False
for country in countries:
    if country['country'] == 'Suecia':
        suecia_ok = True
print(f'Existe Suecia: {suecia_ok}')

sj_existe = False
for country in countries:
    for city in country['cities']:
        if city == 'San Jose':
            sj_existe = True
print(f'LA CIUDAD sAN joSE existe: {sj_existe}')

visit_cities = []
for country in countries:
    for city in country['cities']:
        visit_cities.append(city)
print(f'Las ciudades a visitar son {visit_cities}')

print(country.get('vacations', 'esta clave no existe')) #Existe la clave?



print(countries)

#Ejercicio 7
numbers=[]

for number in range(1, 101):
    number_dicc = {}
    number_dicc['number'] = number

    if number % 2 == 0:
        number_dicc['tyoe'] = 'par'
    else:
        number_dicc['tyoe'] = 'impar'
    numbers.append(number_dicc)
print(numbers)

# Ejercicio 6
customer_payments = ['23423', '58092', '75230', '72879', '82231', '35465', '30943', '12772']
cards_trx = [{'user_id': '35465', 'total_amount': 30000, 'payment_method': 'credit card', 'total_installments': 12,
              'current_installment': 7},
             {'user_id': '23423', 'total_amount': 19099, 'payment_method': 'credit card', 'total_installments': 12,
              'current_installment': 3},
             {'user_id': '82312', 'total_amount': 15500, 'payment_method': 'credit card', 'total_installments': 12,
              'current_installment': 4},
             {'user_id': '29332', 'total_amount': 90200, 'payment_method': 'credit card', 'total_installments': 6,
              'current_installment': 4},
             {'user_id': '82231', 'total_amount': 29000, 'payment_method': 'credit card', 'total_installments': 12,
              'current_installment': 9},
             {'user_id': '76289', 'total_amount': 42300, 'payment_method': 'credit card', 'total_installments': 12,
              'current_installment': 11},
             {'user_id': '58092', 'total_amount': 18900, 'payment_method': 'credit card', 'total_installments': 6,
              'current_installment': 1},
             {'user_id': '30943', 'total_amount': 13520, 'payment_method': 'debit card'},
             {'user_id': '75230', 'total_amount': 67000, 'payment_method': 'credit card', 'total_installments': 6,
              'current_installment': 4},
             {'user_id': '20582', 'total_amount': 21500, 'payment_method': 'credit card', 'total_installments': 12,
              'current_installment': 6},
             {'user_id': '10943', 'total_amount': 5200, 'payment_method': 'debit card'},
             {'user_id': '29002', 'total_amount': 9000, 'payment_method': 'credit card', 'total_installments': 12,
              'current_installment': 11},
             {'user_id': '92389', 'total_amount': 39200, 'payment_method': 'debit card'},
             {'user_id': '12772', 'total_amount': 65700, 'payment_method': 'credit card', 'total_installments': 12,
              'current_installment': 10},
             {'user_id': '72879', 'total_amount': 7300, 'payment_method': 'credit card', 'total_installments': 6,
              'current_installment': 5},
             {'user_id': '83489', 'total_amount': 44000, 'payment_method': 'debit card'}, ]

for customer in customer_payments:
    for card in cards_trx:
        if customer == card['user_id']:
            if card['payment_method'] == 'credit card':
                card['current_installment'] += 1
print(cards_trx)

print('------------\n')

for card in cards_trx:
    if card['payment_method'] == 'credit card':
        card['remaining_installment'] = (card['total_installments'] - card['current_installment'])
        print('Al usuario ' + str(card['user_id']) + ', le quedan: ' + str(card['remaining_installment']) + ' cuotas')

print('---------------\n')

completed_payment = []
for card in cards_trx:
    if card['payment_method'] == 'credit card':
        if card['remaining_installment'] == 0:
            completed_payment.append(card['user_id'])

print(f'Los que completaron las cuotas fueron: {completed_payment}')