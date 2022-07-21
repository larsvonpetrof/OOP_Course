from Polymorphism import Rectangle, Square, Circle

rect1 = Rectangle(3,4)
rect2 = Rectangle(12,2)


sq1 = Square(5)
sq2 = Square(7)


cir1 = Circle(5)
cir2 = Circle(7)

figures = [rect1,rect2,sq1,sq2,cir1,cir2]

print(sq1.get_sq_area(),sq2.get_sq_area())
print(rect1.get_rect_area(),
      rect2.get_rect_area())
#very bulky code, if we have a lot of objects
#like 
for fig in figures:
    if isinstance(fig, Square):
        print(fig.get_sq_area())
    elif isinstance(fig,Circle):
        print(fig.get_cir_area())
    else:
        print(fig.get_rect_area())

#Solution: Polymorphism - we call diff methods
#with one name - get_area()
#Python itself decides for which method for which object to implement
for fig in figures:
    print(fig, fig.get_area())

#Task
class UnitedKindom:
    
    @staticmethod
    def capital(self):
        return 'London is the capital of GB'
    @staticmethod
    def language(self):
        return 'Eng is the primary lang of GB'

class Spain:

    @staticmethod
    def capital(self):
        return 'Madrid is the capital of SP'
    @staticmethod
    def language(self):
        return 'Spanish is the primary lang of SP'
