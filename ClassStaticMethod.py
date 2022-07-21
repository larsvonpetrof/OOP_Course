#Problem: how creat function inside Class 
# which can be called from Class and from Instance
class Example:

    def hello():
        print(f'hello') 
            
    def instance_hello(self):
        print(f'hello {self}')

    @staticmethod
    def static_hello():
        print('static_hello')

    @classmethod
    def class_hello(cls):
        print(f'hello {cls}')

#Task 1
class Robot:

    population = 0

    def __init__(self, name):
        self.name = name
        print(f"Robot {self.name} was created")
        Robot.population += 1

    def destroy(self):
        Robot.population -= 1
        print(f"Robot {self.name} was destroyed")

    def say_hello(self):
        print(f"Robot {self.name} is greeting you, human being!")

    @classmethod
    def how_many(self):
        print(f"{Robot.population}, so many of us are still alive")


