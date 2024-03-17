# Inherit parent class into chile class
# you have to inherit parent constructor if it has code defined in parent class and it's not default.


from classdemo import Calculator


class ChildImpl(Calculator):

    num2 = 20

    def __init__(self):

        Calculator.__init__(self, 2, 5)

    def get_moredata(self):
        return self.num2 + self.num + self.summation()


obj = ChildImpl()
print(obj.get_moredata())

