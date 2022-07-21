#Traning of Properties
from string import digits
password_DB = open('common-passwords.txt').readlines()

class User:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.__secret = 'Next level, Dude'

    @property
    def secret(self):
        s = input('Insert your password ')
        if s == self.password:
            return self.__secret
        else:
            raise ValueError('Access denied')

    @property
    def password(self):
        print("getter called")
        return self.__password

    @staticmethod
    def common_password(password):
        for passw in password_DB:
            if passw.strip() in password:
                return True
        return False

    @staticmethod
    def is_incl_num(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Pass should be string!")
        if  len(value) < 4:
            raise ValueError("Length of pass is too short, \
                             min 4 sybols")
        if not User.is_incl_num(value):
            raise ValueError("Pass must have at least one digit")
        if User.common_password(value):
            raise ValueError("Password is common used, use more complex")

        self.__password = value
        print("setter called")



