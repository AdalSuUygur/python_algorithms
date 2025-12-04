
#todo Sayı Tahmin ve Puanlama Oyunu (Hot/Cold)
# Bilgisayar random sayı üretecek ve kullanıcı 5 seferde tahmin etmeye çalışacak. Girilen sayıya göre SOĞUK SICAK uyarısı verilecek.
# try-except ile olası patlamaların önüne geç. 100 Puanı olsun oyuncunun, kazanırsa toplam puan yazsın ve döngüden çıksın, hakkı biterse kaybı ve hedef sayı yazılsın.


from random import randint
numara = randint(a= 0, b=100)
hak = 5
puan = 100
eksi_puan = puan / hak

while hak >= 0:
    if hak <= 0:
        print(f"Hakkınız bitti, kaybettiniz.\nTahmin etmeniz gereken sayı = {numara} idi.")
        break
    else: 
        try:
            tahmin = int(input("Tahmininizi giriniz: "))
            fark = numara - tahmin
            if fark < 0:
                fark = fark * (-1)
            if fark == 0:
                print(f"Tam isabet, kazandınız!\nToplam puan = {puan}\n")
                break
            elif fark <= 20:
                hak -= 1
                puan -= eksi_puan
                mesaj = "ÇOK SICAK"
            elif fark <= 40:
                hak -= 1
                puan -= eksi_puan
                mesaj = "SICAK"
            elif fark <= 60:
                hak -= 1
                puan -= eksi_puan
                mesaj = "ORTALAMA"
            elif fark <= 80:
                hak -= 1
                puan -= eksi_puan
                mesaj = "SOĞUK"
            elif fark <= 100:
                hak -= 1
                puan -= eksi_puan
                mesaj = "ÇOK SOĞUK"
            print(f"Yanlış giriş, tahmininiz {tahmin}\nKalan hak = {hak}\n")
        except (TypeError, ValueError) as err:
            print(f"{err} hatası nedeniyle girişiniz algılanamadı, lütfen tekrar deneyin.")
