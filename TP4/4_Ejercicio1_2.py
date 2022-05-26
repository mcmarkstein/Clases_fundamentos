#Eejrcicio 1 y 2
print('Welcome to Disney World!')
print('----------\n')

while True:
    print('Buy a ticket, please enter your age:')
    age = input('>> ')
    if age == 'quit':
        break
    try:
        if int(age) < 5:
            print('Free Ticket')
        elif int(age)>= 5 and int(age)<9:
            print('Ticket price: $15')
        elif int(age)>= 9 and int(age)<14:
            print('Ticket price: $23')
        elif int(age)>= 14 and int(age)<100:
            print('Ticket price: $35')
        else:
            print('You are awesome!! Free ticket for you')
    except ValueError:
        print("You cna't enter letters. Just numbers greater than 0")

print('PROGRAMA FINALIZADO')