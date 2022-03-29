class OperatorOverloading:
    def __init__(self, X):
        self.X = X

    def __gt__(self, U):
        if self.X > U.X:
            return True
        else:
            return False


object_1 = OperatorOverloading(int(input("Please enter the value: ")))
object_2 = OperatorOverloading(int(input("Please enter the value: ")))
if object_1 > object_2:
    print("The object_1 is greater than object_2")
else:
    print("The object_2 is greater than object_1")
