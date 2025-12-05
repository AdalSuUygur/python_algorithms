
#todo Login bilgileri eşleşirse, ürün search ve fiyat output.
#todo Yanlış loginde yeni kayıt. username'ler unique
users = [
    ["beast", "123"],
    ["bear", "456"],
    ["keko", "789"]
]

products = [
    ["Laptop", 850],
    ["Smartphone", 499],
    ["Headphones", 79],
    ["Keyboard", 45],
    ["Monitor", 220],
    ["Mouse", 25],
    ["Smartwatch", 150],
    ["Tablet", 310],
    ["External Hard Drive", 95],
    ["Webcam", 60],
    ["Laptop", 850]
]

#region kendi çözümüm

#endregion

#region hocanın çözümü
while True:
    first_process = input("Sign in için 1, Sign up için 2: ")
    match first_process:

        case 1:
            kullanici_adi = input("Username: ")
            sifre = input("Password: ")
            #burası login işlemi
            is_success = False #login başarılı mı değil mi kontrolümüz
            for user in users:
                if user[0] == kullanici_adi and user[1] == sifre:
                    is_success = True
                    break
            if is_success: #ayrı bir döngüde almamızın sebebi 3 kere aynı yazıyı bastırmamak
                print(f"Giriş başarılı, hoşgeldin {kullanici_adi}")
                #buraya tüm yapılacak işlemler gelecek, bunu dışarda yazıp içeri alabiliriz.

                while True:
                    second_process = input("İşlem adı giriniz: ")

                    match second_process:
                        case "toplam fiyat":
                            for product in products:
                                #1. indexlerde fiyatlar var
                                total += product[1]
                            print(f"Toplam fiyat: {total}")

                        case "laptop toplam fiyat":
                            for product in products:
                                if product[0] == "Laptop":
                                    total += product[1]
                                print(f"Toplam laptop fiyatı: {total}")

                        case "ürün ara":
                            urun_adi = input("Ürün adını giriniz: ")
                            for product in products:
                                if urun_adi == product[0]:
                                    print(f"Ürünün fiyatı: {product[0]}")
                                    break #birden fazla ürün olabilir.
                            else:
                                print("Böyle bir ürün yoktur.")

                        case "fiyat aralığına göre ara":
                            alt_sinir = int(input("Alt limit fiyatı: "))
                            ust_limit = int(input("Üst limit fiyatı: "))
                            for product in products:
                                if alt_sinir <= product[1] <= ust_limit:
                                    print(f"Ürününüz: {product[0]} fiyatı: {product[1]}")

                        case "çıkış":
                            print("Uygulama kapatılıyor.")
                            break

                        case _:
                            print("Lütfen işlem türü girdinizi kontrol ediniz.")

            else:
                print("Yanlış giriş bilgileri.")

        case 2:
            #sign in
            kullanici_adi = input("Username: ")
            sifre = input("Password: ")
            #sign up
            is_exists = False #üyeliği yokmuş ve üye olabilir gibi düşünüyoruz.
            for user in users:
                if user[0] == kullanici_adi: #0.indexinde usernameler var
                    is_exists = True #username var mı hali hazırda kontrol ediyoruz 
                    break
            if is_exists:
                print("Kullanıcı adı zaten var")
            else:
                new_user = [kullanici_adi, sifre]
                users.append(new_user)
                print("Üyelik işleminiz tamamlandı.")
            print(users) #test

        case _:
            print("Lütfen girdinizi kontrol ediniz.")
#endregion

