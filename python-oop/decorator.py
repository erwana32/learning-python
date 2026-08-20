class Matematika:
    
    @staticmethod
    def penjumlahan(a, b):
        hasil = a + b
        return hasil
    
print(Matematika.penjumlahan(10,10))




class BankAccount:
    number = ""
    balance = ""
    active = True
    
    def __init__(self, number, balance = 0):
        self.number = number
        self.balance = balance
    
    @classmethod
    def disabled(cls, number, balance=0):
        result = cls(number, balance)
        result.active = False
        return result
        
        
account1 = BankAccount("1234", 10000)
print(f"Bank Account: {account1.number} - {account1.balance} - {account1.active}")

account2 = BankAccount.disabled("67890", 2000000)
print(f"Bank Account: {account2.number} - {account2.balance} - {account2.active}")


#method getter setter di python menggunakan @property (getter) @nama_method.setter
class Category:
    _name = "" #protected
    #__name is private
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Name cannot be empty")
        self._name = name
cat1 = Category()
cat1.name = "Syifa"
print(cat1.name)
print(cat1._name)
