#Magic Methods: __bool__

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    #if __bool__ is not determined in class,
    #bool() would check __len__
    #otherwise bool() would return always True
    def __len__(self):
        print('call len')
        return abs(self.x - self.y)

    def __bool__(self):
        print('call bool')
        return self.x != 0 or self.y != 0
#Task 1
class City:

    def __init__(self, name):
        self.name = name.title()

    def __str__(self):
        return self.name

    def __bool__(self):
        return 'aeiou'.find(self.name[-1]) == -1 
# Task 2

class Quadrilateral:
    
    def __init__(self, width, height=0):
        self.width = width
        if height == 0:
            self.height = width
        else:
            self.height = height

    def __str__(self):
        if self.width == self.height:
            return f'Cube {self.width}x{self.height}'
        else:
            return f'Quadrilateral {self.width}x{self.height}'

    def __bool__(self):
        return self.width == self.height
