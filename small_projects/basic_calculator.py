
#todo Calculator uygulaması
#Kullanıcı login olacak ve successfully loginde uygulamaya erişecek. Yanlış giriş hakkı 3 olacak.
#Calculator uygulamasında +, -, *, /, e(çıkış) olacak.
#İstenen kalıplar:  try except bloğu, infinitive loop, match case

#region Fonksiyon kurarak, kullanıcıları list datasından çekerek yapılan uygulama
users = [
    ["beast", "123"],
    ["bear", "456"],
    ["keko", "789"]
]

def is_login(username, password, users_data):
    for USERNAME, PASSWORD in users_data:
        if username == USERNAME and password == PASSWORD:
            return True
    return False

def calculator(operator, number1, number2):
    match operator:
        case "+":
            return number1 + number2
        case "-":
            return number1 - number2
        case "*":
            return number1 * number2
        case "/":
            return number1 / number2

def is_register(new_username, new_password, users_data):
    for USERNAME, PASSWORD in users_data:
        if new_username == USERNAME:
            return False # Kullanıcı adı zaten alınmış, kayıt başarısız
    
    # Başarılıysa
    users_data.append([new_username, new_password])
    return True # Kayıt başarılı

MAX_ATTEMPTS = 3
attemps = 0

while attemps < MAX_ATTEMPTS:
    username = input("Username: ")
    password = input("Password: ")
    login_successful = is_login(username, password, users)
    if login_successful:
        break
    else:
        attemps += 1
        if attemps < MAX_ATTEMPTS: # Hak bitmediyse uyarı ver
            print(f"Hatalı kullanıcı adı veya şifre. Kalan deneme hakkınız: {MAX_ATTEMPTS - attemps}")

if login_successful:
    print("Login successful")
    while True:
        try:
            operator = input("Please enter mathematical operation you would do, e for exit: ")
            if operator == "e":
                break
            elif operator not in ["+", "-", "*", "/"]:
                print("Couldn't find operator")
            else:
                num1 = float(input("Please enter your first number: "))
                num2 = float(input("Please enter your second number: "))
                result = calculator(operator, num1, num2)
                print(result)
        except (TypeError, ValueError, ZeroDivisionError) as err:
            print(f"Because of {err} we cannot continue, please try again.")
else:
    print("Login unsuccessful.")
    register_input = input("Would you like to register? (Y/N): ").upper()
    if register_input == "Y":
        username = input("Username: ")
        password = input("Password: ")
        if is_register(username, password, users): #burda her türlü programdan çıkıyor. Geri dönmüyor.
            print(f"Register successful. Welcome {username}")
        else:
            print("Please enter another username since this one already taken.")
#endregion

#region Hopefully last try ^^ (28.11.25) **DRY prensibine uyamadım. Will try again!

# username = "adal"
# password = "123"
# #isim ve şifre belirledik
# hak = 3
# while hak > 0:
# #kullanıcıdan da istedik neden döngü içinde, her seferinde sorabilmek için
#     user_name = input("Username: ")
#     pass_word = input("Password: ")
#     if user_name == username and pass_word == password:
#         print("Login successful") #login olduk ama hak için bir şey yapmadık. Test lazım.
#         while True:
#             try:
#                 n1 = int(input("Number1: "))
#                 n2 = int(input("Number2: "))
#                 operation = input("Enter desired matematical operation, e for exit: ")
#                 match operation:
#                     case "+":
#                         result = n1 + n2
#                         print(f"Your calculation is : {n1} {operation} {n2} = {result}") #DRY prensibine uyamadım.
#                     case "-":
#                         result = n1 - n2
#                         print(f"Your calculation is : {n1} {operation} {n2} = {result}")
#                     case "*":
#                         result = n1 * n2
#                         print(f"Your calculation is : {n1} {operation} {n2} = {result}")
#                     case "/":
#                         result = n1 / n2
#                         print(f"Your calculation is : {n1} {operation} {n2} = {result}")
#                     case "e":
#                         print("Exiting the program.")
#                         break
#                     case _:
#                         print("Invalid entry, try again.")
#             except (ValueError, TypeError, ZeroDivisionError) as err:
#                 print(f"Cannot continue because of ({err}), try again.")
#     else:
#         print(f"Login denied!, remaining tries = {hak - 1}")
#         hak -= 1 #döngüye sokacağız mecbur, burda da hakkımızı düşürdük.
# print("Hakkınızı yitirdiniz, bye!") #While döngüsünden çıktığımızda hakkımız kalmamış olcak.

#endregion

#region First Try
# while i < try_count: #Sayacımız try_count kadar devam edicek
#     username = input("Username: ") #Username istedik
#     if username == "Adal": #Eğer doğruysa
#         password = input("Password: ") #Şifre istedik
#         if password == "1234": #Şifre doğrusa
#             print("Login successful! Welcome.") #Giriş yapıldığını söyledik.
#             login_successful = True #Artık login_successfull değişkenimiz true oldu ve döngüyü sonlandırdık.
#             break
#         else:
#             print("Incorrect password.") #Yanlışsa bunu kullanıcıya bildirdik ve 
#             i += 1 #sayacı artırdık.
#     else: #Kullanıcı adı yanlışsa:
#         print(f"Uncorrect username, please try again.")
#         i += 1 #Sayacı 1 artırdık.
#     if login_successful == False:
#         if (try_count - i) > 0:
#             print(f"You have {try_count - i} tries left")
#         else:
#             print("No more tries left. Account locked.")

#endregion

#region Second Try GEREKSİZ KARMAŞIK BU NE OKUNMUYO BİLE KADIN
# while (i+j) < try_count: #Sayacımız try_count kadar devam edicek
#     username = input("Username: ") #Username istedik
#     if username == "Adal": #Eğer doğruysa
#         while i+j < try_count:
#             password = input("Password: ") #Şifre istedik
#             if password == "1234": #Şifre doğrusa
#                 print("Login successful! Welcome.") #Giriş yapıldığını söyledik.
#                 login_successful = True #Artık login_successfull değişkenimiz true oldu ve döngüyü sonlandırdık.
#                 break
#             else:
#                 print("Incorrect password.") #Yanlışsa bunu kullanıcıya bildirdik ve 
#                 j += 1 #sayacı artırdık.
#                 print(f"You have {try_count - (i+j)} tries left")
#     else: #Kullanıcı adı yanlışsa:
#         print(f"Uncorrect username, please try again.")
#         i += 1 #Sayacı 1 artırdık.
#         print(f"You have {try_count - (i+j)} tries left")
#     if login_successful == False:
#         if (try_count - (i+j)) > 0:
#             pass
#         else:
#             print("No more tries left. Account locked.")
#     else:
#         print("happy happy happy") #Buraya calculator
#         while login_successful == True:
#             # stop_attemt = input("Write "STOP" for closing the program.: ").lower()
#             if stop_attemt == "stop":
#                 print("Program is shutting down.")
#                 break #döngüden çıkıyoruz.
#             calculator = input("Desired Mathematical Operation: ")
#             if not calculator in ["+", "-", "*", "/"]:
#                 pass
#             else:
#                 number1 = float(input("First number: "))
#                 number2 = float(input("Second number:  "))
#                 #try: buraya input olarak string kabul etmemeliyiz
#                 #except:
#                 match calculator:
#                     case "+":
#                         result = number1 + number2
#                     case "-":
#                         result = number1 - number2
#                     case "*":
#                         result = number1 * number2
#                     case "/":
#                         if number2 == 0:
#                             pass
#                             # try:
#                             # except:
#                         else:
#                             result = number1 / number2
#                     case "e":
#                         pass
#                     case _:
#                         #Buraya loop koyalım ve diyelim ki doğru işareti girene kadar devam
#                         pass

#endregion

#region Third Try
# i = 0
# try_count = 3
# USERNAME = "Adal"
# PASSWORD = "1234"
# login_successful = False

# while i < try_count:
#     username = input("Username: ")
#     if username == USERNAME:
#         while i < try_count:
#             password = input("Password: ")
#             if password == PASSWORD:
#                 print("Correct password.")
#                 login_successful = True
#                 break
#             else:
#                 i += 1
#                 print(f"Password is wrong, please try again.\nTry count = {i}\nRemaining try count = {try_count - i}")
#         print("Correct username.")
#         break
#     else:
#         i += 1
#         print(f"Username is wrong, please try again.\nTry count = {i}\nRemaining try count = {try_count - i}")

# if login_successful == True:
#     print("Login successful.")
#     while True:
#         operator = input("Please enter the mathematical expression you want to calculate (+, -, *, /, e(to exit)): ")
#         if operator in ["+", "-", "*", "/", "e"]:
#             while True:
#                 try:
#                     number1 = float(input("Number 1: "))
#                     break
#                 except ValueError as err:
#                     print("Please enter invalid number.")
#             while True:
#                 try:
#                     number2 = float(input("Number 2: "))
#                     break
#                 except ValueError as err:
#                     print("Please enter invalid number.")
#             match operator:
#                 case "+":
#                     result = number1 + number2
#                 case "-":
#                     result = number1 - number2
#                 case "*":
#                     result = number1 * number2
#                 case "/":
#                     while number2 == 0:
#                         try:
#                             number2 = float(input("Please re-enter the divisor number: "))
#                         except (ZeroDivisionError, ValueError) as err:
#                             print("You cannot divide a number to 0 or another letter, please check your number.")
#                     result = number1 / number2
#                 case "e":
#                     print("Program is shutting down.")
#                     exit()
#             print(f"Your calculation is: {number1} {operator} {number2} = {result}")
#         else:
#             print("You are attempting an undefined operation, please try again.")
# else:
#     print("You've consumed all of your tries, program is shutting down.") #Buraya programdan çıkış
#     exit()
#endregion