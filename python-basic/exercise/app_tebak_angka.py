def app_tebak_angka():
    import random
    angka_acak = random.randint(1, 10)
    maksimal_tebakan = 3
    tebakan = 0
    while tebakan < maksimal_tebakan:
        tebakan += 1
        angka_user = int(input("Masukan Angka: "))
        if angka_user > angka_acak:
            print("Angka anda Lebih besar")
        elif angka_user < angka_acak:
            print("Angka anda lebih kecil")
        else:
            print("Selesai, Anda Benar")
            break
    else:
        print("kamu telah melewati maksimal tebakan:")
        print("Angka yang benar adalah, ", angka_acak)
    input("Enter untuk lanjut :")
            
def app_menu():
    while True:
        print("===== PROGRAM APP TEBAK ANGKA =====")
        print("1. Tebak Angka")
        print("2. Keluar")
        print("==== PROGRAM TEBAK ANGKA SEDERHANA ====")
        
        pilihan = int(input("Pilihan: "))
        
        if pilihan == 1:
            app_tebak_angka()
            
        elif pilihan == 2:
            print("PROGRAM TEBAK ANGKA SELESAI")
            break
        else:
            print("Error: Pilihan Tidak Valid")
app_menu()
        