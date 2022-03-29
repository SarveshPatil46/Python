class Student:
    name = ''
    age = 0
    div = ''

    def greet(self):
        print(f'Hello {self.name}')

    def details(self):
        print(f'Age: {self.age}')
        print(f'Division: {self.div}')


# create a new object of Student class
sarvesh = Student()

# assign values to properties of student
sarvesh.name = 'Sarvesh'
sarvesh.age = 19
sarvesh.div = 'D10A'

# Calling object's greet() method
sarvesh.greet()
sarvesh.details()
