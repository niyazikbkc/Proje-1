print("""╔════════════════════╗ 
║       KONSOL       ║
║                    ║ 
║ 1. Hesap Makinesi  ║
║ 2. Oyunlar         ║
║ 3. Çizimler        ║
║ 4.                 ║  
║ Seçiminizi Yapınız ║
╚════════════════════╝
""")
secim = input("Seçimizi Yapın (Çıkış için 'q' ya basalım):")
if secim  == 'q':
        print("Çıkılıyor...")
        quit()
if secim == "1" : print("Hesap Makinesini Seçtiniz")
if secim == "2" : print("Oyunları Seçtiniz")
if secim == "3" : print("Çizimleri Seçtiniz")