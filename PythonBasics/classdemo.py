# declaring CLASS
#  SELF keyword is mandatory to call class and instance variable
#  default constructor name is always __init__
#  class can have n number of objects
#  arguments passed in class while creating object has to be caught in default constructor
#  which becomes parameterised constructor

class Calculator:

    # Num is CLASS VARIABLE
    num = 10   # no semicolon required in python

    # DEFAULT CONSTRUCTOR
    def __init__(self, a, b):    # a,b are INSTANCE VARIABLES
        self.first_num = a
        self.second_num = b

        print("I am called automatically when object is created")

    def summation(self):
        return self.first_num + self.second_num + self.num   # self.num = can also write Calculator.num

    def getdata(self):
        print("method execution , functions inside class calls method")


obj = Calculator(2, 3)  # Object created , make sure it creates outside class and method , check for space

obj.getdata()
print(obj.num)

print(obj.summation())



