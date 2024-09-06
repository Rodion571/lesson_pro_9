# Task 1
class BalanceDescriptor:
    def __get__(self, instance, owner):
        return instance._balance
    def __set__(self, instance, value):
        raise AttributeError("Заборонено змінювати баланс безпосередньо.")
class Account:
    balance = BalanceDescriptor()
    def __init__(self, initial_balance):
        self._balance = initial_balance
    @property
    def balance(self):
        return self._balance
    def __setattr__(self, name, value):
        if name == "_balance":
            super().__setattr__(name, value)
        elif name == "balance":
            raise AttributeError("Заборонено змінювати баланс безпосередньо.")
        else:
            super().__setattr__(name, value)
    def __getattr__(self, name):
        return f"Властивість '{name}' не існує."
account = Account(1000)
try:
    account.balance = 2000
except AttributeError as e:
    print(e)
print(account.some_nonexistent_property)
# Task 2
class User:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
    @property
    def first_name(self):
        return self._first_name
    @property
    def last_name(self):
        return self._last_name
    def __setattr__(self, name, value):
        if name in ["_first_name", "_last_name"]:
            super().__setattr__(name, value)
        elif name in ["first_name", "last_name"]:
            raise AttributeError(f"Заборонено змінювати значення {name}.")
        else:
            super().__setattr__(name, value)
    def __getattr__(self, name):
        return f"Властивість '{name}' не існує."
user = User("Іван", "Петренко")
try:
    user.first_name = "Олег"
except AttributeError as e:
    print(e)
print(user.middle_name)
# Task 3
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    def __setattr__(self, name, value):
        if name in ["_width", "_height"]:
            super().__setattr__(name, value)
        elif name in ["width", "height"]:
            raise AttributeError(f"Заборонено змінювати значення {name}.")
        else:
            super().__setattr__(name, value)
    def __getattr__(self, name):
        return f"Властивість '{name}' не існує."
    def area(self):
        return self._width * self._height
rectangle = Rectangle(10, 5)
try:
    rectangle.width = 20
except AttributeError as e:
    print(e)
print(rectangle.color)
print(f"Площа прямокутника: {rectangle.area()} кв. одиниць")
