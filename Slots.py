# Slots - limit qnt of attributes
from timeit import timeit
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class PointSlots:
# __slots__ limits number of attributes in class
# it helps to control attributes and reduce the size
# increase the speed!
    __slots__= ('x','y')

    def __init__(self, x, y):
        self.x = x
        self.y = y
p1 = Point(2,3)
p1.x
p1.__dict__
#new attribute
p1.q = 100

p2 = PointSlots(3,4)
p2.x
#p2.__dict__ #Error now
def make_cl1():
    s = Point(2,3)
    s.x = 100
    del s.x

def make_cl2():
    s = PointSlots(2,3)
    s.x = 100
    del s.x

#print(s.__sizeof__(),s.__dict__.__sizeof__())
#print(p2.__sizeof__())
print(timeit(make_cl1))
print(timeit(make_cl2))

