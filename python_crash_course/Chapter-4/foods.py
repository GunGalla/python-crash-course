# Упражнение 4.10
foods = ['pizza', 'burger', 'ice-cream', 'grill', 'steak']

print('The first three items in the list are:')
for food in foods[:3]:
    print(food)

print('Three items from the middle of the list are:')
for food in foods[1:4]:
    print(food)

print('The last three items in the list are:')
for food in foods[-3:]:
    print(food)
