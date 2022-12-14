"""Calculator of sum."""
# Упражнения 10.6 и 10.7

while True:
    print('Please, enter two numbers and I tell your their sum.')
    print("Enter 'q' any time to stop.")
    num_1 = input('First number: ')
    if num_1 == 'q':
        print('Program finished.')
        break
    num_2 = input('Second number: ')
    if num_2 == 'q':
        print('Program finished.')
        break
    try:
        result = int(num_1) + int(num_2)
    except ValueError:
        print('You must enter an integer!')
    else:
        print(f'The result is: {result}')
