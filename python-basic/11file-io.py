#print("======== Simpan Data Nilai =========")

#file = open("nilai-siswa.txt", "w") #mode write

# while True:
#     nama = input("Masukkan Nama Siswa: ")
#     if nama == "":
#         break
#     nilai = input("Masukkan Nilai Siswa:")
    
#     file.write(f"Nama: {nama}, Nilai: {nilai}.\n")
#     print(f"Data {nama} berhasil disimpan.")
    
# file.close()
# print("Program selesai.")   

# print("======== Baca Data Nilai =========")

# file = open("nilai-siswa.txt", "r")
# for line in file:
#     data = line.strip().split(",")
#     print(data[0], ":", data[1])
# file.close()

# print("Program selesai.")

print("======== Baca Data Nilai =========")
try:
    with open("-siswa.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            print(data[0], ":", data[1])    
except FileNotFoundError:
        print(f"File tidak ditemukan. Pastikan file ada di direktori yang benar.")
    
print("======== Program selesai ========")