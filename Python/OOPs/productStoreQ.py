class Products:
    c = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Products.c+=1
    
    def info(self):
        print(f"price of {self.name} is {self.price}")

    @classmethod
    def total_prodcuct(cls):
        print(f"Total no. of product = {cls.c}")

    @staticmethod
    def calc_discount(price, discount_percent):
        discount = price*discount_percent/100
        print(f"You will get {discount} discount")

    
p1 = Products("mob",12000)
p2 = Products("lap",52000)

p1.info()

Products.total_prodcuct()

p1.calc_discount(p1.price,10)