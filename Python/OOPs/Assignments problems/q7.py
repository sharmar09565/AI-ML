class Person:
    def __init__(self, name, age = None, address = None):
        self.name = name
        self.age = age
        self.address = address

    def show(self):
        print(f"Name: {self.name}\nAge: {self.age}\nAddress: {self.address}\n")

p1 = Person("Rohit")
p1.show()

p2 = Person("Rohit",20)
p2.show()

p3 = Person("Rohit",20,"Govindpur")
p3.show()