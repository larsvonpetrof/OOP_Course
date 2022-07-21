#Magic comparison methods
# __eq__ - ==
# __ne__ - !=
# __lt__ - <
# __le__ - <=
# __gt__ - >
# __ge__ - >=

class Rectangle:

    def __init__(self, a,b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b
        
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area
        elif isinstance(other, (int, float)):
            return self.area < other
    #below method is based on the previous ones
    def __le__(self, other):
        return self == other or self < other

#Task 
class ChessPlayer:

    def __init__(self,name,surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, int):
            return self.rating == other
        elif isinstance(other, ChessPlayer):
            return self.rating == other.rating
        else:
            return 'Comparison is imposible'

    def __gt__(self, other):
        if isinstance(other, int):
            return self.rating > other
        elif isinstance(other, ChessPlayer):
            return self.rating > other.rating
        else:
            return 'Comparison is imposible'

    def __lt__(self, other):
        if isinstance(other, int):
            return self.rating < other
        elif isinstance(other, ChessPlayer):
            return self.rating < other.rating
        else:
            return 'Comparison is imposible'
