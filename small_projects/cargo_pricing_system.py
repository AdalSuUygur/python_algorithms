
#todo Akıllı Lojistik Kargo Fiyatlandırma Sistemi
#Login mekanizması ve kargp ücreti hesabı: hatalı girişte programdan çık. giriş durumunda kargo ağırlığı, gideceği mesafe, kargo türü istenir: dosya, elektronik, mobilya
#dosyaysa 1,5; elektronikse 3, mobilyaysa 5 çarpan katsayısı, farklı girişse tanımsız.
#Girilen mesafe 600 km'den fazlaysa bir değişkene "Uzun Mesafe", değilse "Kısa Mesafe" metnini ata. Bunu tek satırlık if-else (ternary) yapısı ile yap.
#Formül: Fiyat = (Ağırlık * Mesafe * Katsayı) / 100
#Ekrana fiş yazdır, kargo türü, mesafesi, tutarı (virgülden sonra 2 basamak) şeklinde kullanıcıya göster.

kullanici_adi = "adal"
sifre = "1234"

username = input("İsminiz: ")
password = input("Şifreniz: ")
if username == kullanici_adi and password == sifre:
    print(f"Giriş başarılı, hoşgeldin {username}")
    while True:
        try:
            mesafe = float(input("Mesafeyi giriniz: "))
            if mesafe <= 0:
                print("Mesafe negatif değer olamaz")
            else:
                is_far = False if mesafe <= 600 else True
                weight = float(input(f"Kargo ağırlığını giriniz: "))
                while True:
                    tip = input("Kargo türünü giriniz: ")
                    match tip:
                        case "dosya":
                            katsayi = 1.5
                            break
                        case "elektronik":
                            katsayi = 3
                            break
                        case "mobilya":
                            katsayi = 5
                            break
                        case _:
                            print("Tanımsız, lütfen tekrar deneyin.")
                break
        except (ValueError, TypeError) as err:
            print(f"{err} sebebiyle kabul edilemez, tekrar deneyin.")
    fiyat = (weight * mesafe * katsayi) / 100
    print(f"Kargo türü: {tip}\nGideceği mesafe: {'Uzak' if is_far == True else 'Kısa'}\nTotal fiyat = {fiyat:.2f}")
else:
    print(f"Giriş yanlış, program kapatılıyor.")
    exit()