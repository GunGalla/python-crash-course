# Упражнение 9.3

class User:
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def describe_user(self):
        print(f"First name: {self.first_name}.")
        print(f"Last name: {self.last_name}.")
        print(f"Age: {self.age}.")
        print(f"Location: {self.country}.")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")


user = User('Yaroslav', 'Kasatkin', 30, 'Bulgaria')

user.describe_user()
user.greet_user()
