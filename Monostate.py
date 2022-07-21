class Cat:
    __shared_attr = {
        'breed': 'pers',
        'color': 'black'
    }
    def __init__(self):
        self.__dict__ = Cat.__shared_attr

class BankAccount:
    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport
    def print_public_data(self):
        self.__print_private_data()
    def print_protect_data(self):
        print(self._name,self._balance, self._passport)
    def __print_private_data(self):
        print(self.__name,self.__balance, self.__passport)

account1 = BankAccount('Bob', 10000, 737488348)

#Task 1
class Student:
    def __init__(self, name, age, branch):
        self.__name = name
        self.__age = age
        self.__branch = branch
    def __display_details(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"Branch: {self.__branch}")
    def access_private_method(self):
        self.__display_details()

obj = Student("Adam Smith",25,"Econimics")
obj.access_private_method()

#Task 2
class PizzaMaker:
    def __make_pepperoni(self):
        pass
    def _make_barbecue(self):
        pass
    def make_private(self):
        self.__make_pepperoni()

maker = PizzaMaker()
maker._make_barbecue()
