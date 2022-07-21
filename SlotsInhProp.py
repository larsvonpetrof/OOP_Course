# Slots, property, inheritance
class Rectangle:

    __slots__ = '__width', 'height'

    def __init__(self, a,b):
        self.width = a # here width.setter is called
        self.height = b

    @property
    def width(self):
        return self.__width 

    @width.setter
    def width(self, value):
        self.__width = value

a = Rectangle(2,3)
a.width
a.height

b = Rectangle(3,3)
b.perimetr

# __slots__ isn't inherited from parent automatically
# so should be added (no need to repeat attributes, just add 
#new ones.
class Square(Rectangle):
    __slots__ = 'color'
    
    def __init__(self,a,b,color):
        super().__init__(a,b)
        self.color = color

d = Square(2,2,'red')
d.width, d.height, d.color
#new attributes can be added
