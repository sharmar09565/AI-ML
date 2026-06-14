# class Employee:
#     start_time = "10am"
#     end_time = "6pm"
    
#     def change_time(self, new_end_tine):
#         self.end_time = new_end_tine 

# class Teacher(Employee):
#     def __init__(self, subject):
#         self.subject = subject
    
# t1 = Teacher("Maths")

# t1.change_time("5pm")

# print(t1.subject, t1.start_time, t1.end_time) 

# Multilevel inheritance

# class Employee:
#     start_time = "10am"
#     end_time = "6pm"

# class AdminStaff(Employee):
#     def __init__(self, role):
#         self.role = role
    
# class Accountant(AdminStaff):
#     def __init__(self, salary, role):
#         super().__init__(role)      # this is used to call the parent constructor
#         self.salary = salary

# acc1 = Accountant(25_000, "CA")

# print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)


# Multiple inheritance

class Teacher:
    def __init__(self, salary):
        self.salary = salary
        
class Student:
    def __init__(self, gpa):
        self.gpa = gpa

class TA(Teacher, Student):
    def __init__(self, salary, gpa, name):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.name = name

    def show(self):
        print(f"Name:{self.name}\nSalary: {self.salary}\nGpa: {self.gpa}")

ta1 = TA(12_000, 8.5, "Rohit")
# print(ta1.name, ta1.gpa, ta1.salary)
ta1.show()