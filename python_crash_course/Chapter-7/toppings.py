# Упражнение 7.4

while True:
    topping = input("Which topping do you want to add?\n"
                    "Enter 'quit' if you finished with toppings. ")
    if topping == 'quit':
        break
    else:
        print(f'{topping.title()} has been added to your pizza!')
