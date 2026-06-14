# Polymorphism:- Many forms

# Types
# 1. Function overriding - redefining the parent class(PC) func in Child class
# 2. Duck type - If two classes have no relation but they have a function of same name then it is called duck type.

#  func overriding

# class Employee:
#     def get_designation(self):
#         print("Designation = Employee")

# class Teacher(Employee):
#     def get_designation(self):
#         print("Designation = Teacher")

# t1 = Teacher()
# t1.get_designation()

# duck type

class Teacher():
    def get_designation(self):
        print("Designation = Employee")

class Student():
    def get_designation(self):
        print("Designation = Student")

t1 = Teacher()
t1.get_designation()

s1 = Student()
s1.get_designation()