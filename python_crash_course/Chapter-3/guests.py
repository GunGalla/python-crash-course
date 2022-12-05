# Упражнение 3.4
guests = ['Nikonor', 'Alexey', 'Svetlana', 'Tamara']

print(f'I will be glad to invite you to have a dinner, {guests[0]}!')

print(f'I will be glad to invite you to have a dinner, {guests[1]}!')

print(f'I will be glad to invite you to have a dinner, {guests[2]}!')

print(f'I will be glad to invite you to have a dinner, {guests[3]}!')

print(f"Unfortunately, {guests[1]}, won't be able to come :(")

# Упражнение 3.5
guests[1] = 'Evgeniia'

print(f'I will be glad to invite you to have a dinner, {guests[0]}!')

print(f'I will be glad to invite you to have a dinner, {guests[1]}!')

print(f'I will be glad to invite you to have a dinner, {guests[2]}!')

print(f'I will be glad to invite you to have a dinner, {guests[3]}!')

#  Упражнение 3.6
print("I've decided to invite additional people")

guests.insert(0, 'Valentina')

guests.insert(2, 'Kristina')

guests.append('Pavel')

print(f'I will be glad to invite you to have a dinner, {guests[0]}!')

print(f'I will be glad to invite you to have a dinner, {guests[1]}!')

print(f'I will be glad to invite you to have a dinner, {guests[2]}!')

print(f'I will be glad to invite you to have a dinner, {guests[3]}!')

print(f'I will be glad to invite you to have a dinner, {guests[4]}!')

print(f'I will be glad to invite you to have a dinner, {guests[5]}!')

print(f'I will be glad to invite you to have a dinner, {guests[6]}!')

# Упражнение 3.9
print(f'I have invited {len(guests)} guests.')

# Упражнение 3.7
print('Sorry for inconvenience, but I can invite only two people :(')

feel_sorry = guests.pop()

print(f'I am really sorry to decline my invitation, {feel_sorry}')

feel_sorry = guests.pop()

print(f'I am really sorry to decline my invitation, {feel_sorry}')

feel_sorry = guests.pop()

print(f'I am really sorry to decline my invitation, {feel_sorry}')

feel_sorry = guests.pop()

print(f'I am really sorry to decline my invitation, {feel_sorry}')

feel_sorry = guests.pop()

print(f'I am really sorry to decline my invitation, {feel_sorry}')

print(f'Your invitation is still active, {guests[0]}!')

print(f'Your invitation is still active, {guests[1]}!')

del guests[0]

del guests[0]

print(guests)
