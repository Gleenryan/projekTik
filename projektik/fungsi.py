import random


def latihan_perkalian():
    soal = int(input("Berapa soal yang ingin kamu jawab? : "))
    benar = 0
    soal_terjawab = 0

    while soal:
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        hasil = a * b
        jawaban = int(input(f"{a} X {b} = "))
        if jawaban == hasil:
            benar += 1
            print("Jawaban kamu benar!")
        else:
            print(f"Jawaban kamu salah! yang benar adalah {hasil}.")
        soal_terjawab += 1
        print(f"Soal terjawab ({soal_terjawab} / {soal})")

        if soal_terjawab == soal:
            nilai = benar / soal * 100
            print("")
            print(f"Nilai kamu adalah : {int(nilai)} / 100")
            soal = False


def mengubah_celcius():
    suhu = int(input("Berapa (°C) suhu yang ingin dikonversi : "))
    print("Daftar konversi suhu :")
    print("1) Fahrenheit")
    print("2) Kelvin")
    konversi = int(input("Konversi ke (1/2) : "))

    if konversi == 1:
        suhu = (suhu * 9 / 5) + 32
    elif konversi == 2:
        suhu = suhu + 273.15

    print(f"Suhu setelah dikonversikan adalah {suhu}")


def BMI():
    berat = int(input("masukkan berat badan (dalam kg) :"))
    tinggi = int(input("masukkan tingi badan (dalam cm) :"))

    tinggi = tinggi / 100

    BMI = berat / tinggi ** 2

    if BMI < 18.5:
        print("Berat Badan kurang")
    elif 18.5 <= BMI <= 22.9:
        print("Berat Badan normal")
    elif 23 <= BMI <= 29.9:
        print("Berat Badan berlebih")
    else:
        print("Obesitas")


def Guess_the_number():
    soal = random.randint(1, 100)
    win = False
    print("Tingkat kesulitan :")
    print("1) Easy")
    print("2) Medium")
    print("3) Hard ")
    kesulitan = int(input("masukkan tingkat kesulitan (1/2/3) :"))

    if kesulitan == 1:
        percobaan = 10
    elif kesulitan == 2:
        percobaan = 5
    elif kesulitan == 3:
        percobaan = 3

    for i in range(1, percobaan + 1):
        guess = int(input("Guess the number (1/100) : "))

        if guess == soal:
            win = True
            break
        elif guess < soal:
            print("Higher!")
            print(f"Total Percobaan : {i} / {percobaan}")
        elif guess > soal:
            print("Lower!")
            print(f"Total Percobaan : {i} / {percobaan}")

    if win:
        print("Kamu menang")
    else:
        print(f"Kamu kalah, angkanya adalah {soal}")


def BlackJack(): # Tjia Gleen Ryan / 28
    def kalkulator(cards):

        if sum(cards) == 21 and len(cards) == 2:
            return 0

        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def hasil(skor_pemain, skor_lawan):
        if skor_pemain > 21 and skor_lawan > 21:
            return "You went over. You lose 😤"

        if skor_pemain == skor_lawan:
            return "Draw 🙃"
        elif skor_lawan == 0:
            return "Kalah, lawan mendapatkan Blackjack 😱"
        elif skor_pemain == 0:
            return "Kamu menang dengan Blackjack 😎"
        elif skor_pemain > 21:
            return "Total Kartumu lebih dari 21. Kamu kalah😭"
        elif skor_lawan > 21:
            return "Total Kartu lawan lebih dari 21. Kamu menang 😁"
        elif skor_pemain > skor_lawan:
            return "Kamu menang 😃"
        else:
            return "Kamu kalah 😤"

    def ambil_kartu():

        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    def play_game():

        kartu_pemain = []
        kartu_lawan = []
        gameover = False

        for i in range(2):
            kartu_pemain.append(ambil_kartu())
            kartu_lawan.append(ambil_kartu())

        while not gameover:

            skor_pemain = kalkulator(kartu_pemain)
            skor_lawan = kalkulator(kartu_lawan)
            print(f"   Kartumu: {kartu_pemain}, Total skor: {skor_pemain}")
            print(f"   kartu pertama lawan: {kartu_lawan[0]}")

            if skor_pemain == 0 or skor_lawan == 0 or skor_pemain > 21:
                gameover = True
            else:

                lagi = input("Ketik 'y' untuk menambah kartu, ketik 'n' untuk pass: ")
                if lagi == "y":
                    kartu_pemain.append(ambil_kartu())
                else:
                    gameover = True

        while skor_lawan != 0 and skor_lawan < 17:
            kartu_lawan.append(ambil_kartu())
            skor_lawan = kalkulator(kartu_lawan)

        print(f"-------------------------------------------")
        print(f"   Kartu pemain: {kartu_pemain}, Total akhir: {skor_pemain}")
        print(f"   Kartu lawan: {kartu_lawan}, Total akhir: {skor_lawan}")
        print(hasil(skor_pemain, skor_lawan))

    play_game()


def kalkulator():
    def tambah(a, b):
        return a + b

    def kurang(a, b):
        return a - b

    def kali(a, b):
        return a * b

    def bagi(a, b):
        return a / b

    print("list :")
    print("1) Penambahan")
    print("2) Pengurangan")
    print("3) Perkalian")
    print("4) Pembagian")
    program = int(input("Program keberapa yang akan kamu pilih : "))
    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))

    if program == 1:
        hasil = tambah(a, b)
    elif program == 2:
        hasil = kurang(a, b)
    elif program == 3:
        hasil = kali(a, b)
    elif program == 4:
        hasil = bagi(a, b)
    else:
        print("Program tidak tersedia")
    print(f"Hasilnya adalah {hasil}")




