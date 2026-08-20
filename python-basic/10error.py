#SyntaxError
#print("Hello World"

#NameError
#print(nama)

#TypeError
#print("Umur: " + 25)

#ValueError
#angka = int("Lima")

#IndexError [list]
#daftar = [1, 2, 3]
#print(daftar[5])

#KeyError {disctonary}
#kamus = {"nama": "Andi", "umur": 30}
#print(kamus["kota"])

#ZeroDivisionError
#hasil = 10 / 0

#===============Kalkulator Sederhana============================
# angka1 = int(input("Angka pertama:"))
# angka2 = int(input("Angka kedua:"))
# hasil = print(f"Hasil Penjumlahan: {angka1 + angka2}")

#===============Penanganan Error dengan try-except===================
# print("=======Kalkulator Pembagian Sederhana=======")
# try:
#     angka1 = int(input("Angka pertama:"))
#     angka2 = int(input("Angka kedua:"))
#     hasil = print(f"Hasil Penjumlahan: {angka1 / angka2}")
# except ValueError:
#     print("Terjadi kesalahan dalam input angka. Pastikan Anda memasukkan angka yang valid.")
# except ZeroDivisionError:
#     print("Terjadi kesalahan: Pembagian dengan nol tidak diperbolehkan.")
# except:
#     print("Terjadi kesalahan yang tidak terduga.")
# print("Program selesai.")


try:
    angka = int(input("Masukkan sebuah angka: "))
except ValueError as ve:
    print("Angka tidak valid:", ve)
else:
    print("Anda memasukkan angka:", angka)
    if angka > 0:
        print("Angka tersebut adalah bilangan positif.")
    elif angka < 0:
        print("Angka tersebut adalah bilangan negatif.")
    else:
        print("Angka tersebut adalah nol.")
finally:#tetap dijalankan meskipun error atau tidak
    print("Terima kasih telah menggunakan program ini.")