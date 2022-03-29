# class
class Compute:
    def area(self, x=None, y=None):
        if x is not None and y is not None:
            return x * y
        elif x is not None:
            return x * x
        else:
            return 0


# object
obj = Compute()
# zero argument
print("Area Value:", obj.area())
# one argument
print("Area Value:", obj.area(4))
# two argument
print("Area Value:", obj.area(3, 5))
