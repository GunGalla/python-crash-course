"""Write text in the file."""
# Упражнение 10.3

name = 'guest.txt'

with open(name, 'a') as file:
    file.write(input('What is your name? '))

# Упражнение 10.4

name_2 = 'guest_book.txt'

counter = 0
while counter < 5:
    with open(name_2, 'a') as file:
        file.write(f"{input('What is your name? ')}\n")
        counter += 1
