
#todo Geometri Sistemi ve harf notu hesaplama sistemi
#Kullanıcı login olacak ve successfully loginde uygulamaya erişecek. Başarısız girişte program sonlandırılır.
#Giriş başarılı olunca G(Geometri), H(Harf notu hesaplama), S(Stop) erişimi bunlar dışında girerse hata mesajı verir ve menü seçenekleri sorulur.
#dikdörtgen, üçgen, daire, yamuk VEYA vize final notu hesabı

#region Kendi çözümüm
USERNAME = "Adal"
PASSWORD = "1234"

username = input("Username: ")
password = input("Password: ")

def wrong_credentials():
    #Hata mesajı verir ve programı kapatır.
    print("Wrong credentials. Program is shutting down.")
    exit()

if username == USERNAME:
    if password == PASSWORD:
        print("Welcome to the app")
        #Uygulama kod bloğu buraya gelmeli
    else:
        wrong_credentials()
else:
    wrong_credentials()

def wrong_entry():
    #Kullanıcı olması gerekenden farklı bir giriş yaptığında döner.
    print("There is a mistake in your entry, please try again.")

while True:
    applications = input(f"G for Geometri app\nH for Grade app\nS to stop the program\nPlease enter a character: ").lower()
    match applications:
        case "g":
            while True: 
                shape = input("Please enter your shape(R for returning the previous menu): ").lower()
                try: #Buraya caselerin dışında entry girince hata veriyor.
                    match shape:
                        case "rectangle":
                            edge_first = float(input("Enter first edge: "))
                            edge_second = float(input("Enter second edge: "))
                            area = edge_first * edge_second
                            premiter = 2 * (edge_first + edge_second)
                        case "triangle":
                            #Heron'un üçgen alanı hesabı ile yapıyorum, geminiledim.
                            edge_first = float(input("Enter first edge: "))
                            edge_second = float(input("Enter second edge: "))
                            edge_third = float(input("Enter third edge: "))
                            premiter = edge_first + edge_second + edge_third
                            s = premiter / 2 #heronun formülünde paso kullanıyoz.
                            area = (s * (s - edge_first) * (s- edge_second) * (s- edge_third)) ** 0.5 # ** üs alma operatörü
                        case "trapezoid":
                            edge_top = float(input("Enter top edge: "))
                            edge_bottom = float(input("Enter bottom edge: "))
                            edge_side_1 = float(input("Enter side edge: "))
                            edge_side_2 = float(input("Enter second side edge: "))
                            h = float(input("Enter vertical height: "))
                            area = (edge_top + edge_bottom) * h / 2
                            premiter = edge_top + edge_bottom + edge_side_1 + edge_side_2
                        case "circle":
                            pi = 3.1415
                            r = float(input("Enter circle's radius: "))
                            area = pi * (r ** 2)
                            premiter = 2 * pi * r
                        case "r":
                            print("Returning the main menu")
                            break
                        case _:
                            wrong_entry()
                    print(f"Desired shape: {shape.capitalize()}\nPremiter: {premiter:.2f}\nArea: {area:.2f}") # :.2f ifadesi virgülden sonraki 2 basamağı gösteriyor.
                except (TypeError, ValueError) as err:
                    wrong_entry()
                    print(err)

        case "h": 
            while True:
                is_return = input("R for returning the previous menu: ").lower()
                if is_return == "r":
                    break
                else:
                    while True:
                        try:
                            midterm_first = int(input("Please enter your first midterm grade: "))
                            midterm_second = int(input("Please enter your second midterm grade: "))
                            final = int(input("Please enter your final grade: "))
                            if 0 <= midterm_first <= 100 and 0 <= midterm_second <= 100 and 0 <= final <= 100:
                                grade = (midterm_first * 0.3) + (midterm_second * 0.3) + (final * 0.4)
                                is_pass = True #Yani belki ilerde geçti mi kaldı mı sorgusunu yaparsam diye
                                if 0 < grade <= 30:
                                    letter_grade = "FF"
                                    is_pass = False
                                elif 30 < grade <= 45:
                                    letter_grade = "DD"
                                    is_pass = False
                                elif 45 < grade <= 50:
                                    letter_grade = "DC"
                                elif 50 < grade <= 60:
                                    letter_grade = "CC"
                                elif 60 < grade <= 70:
                                    letter_grade = "CB"
                                elif 70 < grade <= 85:
                                    letter_grade = "BB"
                                elif 85 < grade <= 90:
                                    letter_grade = "BA"
                                elif 90 < grade <= 100:
                                    letter_grade = "AA"
                                print(f"Your avarage is {grade} and its equevelant letter grade is: {letter_grade}")
                                break
                            else:
                                wrong_entry()
                        except (TypeError, ValueError) as err:
                            wrong_entry()
                            print(err)

        case "s":
            print("Program is closing.")
            break
        case _:
            wrong_entry()
#endregion

#region İpek Çözümü
# USERNAME = "Adal"
# PASSWORD = "1234"

# def wrong_credentials():
#     print("Wrong credentials. Program is shutting down.")
#     exit()

# def wrong_entry():
#     print("There is a mistake in your entry, please try again.")

# # ---------- LOGIN ----------
# username = input("Username: ")
# password = input("Password: ")

# if username == USERNAME and password == PASSWORD:
#     print("Welcome to the app")
# else:
#     wrong_credentials()

# # ---------- ANA MENÜ ----------
# while True:
#     applications = input(
#         "\nG for Geometry app\n"
#         "H for Grade app\n"
#         "S to stop the program\n"
#         "Please enter a character: "
#     ).lower()

#     match applications:

#         # ---------------- GEOMETRİ ----------------
#         case "g":
#             while True:
#                 shape = input(
#                     "Please enter your shape (rectangle, triangle, trapezoid, circle)\n"
#                     "R for returning the previous menu: "
#                 ).lower()

#                 try:
#                     match shape:
#                         case "rectangle":
#                             edge_first = float(input("Enter first edge: "))
#                             edge_second = float(input("Enter second edge: "))
#                             area = edge_first * edge_second
#                             premiter = 2 * (edge_first + edge_second)

#                         case "triangle":
#                             edge_first = float(input("Enter first edge: "))
#                             edge_second = float(input("Enter second edge: "))
#                             edge_third = float(input("Enter third edge: "))
#                             premiter = edge_first + edge_second + edge_third
#                             s = premiter / 2
#                             area = (s * (s - edge_first) * (s - edge_second) * (s - edge_third)) ** 0.5

#                         case "trapezoid":
#                             edge_top = float(input("Enter top edge: "))
#                             edge_bottom = float(input("Enter bottom edge: "))
#                             edge_side_1 = float(input("Enter side edge: "))
#                             edge_side_2 = float(input("Enter second side edge: "))
#                             h = float(input("Enter vertical height: "))
#                             area = (edge_top + edge_bottom) * h / 2
#                             premiter = edge_top + edge_bottom + edge_side_1 + edge_side_2

#                         case "circle":
#                             pi = 3.1415
#                             r = float(input("Enter circle's radius: "))
#                             area = pi * (r ** 2)
#                             premiter = 2 * pi * r

#                         case "r":
#                             print("Returning to main menu...")
#                             break

#                         case _:
#                             wrong_entry()
#                             continue

#                     print(
#                         f"Desired shape: {shape.capitalize()}\n"
#                         f"Premiter: {premiter:.2f}\n"
#                         f"Area: {area:.2f}"
#                     )

#                 except (TypeError, ValueError) as err:
#                     wrong_entry()
#                     print(err)

#         # ---------------- HARF NOTU (IF / ELIF İLE) ----------------
#         case "h":
#             while True:
#                 action = input("C to calculate grade, R to return main menu: ").lower()

#                 match action:

#                     case "r":
#                         print("Returning to main menu...")
#                         break

#                     case "c":
#                         try:
#                             m1 = int(input("Enter first midterm: "))
#                             m2 = int(input("Enter second midterm: "))
#                             final = int(input("Enter final exam: "))

#                             if not (0 <= m1 <= 100 and 0 <= m2 <= 100 and 0 <= final <= 100):
#                                 wrong_entry()
#                                 continue

#                             grade = m1 * 0.3 + m2 * 0.3 + final * 0.4

#                             # ----- IF / ELIF KULLANILAN KISIM -----
#                             if 0 <= grade <= 30:
#                                 letter = "FF"
#                             elif 30 < grade <= 45:
#                                 letter = "DD"
#                             elif 45 < grade <= 50:
#                                 letter = "DC"
#                             elif 50 < grade <= 60:
#                                 letter = "CC"
#                             elif 60 < grade <= 70:
#                                 letter = "CB"
#                             elif 70 < grade <= 85:
#                                 letter = "BB"
#                             elif 85 < grade <= 90:
#                                 letter = "BA"
#                             elif 90 < grade <= 100:
#                                 letter = "AA"
#                             else:
#                                 wrong_entry()
#                                 continue

#                             print(f"\nAverage: {grade:.2f} → Letter Grade: {letter}")

#                         except (TypeError, ValueError):
#                             wrong_entry()

#                     case _:
#                         wrong_entry()

#         # ---------------- PROGRAM STOP ----------------
#         case "s":
#             print("Program is closing...")
#             break

#         case _:
#             wrong_entry()

#endregion