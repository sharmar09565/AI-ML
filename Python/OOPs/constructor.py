# Constructor:- We can only create one constructor inside a class unlike java and cpp. In py if a class has multiple constructor then only last one is consider as constructor

# Default constructor:- constructor has only self parameter 

class A:
    def __init__(self):     # curr instance of a class. It automatically pass. 
        print("This is the constructor")
    
a1 = A()
a2 = A()


# parameterized constructor

class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def show(self):
        print(f"Name: {self.name}")
        print(f"Cgpa: {self.cgpa}")
    
s1 = Student("Rohit", 8.5)
s2 = Student("Raj", 8.8)

s1.show()