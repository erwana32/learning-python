#Membuat class turunan dari Exception untuk handling error lebih spesifik
class BalanceNotEnough(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return self.message

class BankAccount:
    def __init__(self, number, balance=0):
        self.number = number
        self.balance = balance
    
    def transer(self, amount):
        if amount > self.balance:
            raise BalanceNotEnough("Saldo Tidak Mencukupi")
        self.balance -= amount
 
try:       
    bank_account = BankAccount("12345", 1000000)
    bank_account.transer(2000000)
except BalanceNotEnough as e:
    print(f"Error : {e}")

print("PROGRAM SELESAI")
        