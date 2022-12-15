"""Remember user's favorite number."""
# Упражнения 10.11 и 10.12
import json

file = 'fav_num.json'

try:
    with open(file) as f:
        number = json.load(f)
except FileNotFoundError:
    favorite_num = input('Please, enter your favorite number: ')
    file = 'fav_num.json'
    with open(file, 'w') as f:
        json.dump(favorite_num, f)
        print("I'll remember your favorite number, thank you!")
else:
    print(f"I know your favorite number! It's {number}!")
