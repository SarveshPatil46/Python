class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** (1 / 2)


a = int(input('Enter side A: '))
b = int(input('Enter side B: '))
c = int(input('Enter side C: '))
t1 = Triangle(a, b, c)
print(t1.area())
