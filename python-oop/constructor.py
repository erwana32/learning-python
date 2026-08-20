class Mahasiswa:
    nim = ""
    nama = ""
    
    def __init__(self, nim, nama): #Constructor
        self.nim = nim
        self.nama = nama
        
    def __str__(self): #Method jika memanggil string
        return (f"{self.nim} - {self.nama}")
    
    def __eq__(self, other): #Perbandingan kedua object, bisa juga menggunakan perbandingan yg lain
        #__lt__ untuk < (less then)
        #__gt__ untuk > (greater then)
        #__le__ untuk <= (less equal then)
        #__ge__ untuk >= (greater equal then)
        return self.nim == other.nim and self.nama == other.nama
    
#memanggil constructor
mhs = Mahasiswa("10113500", "Erza")

print(mhs.nim)
print(mhs.nama)
#memanggil string
print(f"Mahasiswa : {mhs} ")

mhs2 = Mahasiswa("10113500", "Erza")

#memanggil method __eq__
print(mhs == mhs2)
        
class BankAccount:
    number = ""
    nama = ""
    saldo = ""
    
    def __init__(self, number, nama, saldo=0):
        if saldo < 0:
            raise ValueError("saldo harus positif")
        
        self.number = number
        self.nama = nama
        self.saldo = saldo

#erza = BankAccount("1234","Erza", -10000)

