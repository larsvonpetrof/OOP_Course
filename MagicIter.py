#Magic Methods: __iter__, __next__
class Mark:

    def __init__(self, values):
        self.values = values
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        print('call next marks')
        if self.index >= len(self.values):
            self.index = 0
            raise StopIteration
        letter = self.values[self.index]
        self.index += 1
        return letter


class Student:

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __iter__(self):
        print('call iter')
        self.index = 0
        return iter(self.marks)

    def __next__(self):
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        self.index += 1
        return letter

m = Mark([1,2,2,2,3])
igor = Student('Igor', 'Schishkanov',m)

for i in igor:
    print(i)

#Task 1
class PowerTwo:

    def __init__(self,number):
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.index > self.number:
            raise StopIteration
        two_powered = 2 ** self.index
        self.index += 1
        return two_powered

#Task 2
class InfinityItegrator:

    def __init__(self):
        self.counter = -10

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 10
        return self.counter
