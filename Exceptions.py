# Exceptions

try:
    int('Hellow')
except ValueError:
    print('incorrect transformation')

# Task 1
class Wallet:
    def __init__(self, currency, balance):
        try:
            if not isinstance(currency, str):
                raise TypeError()
        except TypeError:
            print('Incorrect currency type')
        try:
            if not len(str(currency)) == 3:
                raise NameError()
        except NameError:
            print('Incorrect length of currency name')
        try:
            if not str(currency).isupper():
                raise ValueError()
        except ValueError:
            print('The name should be consisted of UPPER letters')
        self.balance = balance
        self.currency = currency

    def __eq__(self, other):
        try:
            if isinstance(other, Wallet):
                return self.balance == other.balance and \
                        other.balance == self.balance
            else:
                raise TypeError()
        except TypeError:
            return f"Wallet doesn't support comparison with {other}"
        try:
            if not self.currency == other.currency:
                raise NameError()
        except NameError:
            print("Impossible to compare different currencies")

    def __add__(self, other):
        try:
            if not self.currency == other.currency:
                raise NameError()
        except NameError:
            return ("Impossible to add different currencies")
        try:
            if isinstance(other, Wallet):
                return Wallet(self.currency,self.balance + other.balance)
            else:
                raise TypeError()
        except TypeError:
            return (f"Wallet doesn't support addition with {other}")

    def __sub__(self, other):
        try:
            if not self.currency == other.currency:
                raise NameError()
        except NameError:
            return ("Impossible to substract different currencies")
        try:
            if isinstance(other, Wallet):
                return self.balance - other.balance
            else:
                raise TypeError()
        except TypeError:
            return (f"Wallet doesn't support this operation with {other}")
