# Упражнение 9.3 и 9.5

class User:
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        print(f"First name: {self.first_name}.")
        print(f"Last name: {self.last_name}.")
        print(f"Age: {self.age}.")
        print(f"Location: {self.country}.")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User('Yaroslav', 'Kasatkin', 30, 'Bulgaria')

user.describe_user()
user.greet_user()

person = User('Kirill', 'Trofimov', 40, 'Russia')

person.increment_login_attempts()
person.increment_login_attempts()
person.increment_login_attempts()
person.increment_login_attempts()
print(person.login_attempts)
person.reset_login_attempts()
print(person.login_attempts)
