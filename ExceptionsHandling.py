#Error-exceptions handling

try:
    1/0
    int("helo")
except ValueError:
    print("error ValueError")
except ZeroDivisionError as zeroErr:
    print(f"Logging error: {zeroErr} {repr(zeroErr)}")
    raise TypeError('TypeError') from None
except (KeyError, IndexError) as error:
    print(f"Logging error: {error} {repr(error)}")
else:
    print("else")
finally:
    print('hend')

try:
    raise ValueError('value error')
except ValueError:
    try:
        raise TypeError('type error')
    except TypeError:
        raise Exception('Big Exception')
