class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = first
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Bro', 'Code', 50000)
emp_2 = Employee('Code', 'Basics', 60000)

# print(emp_1.email)
# print(emp_2.email)

# print(emp_1.fullname())

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_details(self):
        return f'{self.name} scored {self.marks} marks'
    
student1 = Student('Bro Code', 90)
student2 = Student('shadow coder', 85)

# print(student1.show_details())
# print(student2.show_details())

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        return f'{self.owner} deposited the money.'

    def withdraw(self):
        return f'{self.owner} has withdrawn the money.'

    def show_balance(self):
        return f'{self.owner} your balance amount is: {self.balance}'

user1 = BankAccount('srinath', 45000)
user2 = BankAccount('abhinav', 10000)

# print(user1.deposit())
# print(user1.show_balance())
# print(user2.show_balance())

class Car:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        return f'You are driving {self.brand} car at a speed of {self.speed}kmph'

driver1 = Car('BMW', 100)
driver2 = Car('Lamborghini', 250)

print(driver1.drive())
print(driver2.drive())