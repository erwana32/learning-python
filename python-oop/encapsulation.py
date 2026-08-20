class BankAccount:
    __number = ""
    __name = ""
    __balance = 0
    
    def __init__(self, number, name):
        self.__number = number
        self.__name = name
        
    @property
    def balance(self):
        return self.__balance
    @property
    def name(self):
        return self.__name
    @property    
    def number(self):
        return self.__number
    
    def topup(self, topup_amount):
        self.__balance += topup_amount
    
    def withdrawl(self, wd_amount):
        if self.__balance < wd_amount:
          raise ValueError("Saldo kurang dari nominal WD")
        self.__balance -= wd_amount
        
acc1 = BankAccount("12345", "Erza")
print(acc1.number)
print(acc1.name)
print(acc1.balance)
 
acc1.topup(100000)
print(acc1.balance)

acc1.withdrawl(200000)
print(acc1.balance)