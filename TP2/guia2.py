#Ejercicio 1
bitocin = '4.483.127'
ethereum = '308.416'
litecoin = "12.080"
print('Bitcoin= ', bitocin, ', Etherum: ', ethereum, ', Litecoin =', litecoin)

#Ejercicio 2

#Ejecicio 3
nombre = 'ERNESTO    '
apellido = 'caldini'
email= 'Ecaldini@gmail.com'
print('nombre: ', nombre.lower(), ', apellido: ', apellido.lower(), ', email: ', email.lower())
print('nombre: ', nombre.rstrip().title(), ', apellido: ', apellido.title(), ', email: ', email.lower())

#Ejetrcicio 4
solicita_importar=300
valor_usd=1500
dolar = 200
comision = 0.03
sellado = 15000
total = solicita_importar*valor_usd*dolar
total_con_comisionysellado = total + sellado + total*comision
cantidad_de_socios = 5
print('El totoal es: ',total_con_comisionysellado)
print('Cada uno de los 5 socios gana: ', total*comision/cantidad_de_socios)

#Ejercicio 5
guests = ['ernest', 'martin andrés', 'sofia', 'lucia', 'jose maría', 'abril']
for guest in guests:
    print(guest.title())
guests_formated=[]
for guest in guests:
    guests_formated.append(guest.title())
print(guests_formated)


#Ejercicio 6
new_guests = ['martina', 'josefina isabel', 'tomás']
guests_complete = guests+ new_guests
for guest in guests_complete:
    print(guest.title())
    print()
complete_formated =  []
for guest in guests_complete:
    complete_formated.append(guest.title())
print(complete_formated)

guest_removed = complete_formated.pop()
print(f'Se elimino a: {guest_removed}')
print(complete_formated)

#Ejercicio 8
precios =[117.12, 121.19, 128.37, 135.70, 139.47, 151.80, 157.95, 161.80, 166.20, 174.51, 179.68, 188.96, 200.89, 211.89, 225.99, 232.50, 249.12, 262.69, 177.67, 187.19, 193.81, 209.57, 216.73, 227.52, 239.24, 250.22, 256.04, 269.91, 282.93, 12.37, 92.17, 65.37, 73.26, 43.26, 78.26]
precios_aumentados = []
for precio in precios:
    nuevo_precio =  precio+(0.07*precio)
    precios_aumentados.append(round(nuevo_precio, 2))
print(precios_aumentados)

#Ejercicio 9
encuestas = [True, False, True, True, True, False, True, False, True, True,
True, False, False, True, True, True, True, False, True, True,
True, False, True, True, False, True, True, False, True, False,
True, True, True, False, True, True, True, False, True, False,
True, True, True, False, False, True, True, True, True, False,
True, True, True, False, True, True, False, True, True, False,
True, False, True, True]
ok = 0
ko = 0
for encuesta in encuestas:
    if encuesta:
        ok+=1
    else:
        ko+=1
print(f'Gusto: {ok}')
print(f'No gusto: {ko}')

ok_per = int(44/len(encuestas)*100)
ko_per = int(20/len(encuestas)*100)
if ok_per > 65:
    print('Producto exitoso')
else:
    print('Aun hay ucho que mejorar el producto')

#Ejercicio 10
supermercado = ['té', 'café', 'arroz', 'harina 000', 'lata de tomate', 'jabón', 'queso pategras', 'leche', 'levadura', 'desodorante', 'detergente', 'agua con gas', 'trapo de piso', 'lavandina', 'aceite de oliva', 'vinagre', 'mayonesa', 'ketchup', 'galletas de arroz']
producto= 'leche'
if producto in supermercado:
    print('Porducto en existencia:' + producto)
else:
    print('El proveedor no cuenta con el producto: ' + producto)

'''
Finalmente sustituir el bloque “else” por la palabra clave “not”. Usar comentario para
comentar el bloque “else”. ????
'''
'''''
if producto in supermercado:
    print('Porducto en existencia:' + producto)
not: #????????????
    print('El proveedor no cuenta con el producto: ' + producto)
'''''

#Ejejrcicio 11
lista_usuarios = [ 'mueslicie', 'sanero', 'robedrock', 'admin', 'derivero', 'posloth', 'claypo', 'locustpo', 'mostter']
user_access_denied = ['marmeant', 'gruntmar', 'tokcie', 'ciebank']
ingresante = 'marmeant'
mayus_ingresante = ingresante.title()
if ingresante in user_access_denied:
    print(f'User: {mayus_ingresante} access denied')
elif ingresante == 'admin':
    print('Bienvenido Administrador, en que lo puedo ayudar')
else:
    print(f'Bienvenido estimado {mayus_ingresante}, le desemaos un buen dia.')

#EJERCICIO 12
students = [37128693, 38346828, 48577851, 23923908, 23747794, 46033685, 28372488, 33143443,
38122921, 38915457, 24807285, 35759559, 21061055, 33613272, 24082600, 26477319,
46655903, 46988530, 25145603, 35368988, 25393784, 21295674, 48348316, 31247247,
28498292, 37538741, 21332845, 27557703, 24435687, 38794110, 44518399, 34178717,
45788239, 36998322, 32098132, 22185788, 25030083, 21256524, 34592517, 41755997,
37570846, 30401721, 34832996, 47330519, 34380715, 42724546, 26615771, 23171192,
42223891, 40210778, 33530381, 20478110, 20753240, 28187999, 27785500, 37236996,
22981717, 27744330, 44855039, 36552090, 36824210, 39684157, 26469844, 45037525,
25916934, 41595563, 23571241, 30552911, 40100736, 36047292, 46818813, 36680587,
36107300, 41367347]
student_marks = [15, 19, 19, 9, 6, 12, 20, 3, 1, 15, 10, 16, 3, 25, 18, 13, 24, 30, 7, 28, 20, 25, 28, 10, 2, 1,
18, 20, 3, 3, 19, 12, 11, 8, 24, 27, 15, 15, 19, 0, 27, 8, 29, 5, 1, 12, 8, 17, 19, 0, 0, 18, 15,
23, 22, 2, 24, 6, 10, 28, 18, 3, 15, 6, 26, 0, 21, 14, 24, 13, 10, 17, 16, 2]

print('----------\n')
dni = 48577851      #Aca se coloca el dni del cual se quiere encontrar la nota
if dni in students:
    indice_students = students.index(dni)
    according_mark = student_marks[indice_students]
    print(f'La nota del DNI: {dni} es: {according_mark}')
else:
    print(f'No se ha encontrado el DNI {dni}')


print('---------------\n')
cat_avanzado = []
cat_intermedio_alto = []
cat_intermedio_bajo = []
cat_basico = []
cat_por_debajo_de_basico = []
for mark in student_marks:
    if mark >=25 and mark<=30:
        cat_avanzado.append(mark)
    if mark >=20 and mark<=24:
        cat_intermedio_alto.append(mark)
    if mark >=16 and mark<=19:
        cat_intermedio_bajo.append(mark)
    if mark >=10 and mark<=15:
        cat_basico.append(mark)
    else:
        cat_por_debajo_de_basico.append(mark)
print(f'Las notas en la categoria Avanzado son: {cat_avanzado},  \nEl total de notas es:  {len(cat_avanzado)}')
print(f'Las notas en la catgeoria Intermedio alto son: {cat_intermedio_alto},  \nEl total de notas es:  {len(cat_intermedio_alto)}')
print(f'Las notas en la catgeoria Intermedio bajo son: {cat_intermedio_bajo},  \nEl total de notas es:  {len(cat_intermedio_bajo)}')
print(f'Las notas en la categroia basico son: {cat_basico},  \nEl total de notas es:  {len(cat_basico)}')
print(f'Las notas en la categoria Por debajo del basico son: {cat_por_debajo_de_basico},  \nEl total de notas es:  {len(cat_por_debajo_de_basico)}')

print('-------------\n')
total_de_alumnos = len(students)
print(f'El total de estudiantes que se presento a rendir es de: {total_de_alumnos} alumnos')
