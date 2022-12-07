# Упражнение 7.5

age = int(input('Please, enter your current age: '))

if age < 3:
    print('Your ticket is free!')
elif 3 <= age <= 12:
    print('Your ticket cost is 10$!')
else:
    print('Your ticket cost is 15$!')
