def app_penjumlahan():
    try:
        angka1 = int(input("Angka Pertama:"))
    except ValueError:
        print("Input harus angka")
    try:
        angka2 = int(input("Angka Kedua:"))
    except ValueError:
        print("Input harus angka")
        
        hasil = angka1 + angka2
        print("Hasil Penjumlahan:", hasil)
    

def app_pengurangan():
    angka1 = int(input("Angka Pertama:"))
    angka2 = int(input("Angka Kedua:"))
    hasil = angka1 - angka2
    print("Hasil Pengurangan:", hasil)

def app_perkalian():
    angka1 = int(input("Angka Pertama:"))
    angka2 = int(input("Angka Kedua:"))
    hasil = angka1 * angka2
    print("Hasil Perkalian:", hasil)

def app_pembagian():
    angka1 = int(input("Angka Pertama:"))
    angka2 = int(input("Angka Kedua:"))
    hasil = angka1 / angka2
    print("Hasil Pembagian:", hasil)
    
def app_menu():
    while True:
        print("===== Kalkulator Sederhana =====")
        print("1.Penjumlahan")
        print("2.Pengurangan")
        print("3.Perkalian")
        print("4.Pembagian")
        print("5.Keluar")
        pilihan = int(input("Masukkan pilihan (1/2/3/4/5): """))
        
        if pilihan == 1:
            app_penjumlahan()
        elif pilihan == 2:
            app_pengurangan()
        elif pilihan == 3:
            app_perkalian()
        elif pilihan == 4:
            app_pembagian()
        elif pilihan == 5:
            print("Terima kasih telah menggunakan kalkulator sederhana ini.")
            break
app_menu()
        