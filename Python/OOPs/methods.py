class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage
    
    # instance method: It has 1st parameter self. It can access both class and instance attributes. 
    
    def info(self):    
        print(f";aptop has {self.RAM} RAM ans {self.storage} {self.storage_type}")

    # class method: It has 1st parameter class. Can only access class attributes.
    # We use a decorator with this.Decorators is a func that takes another function/class as an argument and modifies the behavior of that function. It can used by using @decorator_name above the original func.
    
    @classmethod    # it is an inbuilt decorator
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")

    # Static method: No compulsory parameter. IT can neither use class nor instance attribute. It uses @staticmethod

    @staticmethod
    def cal_discount(price,discount):
        final_price = price - (discount*price/100)
        print(f"discounted price = {final_price}")



l1 = Laptop("16gb","512gb")
l2 = Laptop("8gb","256gb")

l1.info()
#class method can be called by using class name or obj name
l1.get_storage_type()
# or
Laptop.get_storage_type()

l1.cal_discount(40000,10)