import random
import math

print("""╔════════════════════╗ 
║       KONSOL       ║
║                    ║ 
║ 1. Hesap Makinesi  ║
║ 2. Oyunlar         ║
║ 3. Çizimler        ║
║ 4. Not Hesabı      ║
║ 5. Boy Kilo Endeksi║
║ Seçiminizi Yapınız ║
╚════════════════════╝
""")

secim = input("Seçiminizi Yapın (Çıkış için 'q' ya basalım):")
if secim == 'q':
    print("Çıkılıyor...")
    quit()

if secim == "1":
    print("Hesap Makinesini Seçtiniz")
    print("""╔════════════════════╗ 
║ İşlem Listesi      ║
║                    ║ 
║ 1. Toplama İşlemi  ║
║ 2. Çıkarma İşlemi  ║
║ 3. Çarpma İşlemi   ║
║ 4. Bölme İşlemi    ║
╚════════════════════╝
""")
    while True:
        islem = input("İşlem Seçiniz (Çıkış için 'q' ya basalım): ")
        if islem == 'q':
            print("Çıkılıyor...")
            quit()
        elif islem == "1":
            print("║------Toplama İşlemi------║")
            sayi1 = int(input("1. Sayıyı Giriniz: "))
            sayi2 = int(input("2. Sayıyı Giriniz: "))
            print("║{} + {} = {}║".format(sayi1, sayi2, sayi1 + sayi2))
        elif islem == "2":
            print("║------Çıkarma İşlemi------║")
            sayi1 = float(input("1. Sayıyı Giriniz: "))
            sayi2 = float(input("2. Sayıyı Giriniz: "))
            print("║{} - {} = {}║".format(sayi1, sayi2, sayi1 - sayi2))
        elif islem == "3":
            print("║------Çarpma İşlemi------║")
            sayi1 = float(input("1. Sayıyı Giriniz: "))
            sayi2 = float(input("2. Sayıyı Giriniz: "))
            print("║{} x {} = {}║".format(sayi1, sayi2, sayi1 * sayi2))
        elif islem == "4":
            print("║------Bölme İşlemi------║")
            try:
                sayi1 = int(input("1. Sayıyı Giriniz: "))
                sayi2 = int(input("2. Sayıyı Giriniz: "))
                print("║{} / {} = {:.2f}║".format(sayi1, sayi2, sayi1 / sayi2))
            except ZeroDivisionError:
                print("║Bir sayıyı 0'a bölemezsiniz!║")
            except ValueError:
                print("║Lütfen sadece sayı girin!║")
        else:
            print("Geçersiz Seçenek...")

elif secim == "2":
    print("Oyunları Seçtiniz")
    print("""╔════════════════════╗ 
║ Oyun Listesi       ║
║                    ║ 
║ 1. Mayın Tarlası   ║
║ 2. Taş Kağıt Makas ║
║ 3. Adam Asmaca     ║
╚════════════════════╝
""")
    while True:
        islem = input("Oyun Seçiniz (Çıkış için 'q' ya basalım): ")
        if islem == 'q':
            print("Çıkılıyor...")
            quit()
        elif islem == "1":
            print("Mayın Tarlasını Seçtiniz")

            # Mayın Tarlası oyunu
            def minesweeper():
                # Oyun tahtası boyutları
                BOARD_WIDTH = 10
                BOARD_HEIGHT = 10

                # Mayın sayısı
                NUM_MINES = 10

                # Mayın tarlası tahtası
                board = [[0 for x in range(BOARD_WIDTH)] for y in range(BOARD_HEIGHT)]

                # Mayınları yerleştirme
                mines = set()
                while len(mines) < NUM_MINES:
                    x = random.randint(0, BOARD_WIDTH - 1)
                    y = random.randint(0, BOARD_HEIGHT - 1)
                    if board[y][x] == 0:  # Aynı yere iki kere mayın yerleştirmeyi engeller
                        board[y][x] = "X"
                        mines.add((x, y))

                # Kullanıcının tahmin ettiği koordinatları alır
                def get_guess():
                    while True:
                        try:
                            x, y = map(int, input("Tahmin etmek istediğiniz koordinatları girin (örneğin: 2,3): ").split(","))
                            if x < 0 or x >= BOARD_WIDTH or y < 0 or y >= BOARD_HEIGHT:
                                print("Girdiğiniz koordinatlar tahtanın dışında kaldı. Lütfen tekrar deneyin.")
                                continue
                            return x, y
                        except ValueError:
                            print("Geçersiz koordinat. Lütfen tekrar deneyin.")

                # Tahtayı ekrana basar
                def print_board(board, show_mines=False):
                    print("  " + " ".join(str(x) for x in range(BOARD_WIDTH)))
                    for i in range(BOARD_HEIGHT):
                        row = ""
                        for j in range(BOARD_WIDTH):
                            if board[i][j] == "X" and show_mines:
                                row += "X"
                            elif board[i][j] == 0:
                                row += "-"
                            else:
                                row += str(board[i][j])
                        print(str(i) + " " + row)

                # Verilen koordinatlardaki hücrenin komşu mayınlarını sayar
                def count_adjacent_mines(x, y):
                    count = 0
                    for i in range(max(0, y - 1), min(BOARD_HEIGHT, y + 2)):
                        for j in range(max(0, x - 1), min(BOARD_WIDTH, x + 2)):
                            if board[i][j] == "X":
                                count += 1
                    return count

                # Oyunun kazanılıp kazanılmadığını kontrol eder
                def check_win():
                    for i in range(BOARD_HEIGHT):
                        for j in range(BOARD_WIDTH):
                            if board[i][j] == 0:
                                return False
                    return True

                # Oyunu başlatır
                def play_game():
                    print("Mayın Tarlası oyununa hoş geldiniz!")
                    print_board(board)
                    while True:
                        x, y = get_guess()
                        if board[y][x] == "X":
                            print("Oyun bitti! Mayına bastınız.")
                            print_board(board, show_mines=True)
                            break
                        else:
                            adjacent_mines = count_adjacent_mines(x, y)
                            board[y][x] = adjacent_mines
                            print_board(board)
                            if check_win():
                                print("Tebrikler, oyunu kazandınız!")
                                break

                play_game()

            minesweeper()

        elif islem == "2":
            print("Taş Kağıt Makas Seçtiniz")

            # Taş Kağıt Makas oyunu
            def rock_paper_scissors():
                choices = ['taş', 'kağıt', 'makas']

                while True:
                    user_choice = input("Taş, Kağıt veya Makas? (Çıkmak için 'q' tuşuna basın): ").lower()
                    if user_choice == 'q':
                        print("Oyun sonlandırıldı.")
                        break
                    if user_choice not in choices:
                        print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
                        continue

                    computer_choice = random.choice(choices)

                    print(f"Senin seçimin: {user_choice}")
                    print(f"Bilgisayarın seçimi: {computer_choice}")

                    if user_choice == computer_choice:
                        print("Berabere! Tekrar deneyin.")
                    elif (user_choice == 'taş' and computer_choice == 'makas') or \
                         (user_choice == 'kağıt' and computer_choice == 'taş') or \
                         (user_choice == 'makas' and computer_choice == 'kağıt'):
                        print("Tebrikler! Kazandınız.")
                    else:
                        print("Üzgünüm! Kaybettiniz.")

            rock_paper_scissors()

        elif islem == "3":
            print("Adam Asmacayı Seçtiniz")

            # Adam Asmaca oyunu
            def hangman():
                try:
                    from termcolor import cprint
                except ImportError:
                    def cprint(*args, **kwargs):
                        print(*args)

                kelimeler = ["vantilatör", "adaptör", "kalem", "fare", "telefon", "kulaklık", "pervane", "merdane", "kestane"]

                def oyun_hazirlik():
                    global secilen_kelime, gorunen_kelime, can
                    secilen_kelime = random.choice(kelimeler)
                    gorunen_kelime = ["-"] * len(secilen_kelime)
                    can = 5

                def harf_al():
                    devam = True
                    while devam:
                        harf = input("Bir harf giriniz: ")
                        if harf.lower() == "quit":
                            cprint("Gidiyor gönlümün efendisi...", color="red", on_color="on_blue")
                            exit()
                        elif len(harf) == 1 and harf.isalpha() and harf not in gorunen_kelime:
                            devam = False
                        else:
                            cprint("Hatalı Giriş", color="red", on_color="on_grey")
                    return harf.lower()

                def oyun_dongusu():
                    global gorunen_kelime, can
                    while can > 0 and "-" in gorunen_kelime:
                        print("Kelime:", " ".join(gorunen_kelime))
                        print(f"Kalan Can: {can}")
                        tahmin = harf_al()
                        if tahmin in secilen_kelime:
                            for index, harf in enumerate(secilen_kelime):
                                if harf == tahmin:
                                    gorunen_kelime[index] = tahmin
                        else:
                            can -= 1
                            cprint(f"Yanlış tahmin! Kalan can: {can}", color="red", on_color="on_grey")
                    if "-" not in gorunen_kelime:
                        cprint("Tebrikler! Kelimeyi doğru tahmin ettiniz: " + secilen_kelime, color="green", on_color="on_grey")
                    else:
                        cprint("Oyunu kaybettiniz! Kelime şuydu: " + secilen_kelime, color="red", on_color="on_grey")

                oyun_hazirlik()
                oyun_dongusu()

            hangman()

        else:
            print("Geçersiz Seçenek...")

elif secim == "3":
    print("Çizimleri Seçtiniz")
    print("""╔════════════════════╗ 
║ Çizim Listesi      ║
║                    ║ 
║ 1. Kare Çiz        ║
║ 2. Üçgen Çiz       ║
║ 3. Çember Çiz      ║
╚════════════════════╝
""")
    while True:
        islem = input("Çizim Seçiniz (Çıkış için 'q' ya basalım): ")
        if islem == 'q':
            print("Çıkılıyor...")
            quit()
        elif islem == "1":
            print("Kare Çizme Seçtiniz")
            def draw_square():
                size = int(input("Karenin boyutunu giriniz: "))
                for i in range(size):
                    print("█ " * size)
            draw_square()

        elif islem == "2":
            print("Üçgen Çizme Seçtiniz")
            def draw_triangle():
                size = int(input("Üçgenin yüksekliğini giriniz: "))
                for i in range(size):
                    print(" " * (size - i - 1) + "* " * (i + 1))
            draw_triangle()

        elif islem == "3":
            print("Çember Çizme Seçtiniz")
            def draw_circle():
                radius = int(input("Çemberin yarıçapını giriniz: "))
                for y in range((2 * radius) + 1):
                    for x in range((2 * radius) + 1):
                        if math.sqrt((x - radius) ** 2 + (y - radius) ** 2) < radius + 0.5:
                            print("*", end=" ")
                        else:
                            print(" ", end=" ")
                    print()
            draw_circle()

        else:
            print("Geçersiz Seçenek...")

elif secim == "4":
    print("Not Hesabını Seçtiniz")
    print("""╔════════════════════╗ 
║ Not Hesap Listesi  ║
║                    ║ 
║ 1. Ortalama Hesapla║
║ 2. Harf Notu Çevir  ║
╚════════════════════╝
""")
    while True:
        islem = input("Not Hesap Seçiniz (Çıkış için 'q' ya basalım): ")
        if islem == 'q':
            print("Çıkılıyor...")
            quit()
        elif islem == "1":
            print("Ortalama Hesaplama Seçtiniz")
            def calculate_average():
                notlar = input("Notları giriniz (virgülle ayırarak): ").split(',')
                notlar = [float(n) for n in notlar]
                ortalama = sum(notlar) / len(notlar)
                print(f"Ortalamanız: {ortalama:.2f}")
            calculate_average()

        elif islem == "2":
            print("Harf Notu Çevirme Seçtiniz")
            def convert_grade():
                grade = float(input("Notu giriniz: "))
                if 90 <= grade <= 100:
                    print("Harf Notu: AA")
                elif 85 <= grade < 90:
                    print("Harf Notu: BA")
                elif 80 <= grade < 85:
                    print("Harf Notu: BB")
                elif 75 <= grade < 80:
                    print("Harf Notu: CB")
                elif 70 <= grade < 75:
                    print("Harf Notu: CC")
                elif 65 <= grade < 70:
                    print("Harf Notu: DC")
                elif 60 <= grade < 65:
                    print("Harf Notu: DD")
                elif 50 <= grade < 60:
                    print("Harf Notu: FD")
                else:
                    print("Harf Notu: FF")
            convert_grade()

        else:
            print("Geçersiz Seçenek...")

elif secim == "5":
    print("Boy Kilo Endeksi Seçtiniz")
    def calculate_bmi():
        height = float(input("Boyunuzu (metre cinsinden) giriniz: "))
        weight = float(input("Kilonuzu (kg cinsinden) giriniz: "))
        bmi = weight / (height ** 2)
        print(f"Vücut Kitle İndeksiniz: {bmi:.2f}")
        if bmi < 18.5:
            print("Kilo: Zayıf")
        elif 18.5 <= bmi < 24.9:
            print("Kilo: Normal")
        elif 25 <= bmi < 29.9:
            print("Kilo: Fazla Kilolu")
        else:
            print("Kilo: Obez")
    calculate_bmi()

else:
    print("Geçersiz Seçenek...")

