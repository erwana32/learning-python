# class Kendaraan:
#     def __init__(self, merk, tahun):
#         self.merk = merk
#         self.tahun = tahun
    
#     def info(self):
#         return (f"Kendaraan : {self.merk} Keluaran Tahun {self.tahun}")
    
#     def turn_on(self):
#         return (f"{self.merk} dinyalakan")
    
# kendaraan1 = Kendaraan("Honda", "2025")
# print(kendaraan1.info())


# class Mobil(Kendaraan):
   
#     def klakson(self):
#         print(f"Mobil {self.info()} memiliki klakson")

# class Motor(Kendaraan):
    
#     def klakson(self):
#         print(f"Motor {self.info()} memiliki klakson")
        
# pajero = Mobil("Mitsubishi","2025")
# pajero.klakson()

# zx250 = Motor("Kawasaki","2025")
# zx250.klakson()

class Kendaraan:
    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun
    
    def info(self):
        return (f"Kendaraan : {self.merek} Keluaran Tahun {self.tahun}")
    
    def turn_on(self):
        return (f"{self.merek} dinyalakan")
    
kendaraan1 = Kendaraan("Honda", "2025")
print(kendaraan1.info())


class Mobil(Kendaraan):
    def __init__(self, merek, tahun, jml_roda):
        super().__init__(merek, tahun)
        self.jml_roda = jml_roda
        
    def klakson(self):
        print(f"Mobil {self.info()} memiliki klakson")

class Motor(Kendaraan):
    
    def klakson(self):
        print(f"Motor {self.info()} memiliki klakson")
    
    def turn_on(self): #ovveride method
        print(f"{self.merek} Otomatis dinyalakan")
        
pajero = Mobil("Mitsubishi","2025",4)
pajero.klakson()
print(pajero.jml_roda)

zx250 = Motor("Kawasaki","2025")
zx250.klakson()
zx250.turn_on()

#Type Checking
print(isinstance(pajero,Kendaraan))