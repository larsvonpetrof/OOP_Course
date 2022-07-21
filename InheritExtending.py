#Inheritance: Extending

class Person:

    def breath(self):
        print('breath')

    def sleep(self):
        print('person sleeps')

    def combo(self):
        self.breath()
        if hasattr(self, 'walk'):
            self.walk()
        self.sleep()
        if hasattr(self, 'age'):
            print(self.age)

class Doctor(Person):
    age = 30
    #extending:
    def sleep(self):
        print('dOCtor is sleeping')
        
    def sleep(self):
        print('Doctor sleeps')

    def walk(self):
        print('Doctor walks')

p = Person()
d = Doctor()

d.sleep()
p.sleep() #error

p.combo()
