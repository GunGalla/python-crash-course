# Упражнения 5.8 и 5.9

names = ['Yaroslav', 'Evgenia', 'admin', 'Vladimir', 'Tom']

if names:
    for name in names:
        if name == 'admin':
            print(f'Hello {name}, would you like to see a status report?')
        else:
            print(f'Hello {name}, thank you for logging in again!')
else:
    print('We need to find some users...')
