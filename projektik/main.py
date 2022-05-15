from fungsi import *
#pembuat program utama : Reynaldo Divano / 22
running = True
while running:
    print("Daftar program :")
    print("1) Latihan perkalian") #Marcello adi/ 15
    print("2) Konversi °C ke suhu lain")#Christiano / 5
    print("3) Menentukan BMI") #Aaron / 1
    print("4) Guess the Number")#sherin adrea / 25
    print("5) BlackJack") # Tjia Gleen Ryan / 28
    print("6) kalkulator") #Jenefine / 6
    pilihan = int(input("Proram keberapakah yang ingin dijalankan : "))

    if pilihan == 1:
        latihan_perkalian()

    elif pilihan == 2:
        mengubah_celcius()

    elif pilihan == 3:
        BMI()

    elif pilihan == 4:
        Guess_the_number()

    elif pilihan == 5:
        BlackJack()

    elif pilihan == 6:
        kalkulator()

    else:
        print("fungsi tidak tersedia")

    keluar = input("Apakah anda ingin keluar? (y/n) : ")

    if keluar.lower() == "y":
        running = False




