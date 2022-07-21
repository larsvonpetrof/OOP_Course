#Property. getter-method and setter-method
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        #make it private
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def set_balance(self, value):
        if not isinstance(value, (int,float)):
            raise ValueError('Balance must be number')
        self.__balance = value
    def delete_balance(self):
        print("delete balance")
        del self.__balance
    balance = property(fget=get_balance,fset=set_balance,fdel=delete_balance)

a = BankAccount('Ivan', 100)

#Task 1 - workable, however diffet to solution
class UserMail:
    def __init__(self, login, __email):
        self.login = login
        self.__email = __email
    def _get_mail(self):
        return self.__email
    def _set_mail(self, value):
        if not isinstance(value, str):
            raise ValueError(f"ErrorMail: {value}")
        #can be used "\" for going to the next row
        elif ((value.count("@") != 1) 
            + (value.find("@") > value.find("."))):
            raise ValueError(f"ErrorMail: {value}")
        self.__email = value

k = UserMail("belosne#ka","prins@gmail.com")
print(k.email)
k.email = [1,2,3]
k.email = "prinse@still@.wait"
k.email = "prince@still.wait"

#Solution
class UserMail:
    def __init__(self, name, mail):
        self.login = name
        self.__email = mail
    def get_mail(self):
        return self.__email
    def set_mail(self, new_mail):
        if isinstance(new_mail,str) and \
           new_mail.count("@") == 1 and \
           "." in new_mail[new_mail.find("@"):]:
            self.__email = new_mail
        else:
            raise ValueError(f"ErrorMail: {new_mail}")
    email = property(fget=_get_mail, fset=_set_mail)

#Getter() and setter()

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        #make it private
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def set_balance(self, value):
        if not isinstance(value, (int,float)):
            raise ValueError('Balance must be number')
        self.__balance = value
    def delete_balance(self):
        print("delete balance")
        del self.__balance
    my_balance = property()
    my_balance = my_balance.getter(get_balance)
    my_balance = my_balance.setter(set_balance)
    my_balance = my_balance.deleter(delete_balance)
    balance = property(fget=get_balance,fset=set_balance,fdel=delete_balance)




