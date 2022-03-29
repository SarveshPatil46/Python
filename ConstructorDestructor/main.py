class Employee:
    def __init__(self, name, emp_id, salary, age):
        self.id = emp_id
        self.name = name
        self.salary = salary
        self.age = age

    def display(self):
        print(f'Name : {self.name}')
        print(f'ID : {self.id}')
        print(f'Salary : {self.salary}')
        print(f'Age : {self.age}')

    def __del__(self):
        print(f'Destructor called for {self.name}')


emp1 = Employee("John", 101, 90000, 24)
emp2 = Employee("David", 102, 110000, 25)

# accessing display() method to print employee 1 information

emp1.display()

# accessing display() method to print employee 2 information
emp2.display()
