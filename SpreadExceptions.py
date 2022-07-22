#Spread of Exceptions

def third():
    print('start first')
    1/0
    print('finish first')
def second():
    print('start first')
    third()
    print('finish first')
def first():
    print('start first')
    try:
        second()
    except ZeroDivisionError:
        print('handling first')

    print('finish first')

print('hello')
first()
