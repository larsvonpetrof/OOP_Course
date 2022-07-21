#Inheritance: Delegating

class Person:
    
    def __init__(self, name, surn):
        self.name = name
        self.surname = surn

    def breath(self):
        print('Man is breathing')

class Doctor(Person):

    def __init__(self,name,surn,age):
        #self.name = name
        #self.surname = surn
        #instead of above can be used super()
        super().__init__(name,surn) #parent should be before child
        self.age = age

    def breath(self):
        print('Doctor is breathing')
        super().breath() # calling parent method

p = Person('Ivan','Ivanov')
d = Doctor('Petr','Petrov',23)

print(p.name, p.surname)
print(d.name, d.surname, d.age)


#Task 1
class Transport:

    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return f'Type of Transport {self.kind} of brand {self.brand} \
                can be driven up to {self.max_speed} km/h'

class Car(Transport):

    def __init__(self, brand, max_speed, mileage, gasoline_residue):
        super().__init__(brand,max_speed,kind="Car")
        self.mileage = mileage
        self.__gasoline_residue = gasoline_residue

    @property
    def gasoline(self):
        return f"There is  gasoline for {self.__gasoline_residue} km" 

    @gasoline.setter
    def gasoline(self, value):
        if isinstance(value,int):
            self.__gasoline_residue += value
            print(f"The gasoline was increased on {value} l and is \
                  {self.__gasoline_residue} l")
        else:
            print("Error fueling")

class Boat(Transport):

    def __init__(self, brand, max_speed, owners_name):
        super().__init__(brand,max_speed,kind="Car")
        self.owners_name = owners_name

    def __str__(self):
        return f"This boat brand is {self.brand} owned by {self.owners_name}"

class Plane(Transport):

    def __init__(self, brand, max_speed, capacity):
        super().__init__(brand,max_speed,kind="Plane")
        self.capacity = capacity

    def __str__(self):
        return f"The plane brand {self.brand} and can board {self.capacity} people"

trn = Transport('Telega', 10)

print(trn)

bike = Transport('shkolnik', 20, 'bike')
print(bike)

plane = Plane('Virgin Atlantic', 700, 450)
print(plane)

car = Car('BMW', 230, 75000, 300)
print(car)
print(car.gasoline)
car.gasoline = 20
print(car.gasoline)

se_car = Car('Audi', 230, 70000, 130)
se_car.gasoline = [None]

boat = Boat('Yamaha', 40, 'Petr')
print(boat)

# Task 2

class Initialization:

    def __init__(self, capacity, food):
        if isinstance(capacity,int):
            self.capacity = capacity
            self.food = food
        else:
            print('Quantity of people has to be int')
        
class Vegetarian(Initialization):

    def __init__(self, capacity, food):
        super().__init__(capacity,food)

    def __str__(self):
        return f'{self.capacity} of people avoid eating meat! \
                They prefer to eat {self.food}'

class MeatEater(Initialization):

    def __init__(self, capacity, food):
        super().__init__(capacity,food)

    def __str__(self):
        return f'{self.capacity} of meateaters in Moscow! \
                however except meat they eat {self.food}'

class SweetTooth(Initialization):

    def __init__(self, capacity, food):
        super().__init__(capacity,food)

    def __str__(self):
        return f'There are {self.capacity} of sweet lovers in Moscow! \
                Their most favourite food is {self.food}'

    def __eq__(self, value):
        if isinstance(value, int) and self.capacity == value:
            return True
        elif isinstance(value, (Vegetarian, MeatEater)) and self.capacity==value.capacity:
            return True
        elif not isinstance(value, (int, Vegetarian, MeatEater)):
            print(f'Impossible to compare quantity of sweet tooth with {value}')
        else:
           return False

    def __lt__(self, value):
        if isinstance(value, int) and self.capacity < value:
            return True
        elif isinstance(value, (Vegetarian, MeatEater)) and self.capacity<value.capacity:
            return True
        elif not isinstance(value, (int, Vegetarian, MeatEater)):
            print(f'Impossible to compare quantity of sweet tooth with {value}')
        else:
            return False

    def __gt__(self, value):
        if isinstance(value, int) and self.capacity > value:
            return True
        elif isinstance(value, (Vegetarian, MeatEater)) and self.capacity>value.capacity:
            return True
        elif not isinstance(value, (int, Vegetarian, MeatEater)):
            print(f'Impossible to compare quantity of sweet tooth with {value}')
        else:
            return False

v_first = Vegetarian(1000, ['Nuts','vegetables','fruits'])
print(v_first)
v_second = Vegetarian([23], ['nothing'])

m_first = MeatEater(15000, ['Fried potatos','fish'])
print(m_first)

s_first = SweetTooth(30000,['Icecream','Chips','Choco'])
print(s_first)
print(s_first > v_first)

print(30000 == s_first)
print(s_first == 25000)
print(10000 < s_first)
print(100 < s_first)



