#Magic Method __call__
#Example of closure by __call__
class Counter:

    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.length = 0
        print('init objeckt', self)

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summa += sum(args)
        self.length += len(args)
        print(f'object called {self.counter} times')

    def average(self):
        return self.summa / self.length
from time import perf_counter
#Example of property by __call__
class Timer:
    def __init__(self, func):
        self.fn = func

    def __call__(self, *args,**kwargs):
        start = perf_counter()
        print(f'Function {self.fn.__name__} is called')
        result = self.fn(*args, **kwargs)

        finish = perf_counter()
        print(f'Function {self.fn.__name__} {finish - start} worked')
        return result

@Timer
def fact(n):
    pr=1 
    for i in range(1,n+1):
        pr *= i
    return pr

def fib(n):
    if n<=2:
        return 1
    return fib(n-1) + fib(n-2)

#Decoration can be realized another way:
#fact = Timer(fact)


#Task 1
class Addition:

    def __call__(self, *args, **kwargs):
        vec = [i for i in args if isinstance(i, (int,float))]
        return f'Sum of input values is {sum(vec)}'

import time
#Task 2
class Timer_New:
    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        self.fn(*args)
        finish = time.time()
        return f'Working time of the program is {round(finish - start,2)}'

@Timer_New
def calculate():
    for i in range(10000000):
        2**100
        
