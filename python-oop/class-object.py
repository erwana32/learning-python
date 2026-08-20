class Kampus:
    nama = ""
    alamat = ""

class Mahasiswa:
    nim = ""
    nama = ""
    
    def perkenalan(self):
        print(f"Halo nama saya {self.nama}")
    
    def hello(self, nama):
        print(f"Halo {nama}, nama saya {self.nama}")
 
        
mahasiswa1 = Mahasiswa()
mahasiswa1.nim = "12345"
mahasiswa1.nama = "Erza"

mahasiswa1.perkenalan()
mahasiswa1.hello("Syifa")

