# decorator
def decorator(func):
    def inner(*args,**kwargs):
        print('start decorator...')
        func(*args,**kwargs)
        print('end decorator...')
    return inner

def say(name, surname):
    print("hello", name, surname)

say = decorator(say)
say('Vasja','Petrov')
# decorator HTML
def header(func):
    def inner(*args,**kwargs):
        print('<h1>')
        func(*args,**kwargs)
        print('</h1>')
    #define name and doc of func in order save it
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner
from functools import wraps
def table(func):
    #or we can use @wraps from functools
    @wraps(func)
    def inner(*args,**kwargs):
        print('<table>')
        func(*args,**kwargs)
        print('</table>')
    return inner

#say = table(header(say))
@table
@header
def say(name, surname,age):
    print("hello", name, surname,age)

def sqr(x):
    """
    Funciton makes x^2
    """
    print(x**2)

say('Vasja','Petrov',20)
