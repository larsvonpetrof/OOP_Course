# Class Exception

class MyException(Exception):
    """This is my first Exception"""

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print("str called")
        if self.message:
            return f"MyException ({self.message})"
        else:
            return "MyException is empty"

raise MyException('hello')
