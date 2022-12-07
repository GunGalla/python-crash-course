# Упражнения 6.1 - 6.4

human = {
    'first_name': 'Yaroslav',
    'last_name': 'Kasatkin',
    'age': 30,
    'city': 'Saransk'
    }

print(human['first_name'])
print(human['last_name'])
print(human['age'])
print(human['city'])

favorite_nums = {
    'Evgenia': 28,
    'Yaroslav': 8,
    'Vladimir': 2,
    'Kirill': 10,
    'Mob': 23,
    }

for name in favorite_nums:
    print(f"{name}'s favorite number is:\n\t{favorite_nums[name]}!")
