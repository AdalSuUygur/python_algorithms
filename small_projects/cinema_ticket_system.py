
#todo Şanslı Koltuklu Sinema Otomasyonu
# 3 haklı login 
# Başarılı login menüye ulaşır, menüde 2 seçenek: bilet al ve çıkış seçenekleri, 
# bilet al seçerse kaç tane bilet alınacak
# <10 bilet tanesi 250 tl; 10-20 arası 200 tl; >20 150 tl
# girilen bilet sayısı kadar koltuk numarası iste, eğer koltuk numarası asal bir sayı ise şanlsı koltuk indirimi yazdır ve %50 indirim uygula.
# total bilet fiyatını tüm biletlerin hesaplaması bitince döngüden çıkarak kullanıcıya göster ve ana menüye geri dön.

#3 haklı login
number_of_tries = 3

for i in range(1, (number_of_tries+1)):
    username = input("Username: ")
    password = input("Password: ")
    if username == "adal" and password == "1234":
        print("Login succesful!")
        #2 seçenekli menü seçeneği
        print("Welcome to the menu!")
        while True:
            options = input("1 for Ticket buy\n2 for exit\nPlease enter a input: ")
            match options:
                case "1": #Kaç tane bilet alınacağını soracağız
                    try:
                        count_ticket = int(input("How much ticket you wanted to buy: "))
                        base_price = 0
                        if 0 < count_ticket < 10:
                            base_price = 250
                        elif 10 < count_ticket <= 20:
                            base_price = 200
                        elif count_ticket > 20:
                            base_price = 150
                        else:
                            print("Please enter a valid number.")
                    except (ValueError, TypeError) as err:
                        print("Because of the {err} we cannot continue, please try again.")
                    print(f"Unit Price determined as: {base_price} TL") #Buraya kadar baz fiyatı öğrendik.
                    total_payment = 0
                    for j in range(1, count_ticket+1):
                        try: #seat number istedik
                            seat_number = int(input(f"Please enter {j}. seat's number."))
                        except (TypeError, ValueError) as err:
                            print("Invalid seat  because of {err}!")
                        is_asal = True #ve dedik ki asal kabul edelim
                        if seat_number < 2:
                            is_asal = False
                        else:
                            for k in range(2, seat_number):
                                if seat_number % k == 0:
                                    is_asal = False
                                    break #Burda artık sayım asal mı değil mi net olarak biliyorum.
                        current_seat_price = base_price # Baz fiyatı geçici değişkene aldık
                        if is_asal:
                            print(f"Lucky Seat! ({seat_number}) is Prime! %50 Discount applied.")
                            current_seat_price = current_seat_price * 0.5
                        total_payment += current_seat_price
                        print(f"Ticket #{j} added. Price: {current_seat_price} TL")
                    print(f"\n💰 Transaction Complete! Total Amount to Pay: {total_payment} TL\n")
                #buraya kod gelecek.
                case "2":
                    print("Program is shutting down.")
                    break
                case _:
                    print("This entry is not on the menu, please try again.")
    else:
        print(f"Wrong credentials.\nRemaining tries = {number_of_tries - i}")
        if i == number_of_tries:
            print("Your tries has ended, program is shutting down.")
            exit()
