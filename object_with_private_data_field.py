#Python object with private data fields
class BankAccount:

    def __init__(self, name, money):
        self.__name = name
        self.__balance = money # both __name and __balance are private data fields only accessible inside the class
    
    def deposit(self, money):
        self.__balance += money
    
    def withdraw(self, money):
        if self.__balance > money:
            self.__balance -= money
            return money
        else:
            return "Insufficient Funds"
        
    def checkBalance(self):
        return self.__balance
#end class BankAccount

b1 = BankAccount("Daniel", 400)
print(b1.withdraw(500))
b1.deposit(500)
print(b1.checkBalance())
print(b1.withdraw(800))
print(b1.checkBalance())
# print(b1.__balance)