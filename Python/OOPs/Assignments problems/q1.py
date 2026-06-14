class BankAccount:
    def __init__(self, accNo, name, balance):
        self.name = name
        self.accNo = accNo
        self.balance = balance

    def deposit(self,deposit_money):
        self.balance += deposit_money
        return self.balance
    
    def withdraw(self,withdraw_money):
        self.balance -= withdraw_money
        return self.balance
    
    def check_balance(self):
        return self.balance

p1 = BankAccount(123, "Rahul", 12_000)

