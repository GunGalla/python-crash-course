# Упражнения 7.8 и 7.9

sandwich_orders = ['BMT', 'pastrami', 'chicken BBQ', 'pastrami', 'Tuna', 'pastrami', 'Melt']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    preparing = sandwich_orders.pop()
    print(f'We are currently making {preparing} sandwich.')
    finished_sandwiches.append(preparing)
print('We have made following sandwiches: ')
for sandwich in finished_sandwiches:
    print(sandwich)
