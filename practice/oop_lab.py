class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_details(self):
        return f'{self.name} scored {self.marks}'

student1 = Student('srinath', 80)
student2 = Student('abhinav', 95)

print(student1.show_details())
print(student2.show_details())

