# Упражнения 9.1, 9.2 и 9.4

class Restaurant:
    '''Simple restaurant class'''

    def __init__(self, restaurant_name, restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"This restaurant's name is {self.restaurant_name}!")
        print(f'This is a {self.restaurant_type} restaurant.')

    def open_restaurant(self):
        print(f'Welcome! {self.restaurant_name.title()} is open for everyone!')

    def set_number_served(self, served_num):
        self.number_served = served_num

    def increment_number_served(self, served_today):
        self.number_served += served_today


my_restaurant = Restaurant('Twins Garden', 'seafood')

print(my_restaurant.restaurant_name)
print(my_restaurant.restaurant_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

good_restaurant = Restaurant('Beverly Hills', 'BBQ')
good_restaurant.describe_restaurant()

restaurant = Restaurant('Yeger', 'steakhouse')
print(restaurant.number_served)
restaurant.number_served = 20
print(restaurant.number_served)
restaurant.set_number_served(5)
print(restaurant.number_served)
restaurant.increment_number_served(35)
print(restaurant.number_served)


# Упражнение 9.6
class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, restaurant_type, *flavors):
        super().__init__(restaurant_name, restaurant_type)
        self.flavors = flavors

    def show_flavors(self):
        print("We have following flavors of ice-cream:")
        for item in self.flavors:
            print(f"- {item.title()}")


ice_cream_restaurant = IceCreamStand('33 Penguins', 'Gelato', 'chocolate', 'raspberry')

ice_cream_restaurant.show_flavors()
ice_cream_restaurant.describe_restaurant()
