class Person:
    def __init__(self, first_name, last_name, user_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password


class Admin(Person):
    pass


class Costumer(Person):
    pass


class Employee(Person):
    pass


class Product:
    pass


class Book(Product):
    pass


class Coffee(Product):
    pass


class Order:
    pass
