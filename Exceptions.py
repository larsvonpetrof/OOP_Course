# Exceptions

try:
    int('Hellow')
except ValueError:
    print('incorrect transformation')

# Task 1
class Wallet:
    def __init__(self, currency, balance):
        self.balance = balance
        try:
            if isinstance(self.currency, str):
                self.currency = currency
        except TypeError:
            print('Incorrect currency type')
        try:
            len(str(self.currency)) == 3
        except NameError:
            print('Incorrect length of currency name')
        try:
            str(self.currency).isupper()
        except ValueError:
            print('The name should be consisted of UPPER letters')

    
