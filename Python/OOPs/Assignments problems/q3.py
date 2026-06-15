class Student:
    def __init__(self, name, roll, marks):
        self._name = None
        self._roll = None
        self._marks = None
        name = name.strip()
        if(name!="" and (roll>=1 and roll<=100) and (marks>0 and marks<100)):
            self._name = name
            self._roll = roll
            self._marks = marks
        else:
            print("Enter valid input")

    def getter(self):
        print(f"Name: {self._name}\nRoll: {self._roll}\nMarks: {self._marks}")

    def setter(self, name, roll, marks):
        name = name.strip()
        if(name!="" and (roll>=1 and roll<=100) and (marks>0 and marks<100)):
            self._name = name
            self._roll = roll
            self._marks = marks
        else:
            print("Enter valid input")

s1 = Student("  Rohit ",22, 84)
s1.getter()

# s1.setter("Raj", 22, 84)
# s1.getter()