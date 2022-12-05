# Упражнение 4.1
pizzas = ['pepperoni', 'bbq', 'margarita']

for pizza in pizzas:
    print(f'I would like to order {pizza.title()} pizza!')
print("I've ordered three pizzas!")

# Упражнение 4.11 и 4.12
friend_pizzas = pizzas[:]
pizzas.append('chicken_bbq')
friend_pizzas.append('teriyaki')
print('My favorite pizzas are:')

for pizza in pizzas:
    if pizza == 'bbq':
        print(pizza.upper())
    else:
        print(pizza.title())

print("My friend's favorite pizzas are:")

for pizza in friend_pizzas:
    if pizza == 'bbq':
        print(pizza.upper())
    else:
        print(pizza.title())
