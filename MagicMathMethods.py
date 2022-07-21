#Magic Methods: Math __add__, __mul__, __sub__, __truediv__

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def __add__(self, other):
        print('method __add__ call')
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            return self.balance + other
        raise NotImplemented
    def __radd__(self,other):
        print('__radd__ call')
        return self + other
#Task 
class Vector_incorrect:

    def __init__(self, *args):
        #nobody said it has to be list
        self.values = [x for x in args if isinstance(x,int)]

    def sort_values(vec):
            vec.sort()
            for i in vec:
                if not i == vec[0]:
                    str_vec += ', ' + str(i)
                else:
                    str_vec = str(i)
            return f'Vector({str_vec})'
        
    def __str__(self):
        if self.values:
            Vector.sort_values(self.values)
        else:
            return 'Empty Vector'

    def __add__(self, other):

        if isinstance(other, int):
            self.values = [i + other for i in self.values]
            return Vector.sort_values(self.values)

        elif isinstance(other, Vector):
            if len(other.values) != len(self.values):
                return 'Adding Vectors of different size'
            vec_sum = [i+j for i,j in zip(other.values, self.values)]
            return Vector.sort_values(vec_sum)
        else:
            return f'Vector cannot be added to {other}'
# Task Corrected
class Vector:

    def __init__(self, *args):
        self.values = sorted(args)

    def __str__(self):
        if self.values:
            temp = [str(i) for i in self.values]
            return f'Vector({", ".join(temp)})'
        else:
            return 'Vector is empty'

    def __add__(self, other):

        if isinstance(other, int):
            temp = [i+other for i in self.values]
            return Vector(*temp)
        elif isinstance(other, Vector):
            if len(other.values)==len(self.values):
                temp = [i+j for i,j in zip(self.values, other.values)]
                return Vector(*temp)
            else:
                return 'Addition of vectors with diff length is impossible'
        else:
            return f'Vector is impossible to add to {other}'

    def __mul__(self, other):

        if isinstance(other, int):
            temp = [i*other for i in self.values]
            return Vector(*temp)
        elif isinstance(other, Vector):
            if len(other.values)==len(self.values):
                temp = [i*j for i,j in zip(self.values, other.values)]
                return Vector(*temp)
            else:
                return 'Multiply of vectors with diff length is impossible'
        else:
            return f'Vector is impossible to multiply with {other}'


        

        
