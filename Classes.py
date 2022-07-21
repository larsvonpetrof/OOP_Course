class Person:
    name = 'Ivan'
    age = 30
setattr(Person, 'x',100)

class Car:
    model = 'BMW'
    engine = 1.6
    def drive():
        print('Let go')

class Cat:
    breed = 'pers'
    def hello(*args):
        print("Hello world from kitty", args)
    def show_breed(self):
        print(f'my breed is {self.breed}')
    def show_name(self):
        if hasattr(self, 'name'):
            print(f'my name is {self.name}')
        else:
            print('nothing')
    def __init__(self, name, breed='abyss',age=1, color='red'):
        print('hello new object is ',self, name, breed,age, color)
        self.breed = breed
        self.name = name
        self.age = age
        self.color = color

class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = brand + " " + model
#Task 2
class SoccerPlayer:
    def __init__(self,name, surname): 
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0 
    def score(self,goal=1):
        self.goals +=  goal 
    def make_assist(self,assist=1):
        self.assists += assist
    def statistics(self):
        print(f"{self.name} {self.surname} - {self.goals} assists {self.assists}")
#Task 3
class Zebra:
    stripe = "Stripe Black"
    def which_stripe(self):
        if self.stripe == "Stripe Black":
            self.stripe = "Stripe White"
        else:
            self.stripe = "Stripe Black"
        print(self.stripe)
#Task 4
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def full_name(self):
        print(f"{self.first_name} {self.last_name}")
    def is_adult(self):
        if self.age >= 18:
            print(True)
        else:
            print(False)

