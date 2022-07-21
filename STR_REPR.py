#Magic methods: __str__ and __repr__
class Lion:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"The object Lion - {self.name}"
    
    def __str__(self):
        return f"Lion - {self.name}"
#Task 1
class Person:

    def __init__(self, name, surname, gender='male'):
       self.name = name
       self.surname = surname
       self.gender = gender
       if not gender in ('male','female'):
           print('I\'ve no idea what do you mean?Let it be boy!')
           self.gender = 'male'

    def __str__(self):
        if self.gender == 'male':
            return f'Herr {self.name} {self.surname}'
        else:
            return f'Frau {self.name} {self.surname}'
        
#Task 2
class Vector:

    def __init__(self, *args):
        self.values = [x for x in args if isinstance(x,int)]

    def __str__(self):
        if elf.values:
            self.values.sort()
            for i in self.values:
                if not i == self.values[0]:
                    str_vec += ', ' + str(i)
                else:
                    str_vec = str(i)
            return f'Vector({str_vec})'
        else:
            return f'Empty Vector'
