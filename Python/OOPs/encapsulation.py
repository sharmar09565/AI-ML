# Encapsulation:- Wrapping up of a data in single unit 

class BankAccount:
    def __init__(self, name, balance):
        self.name = name 
        self.__balance = balance #private (we uses '_' to keep the variable protected and '__' for private)

    def get_balance(self):      #getter- use to access private and protected data outside the class
        return self.__balance
    
    def set_balance(self, newBalance):
        self.__balance = newBalance
        return self.__balance
    
acc1 = BankAccount("Rohit Sharma",10_000)

acc1.set_balance(12_000)
print(acc1.get_balance())

# There is no compulsion of using private and protected data outside the class.
# We can access protected data by simply obj._variableName and private by obj._className__variable