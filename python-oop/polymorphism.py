class Hewan:
    def __init__(self, nama):
        self.nama = nama
    
    def suara(self):
        print(f"{self.nama}, bersuara")
        
class Anjing(Hewan):
    def suara(self):
        print(f"{self.nama}, Guk guk")
        
class Kucing(Hewan):
    def suara(self):
        print(f"{self.nama}, Meow")

class Sapi(Hewan):
    def suara(self):
        print(f"{self.nama}, Mooo")
        
hewan_list = [
    Anjing("Anjing"),
    Kucing("Kucing"),
    Sapi("Sapi")
]

for hewan in hewan_list:
    hewan.suara()
    
    
    
print(f"\n\n")   
#Duck Typing

class Mobil:
    def start(self):
        return "Mobil Menyala"

class Motor:
    def start(self):
        return "Motor Menyala"

class Kereta:
    def start(slef):
        return "Kereta Menyala"
    
#functon polymorphism
def operasikan_kendaraan(kendaraan):
    print(kendaraan.start())
    
#Polymorphism dengan duck typing
kendaraan_list = [
    Mobil(),
    Motor(),
    Kereta()
]

for kendaraan in kendaraan_list:
    operasikan_kendaraan(kendaraan)
    
print(f"\n")

# #Override Operator
# __add__ untuk +
# __sub__ untuk -
# __mul__ untuk *
# __eq__ untuk ==
# __lt__ untuk <
# __le__ untuk <=
# __gt__ untuk >
# __ge__ untuk >=
# __ne__ untuk !=

class Apple():
    def __init__(self, jumlah):
        self.jumlah = jumlah
    
    def __add__(self, other):
        return Apple(self.jumlah + other.jumlah)
    
    def __str__(self):
        return f"Apple: {self.jumlah}"
    
apple1 = Apple(10)
apple2 = Apple(30)
apple3 = apple1 + apple2
print(apple3)  

print(f"\n")

#Abstract Base Class
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod #metoe abstrak
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self): #implementasi metode dari abstract metod
        return self.length * self.width

class Circle(Shape): #implementasi metode dari abstract metod
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius **2

shape_list = [
    Rectangle(5,6),
    Circle(10)
]

for s in shape_list:
    print(f"Area is {s.area()}")

