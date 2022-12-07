# Упражнение 6.7, 6.8

human_1 = {
    'first_name': 'Yaroslav',
    'last_name': 'Kasatkin',
    'age': 30,
    'city': 'Saransk'
    }

human_2 = {
    'first_name': 'Evgenia',
    'last_name': 'Kasatkina',
    'age': 29,
    'city': 'Essentuki'
    }

human_3 = {
    'first_name': 'Robert',
    'last_name': 'Kasatkin',
    'age': 4,
    'city': 'Moscow'
    }

people = [human_1, human_2, human_3]

for human in people:
    name = human['first_name']
    surname = human['last_name']
    print(f"{surname} {name}, {human['age']}.\n\tLiving in {human['city']}")
