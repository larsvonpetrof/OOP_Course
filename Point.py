#Creat a class Point(x,y)

class Point:
    def __init__(self, coord_x=0, coord_y=0):
        self.move_to(coord_x,coord_y)
    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def go_home(self):
        self.move_to(0,0)
    def print_point(self):
        print(f"Point with coordinates ({self.x}, {self.y})")
    def calc_dist(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError("Arg must belong to class")
        return ((self.x - another_point.x)**2 + (self.y - another_point.y)**2)**0.5
#Task 1
class Dog:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def descript(self):
        print(f"{self.name} is {self.age} years old")
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
#Task 2 (Stack)
class Stack:
    def __init__(self):
        self.values = []
    def push(self,item):
        self.values.append(item)
    def pop(self):
        if not self.values:
            print("Empty Stack")
        else:
            return self.values.pop()
    def peek(self):
        if not self.values:
            print("Empty Stack")
        else:
            return self.values[-1]
    def is_empty(self):
        return self.values == []
    def size(self):
        return len(self.values)
