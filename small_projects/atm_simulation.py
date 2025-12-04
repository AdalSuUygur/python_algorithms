
#todo Kapsamlı ATM Simülasyonu
#Kullanıcı adı ve şifre ile giriş, 3 kere hak var. Doğru girişte menüde 1- bakiye sorgula ,2- para yatır, 3-para çek, 4-çıkış
#Bakiye başlangıçta belirlenir. para yatırılırsa bakiyeye eklenir, çekilirse çıkartılır.
#Para çekerken: Önemli! Çekilmek istenen tutar bakiyeden fazlaysa "Yetersiz bakiye" uyarısı verilmeli, işlem yapılmamalı.

kullanici_adi = "adal"
sifre = "1234"
hak = 3
bakiye = 0
login_successful = False

while hak >= 0:
    if hak <= 0:
        print("Hesabınız bloke edilmiştir.")
        exit()
    else:
        username = input("İsminiz: ")
        password = input("Şifreniz: ")
        if username == kullanici_adi:
            if password == sifre:
                print(f"Giriş başarılı, hoşgeldin {username}")
                while True:
                    try:
                        islem = int(input("Bakiye sorgulamak için 1\nPara yatırmak için 2\nPara çekmek için 3\nGüvenli çıkış için 4\nYapılması istenen işlemi giriniz = "))
                        match islem:
                            case 1:
                                print(f"Bakiyeniz = {bakiye}")
                            case 2:
                                gelen_para = int(input("Yatırmak istenilen tutarı giriniz: "))
                                if gelen_para < 0:
                                    print("Yatırılmak istenilen tutar geçerli değil.")
                                else:
                                    bakiye += gelen_para
                                    print(f"{gelen_para} hesabınıza yatırıldı, yeni tutar = {bakiye}")
                            case 3:
                                giden_para = int(input("Çekilmek istenilen tutarı giriniz: "))
                                if giden_para > bakiye or giden_para < 0:
                                    print("Çekilmek istenilen tutar geçerli değil.")
                                else:
                                    bakiye -= giden_para
                                    print(f"{giden_para} hesabınızdan çekildi, yeni tutar = {bakiye}")
                            case 4:
                                print(f"Hoşçakal {username}!")
                                break
                            case _:
                                print("Girilen işlem tanımlanamaz, tekrar deneyiniz.")
                    except (TypeError, ValueError) as err:
                        print(f"{err} hatası sebebiyle giriş kabul edilmedi, girişinizi kontrol ediniz.")
            else:
                hak -= 1
                print(f"Giriş yanlış, kalan deneme hakkınız = {hak}")
        else:
            hak -= 1
            print(f"Giriş yanlış, kalan deneme hakkınız = {hak}")
