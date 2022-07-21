#Basics Inheritance
#Everything is object in Python, can be checked with 
#function issubclass(smth, object)
class Vehicle:
    pass

class Car(Vehicle):
    pass

class Plane(Vehicle):
    pass

class Boat(Vehicle):
    pass

class RaceCar(Car):
    pass


print(issubclass(Car, Vehicle))
print(issubclass(RaceCar, Vehicle))
print(issubclass(RaceCar,Car))

#Task 
class NewInt(int):

    def repeat(self, n=2):
        return int(str(self)*n)

    def to_bin(self):
        return int(str(bin(self))[2:])

