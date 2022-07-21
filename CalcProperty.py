#Calculated Property
class Square:


    def __init__(self, s):
        self.__side = s
        self.__area = None
#if s is const and we don't need area is calculated
# each time, we need creat self.__area = None
    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None
    
    @property
    def area(self):
        if self.__area is None:
            print("Calculated output")
            self.__area = self.side**2
        return self.__area

# Task 1
class Rectangle:

    def __init__(self, l, w):
        self.area = l * w

# Task 2
class Date:

    def __init__(self, d, m, y):
        self.day = str(d)
        self.month = str(m)
        self.year = str(y)
    
    @property
    def date(self):

        if len(self.day) < 2:
            self.day = '0' + self.day

        if len(self.month) < 2:
            self.month = '0' + self.month

        if len(self.year) < 4:
            self.year = '0' + self.year

        return f'{self.day}/{self.month}/{self.year}'
    
    @property
    def usa_date(self):

        if len(self.day) < 2:
            self.day = '0' + self.day

        if len(self.month) < 2:
            self.month = '0' + self.month

        if len(self.year) < 4:
            self.year = '0' + self.year

        return f'{self.month}/{self.day}/{self.year}'
#Solution Task 2
class Date_solution:

    def __init__(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y
    
    @property
    def date(self):
        return f'{self.day:02}/{self.month:02}/{self.year:02}'
    
    @property
    def usa_date(self):
        return f'{self.month:02}-{self.day:02}-{self.year:02}'
