class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f'Name : {self.name}')
        print(f'Age : {self.age}')


class Student(Person):
    def __init__(self, name, age, div, roll_no):
        Person.__init__(self, name, age)
        self.div = div
        self.roll_no = roll_no

    def details(self):
        Person.details(self)
        print(f'Division : {self.div}')
        print(f'Roll No : {self.roll_no}')


name = str(input('Enter name: '))
age = int(input('Enter age: '))
div = str(input('Enter division: '))
roll_no = int(input('Enter roll no: '))
s1 = Student(name, age, div, roll_no)
s1.details()
