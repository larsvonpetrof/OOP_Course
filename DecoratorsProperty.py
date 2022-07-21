# Decorator Property
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        #make it private
        self.__balance = balance
    @property
    def my_balance(self):
        return self.__balance
    @my_balance.setter
    def my_balance(self, value):
        if not isinstance(value, (int,float)):
            raise ValueError('Balance must be number')
        self.__balance = value
    @my_balance.deleter
    def my_balance(self):
        print("delete balance")
        del self.__balance



#    my_balance = property()
#    my_balance = my_balance.getter(get_balance)
#    my_balance = my_balance.setter(set_balance)
#    my_balance = my_balance.deleter(delete_balance)
#    balance = property(fget=get_balance,fset=set_balance,
#                       fdel=delete_balance)

a = BankAccount('Ivan',100)
a.my_balance


#Task 1
class Notebook:
    def __init__(self, list_value):
        self._notes = list_value
    @property
    def note_list(self):
        conuter = 0
        for i in self._notes:
            conuter += 1
            print(f"{conuter}. {i}")
            

note = Notebook(['Potato','Tomato','Carrot'])

#Task 2 (my version, workable)
class Money:
    def __init__(self, dollars, cents):
        self.__dollar = dollars
        self.__cent = cents
        self.total_cents = self.__dollar * 100 + self.__cent
    @property
    def dollars(self):
        return self.total_cents // 100
    @dollars.setter
    def dollars(self,value):
        if isinstance(value, int) & (value > 0):
            self.__dollar = value
        else:
            raise ValueError("Error dollars")
    @property
    def cents(self):
        return self.__cent
    @cents.setter
    def cents(self, value):
        if isinstance(value, int) & (value in range(0,100)):
            self.__cent = value
        else:
            raise ValueError("Error cents")
    def __str__(self):
        return f'Your wealth is equal {self.dollars} and {self.cents}'
# Solution of Task 2
class Money_solution:

    def __init__(self, d, c):
        self.total_cents = d*100 + c

    @property
    def dollars(self):
        return self.total_cents // 100

    @property
    def cents(self):
        return self.total_cents % 100

    @dollars.setter
    def dollars(self, value):
        if isinstance(value,int) and (value>=0):
            self.total_cents = value*100 + self.cents
        else:
            print('Error dollars')

    @cents.setter
    def cents(self, value):
        if isinstance(value,int) and 100 > value >= 0:
            self.total_cents = self.dollars*100 + value
        else:
            print('Error cents')

    def __str__(self):
        return f'Your wealth is equal {self.dollars} and {self.cents}'
