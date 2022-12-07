# Упражнение 5.10

current_users = ['Yaroslav', 'Evgenia', 'Harry', 'Vladimir', 'Tom']

new_users = ['Pamela', 'Iris', 'EvgeNia', 'Busya', 'Harry']

user_check = []
for user in current_users:
    user_check.append(user.lower())

for user in new_users:
    if user.lower() in user_check:
        print(f'You need to choose a new username, name {user} is already taken.')
    else:
        print(f'Name {user} is available.')
