#Inheritance: Overriding

class Person:

    def __init__(self, name):
        self.name = name

    def breath(self):
        print('Breathing')

    def walk(self):
        print('Walking')

class Doctor(Person):

    def __str__(self):
        return f"Doctor {self.name}"

    def breath(self):
        print('Doctor breaths')

d = Doctor('John')
p = Person('Adam')

p.breath()
d.breath()
p.walk()
d.walk()
print(p.name, d.name)
print(p,d)
