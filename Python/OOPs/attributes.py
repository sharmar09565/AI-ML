# Attributes:- they are two types

# 1. class - belongs to class. Same for all obj
# 2. instance - belongs to obj. Can be same or unique for each obj

class Student:
    college = "SVIET"       # class
    branch = "CSE"

    def __init__(self, name, cgpa, branch):
        self.name = name
        self.cgpa = cgpa
        self.branch = branch    #this branch has higher priority as this attribute is specific for an instance

s1 = Student("Rahul", 8.9, "CSD")

print(Student.branch)