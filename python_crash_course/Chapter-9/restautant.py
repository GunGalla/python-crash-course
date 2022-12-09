# Упражнения 9.1 и 9.2

class Restaurant:
    '''Simple restaurant class'''

    def __init__(self, restaurant_name, restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type

    def describe_restaurant(self):
        print(f"This restaurant's name is {self.restaurant_name}!")
        print(f'This is a {self.restaurant_type} restaurant.')

    def open_restaurant(self):
        print(f'Welcome! {self.restaurant_name.title()} is open for everyone!')


my_restaurant = Restaurant('Twins Garden', 'seafood')

print(my_restaurant.restaurant_name)
print(my_restaurant.restaurant_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

good_restaurant = Restaurant('Beverly Hills', 'BBQ')
bad_restaurant = Restaurant('Kirkorov', 'Gavno')
normal_restaurant = Restaurant('Frank', 'Ribs')

good_restaurant.describe_restaurant()
bad_restaurant.describe_restaurant()
normal_restaurant.describe_restaurant()
