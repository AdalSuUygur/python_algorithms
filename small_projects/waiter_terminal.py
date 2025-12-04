
#todo Garson Terminali
#Müşteri masaya oturunca sistem açılacak ve sürekli sipariş alacak. Garson hesap diyene kadar döngü devam edecek.
# Çıktı: En sonda ekrana; İndirimsiz Tutar, İndirim Miktarı ve Ödenecek Net Tutarı yazdır.

sepet = 0

while True:
    siparis = input("Çorba, Kebap, Salata, İçecek giriniz: ").lower()
    match siparis:
        case "çorba":
            fiyat = 50
            sepet += fiyat
        case "kebap":
            fiyat = 150
            sepet += fiyat
        case "salata":
            fiyat = 40
            sepet += fiyat
        case "içecek":
            fiyat = 20
            sepet += fiyat
        case "hesap":
            if sepet >= 300:
                indirim = 0.1
                net_sepet = sepet * (1 - indirim)
            else:
                indirim = 0
                net_sepet = sepet * (1 - indirim)
            print(f"İndirimsiz tutar = {sepet}\nİndirim miktarı = %{indirim*100}\nÖdenecek net = {net_sepet}")
            break
        case _:
            print("Menüde böyle bir ürün yok.")