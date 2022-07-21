#Closure

def inner(value):
    def inner(a):
        return value + a
    return inner

def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

def avrg_num():
    number = []
    def inner(num):
        number.append(num)
        print(number)
        return sum(number) / len(number)
    return inner
#improve function with less code
def avrg_num2():
    summ = 0
    count = 0
    def inner(num):
        nonlocal summ
        nonlocal count
        summ += num
        count += 1
        return summ / count
    return inner

from datetime import datetime
def timer():
    start = datetime.now()
    def inner():
        return datetime.now() - start
    return inner

#one more time illustration
def add(a,b):
    return a + b

def couner(func):
    count = 0
    def inner(*args):
        nonlocal count
        count += 1
        print(f"Function {func} was called {count} times")
        return func(*args)
    return inner

