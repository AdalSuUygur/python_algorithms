
#todo Calculator uygulaması
#Kullanıcı login olacak ve successfully loginde uygulamaya erişecek. Yanlış giriş hakkı 3 olacak.
#Calculator uygulamasında +, -, *, /, e(çıkış) olacak.
#İstenen kalıplar:  try except bloğu, infinitive loop, match case

login_attempt = 3
USERNAME = "Adal"
PASSWORD = "1234"
while login_attempt > 0:
    username = input("Kullanıcı adı: ")
    password = input("Şifre: ")
    if username == USERNAME:
        if password == PASSWORD:
            print("Bilgiler doğru, hoşgeldiniz.")
            while True:
                operator = input("Yapılmak istenen işlemi (+, -, *, /, x(Çıkış)) giriniz: ")
                if operator == "+" or operator == "-" or operator == "*" or operator == "/":
                #veya: if operator in ["+", "-", "*", "/"]:
                    while True:
                        try:
                            number1 = float(input("Birinci sayı: "))
                            number2 = float(input("İkinci sayı: "))
                            match operator:
                                case "+":
                                    result = number1 + number2
                                case "-":
                                    result = number1 - number2
                                case "*":
                                    result = number1 * number2
                                case "/":
                                    result = number1 / number2
                            print(f"İstenen işlemin sonucu\n{number1} {operator} {number2} = {result}")
                            break
                        except (ValueError, ZeroDivisionError, TypeError, NameError) as err:
                            print(f'{err} hatası nedeniyle işlem yapılamaz, lütfen girdinizi kontrol ediniz ve tekrar deneyiniz.')
                elif operator == "x":
                    print("Programdan çıkılıyor.")
                    break
                else:
                    print("Yanlış değer girildi, lütfen tekrar deneyin.")
        else:
            login_attempt -= 1
            print(f"Yanlış giriş. Kalan hak: {login_attempt}")
    else:
        login_attempt -= 1
        print(f"Yanlış giriş. Kalan hak: {login_attempt}")