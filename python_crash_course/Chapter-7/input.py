# Упражнение 7.1

car = input('Which car do you want to rent? ')
print(f'Let me see if I can find {car}.')

# Упражнение 7.2

reservation_amount = int(input('How many places do you need? '))
if reservation_amount > 8:
    print('Sorry, but you have to wait until table become available.')
else:
    print('Your reservation is accepted!')

# Упражнение 7.3

number = int(input('Tell me the number and I say you if it multiple of ten or not. '))
if number % 10 == 0:
    print('Your number is multiple of ten!')
else:
    print('Your number is not multiple of ten :(')
