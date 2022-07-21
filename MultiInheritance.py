#Multiple Inheritance
class Doctor:

    def __init__(self, degree):
        self.degree = degree

    def graduate(self):
        print('I\'m Doctor, yahoo!') 

class Builder:
    def __init__(self, rank):
        self.rank = rank
    def graduate(self):
        print('I\'m Builder, yahoo!') 

class Person(Doctor,Builder): #the order is important
# if the method isn't in the child class, it will look
# for it in Parent classes in strict order - this is known as MRO
# MRO - method resolution order
    def __init__(self, rank,degree):
        super().__init__(rank)
        Doctor.__init__(self,degree)
   # def graduate(self):
   #     print("let's see who am I")
   #     super().graduate()
   #     Doctor.graduate(self)
    def __str__(self):
        return f"Person {self.rank} {self.degree}"

s = Person(3,4)

