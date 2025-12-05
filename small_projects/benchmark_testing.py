#todo Benchmark testing between without tryExcept / tryExcept / raiseException

# import time
# import tracemalloc

# bolunen = 2
# bolen = 0
# test1 = "IF_ELSE"
# test2 = "TRY_EXCEPT"
# test3 = "RAISE_EXCEPTION"

# #region Kendi çözümüm

# def path_1(bolunen, bolen):
#     if bolen == 0:
#         return "Sıfıra bölünme hatası (IF/ELSE ile yakalandı)"
#     else:
#         bolum = bolunen / bolen
#         return bolum

# def path_2(bolunen, bolen):
#     try:
#         bolum = bolunen / bolen
#     except (ZeroDivisionError) as err:
#         bolum = f"Sıfıra bölünme hatası (TRY/EXCEPT ile yakalandı): {err}"
#     return bolum

# def path_3(bolunen, bolen):
# # Bu metotta bilerek ZeroDivisionError yerine başka bir hata fırlatıyoruz.
#     if bolen == 0:
#         # Kendi hata tipimizi fırlatıyoruz.
#         raise ValueError("Özel Hata: Bölen sıfır olamaz!")        
#     return bolunen / bolen

# def benchmart_test(bolunen_deger, bolen_deger, test_adi):
#         # 1. TEST FONKSİYONUNU SEÇME
#     if test_adi == "IF_ELSE":
#         test_func = path_1
#     elif test_adi == "TRY_EXCEPT":
#         test_func = path_2
#     elif test_adi == "RAISE_EXCEPTION":
#         test_func = path_3
#     else:
#         raise ValueError("Tanımsız test adı!")

#     tracemalloc.start()
#     t1 = time.perf_counter()

#     # path_3 (RAISE_EXCEPTION) bir hata fırlatacağı için, onu da yakalamamız lazım.
#     try:
#         # Seçilen fonksiyonu çağırıyoruz
#         result = test_func(bolunen_deger, bolen_deger)
#     except ValueError as e:
#         # path_3'ten gelen özel hatayı yakala
#         result = str(e)

#     t2 = time.perf_counter()
#     current, peak = tracemalloc.get_traced_memory()
#     tracemalloc.stop()

#     runtime_ms = (t2 - t1) * 1000 
#     peak_memory = peak / 1024
    
#     return runtime_ms, peak_memory, result

# runtime_memory1, peak_memory1, islem_sonucu1 = benchmart_test(bolunen, bolen, test1)
# runtime_memory2, peak_memory2, islem_sonucu2 = benchmart_test(bolunen, bolen, test2)
# runtime_memory3, peak_memory3, islem_sonucu3 = benchmart_test(bolunen, bolen, test3)

# print(
#     f'Method --> {test1}\n'
#     f'Runtime: {runtime_memory1:.6f} ms\n'
#     f'Peak Memory: {peak_memory1:.6f} KB\n'
#     f'Result: {islem_sonucu1}\n'
#     '===============================\n'
#     f'Method --> {test2}\n'
#     f'Runtime: {runtime_memory2:.6f} ms\n'
#     f'Peak Memory: {peak_memory2:.6f} KB\n'
#     f'Result: {islem_sonucu2}\n'
#     '===============================\n'
#     f'Method --> {test3}\n'
#     f'Runtime: {runtime_memory3:.6f} ms\n'
#     f'Peak Memory: {peak_memory3:.6f} KB\n'
#     f'Result: {islem_sonucu3}'
# )




# #todo Benchmark testing between listComprehension / lambdaFilter / forLoop
# #Random sayılardan oluşan bir liste üretilir (a=-100, b=100)
# #Path1 ile list comprehension, Path2 ile lambda filter, Path3 ile for loop ile pozitif sayılar ayıklanır.
# #Bu pathler arasında benchmark testi yapılır.

# #region Benchmark testing kendi çözümüm
# from time import time_ns #nanosecond olarak ölçmeye yarayan fonksiyon
# from random import randint #random sayı üretmeye yarayan fonksiyon
# timer_start = time_ns()
# timer_finish = time_ns()
# import sys #sys modülünü çektik

# #numbers = [randint(a=-100, b=100) for i in range(10000)] #numbers diye 10000 itemlı liste oluşturuldu
# #bilgisayar zorlansın diye adet değişkeni tanımladım, ayrıca teste de yardımcı oldu.

# ADET = 1_000_000 
# print(f"{ADET} adet sayı üretiliyor, lütfen bekleyiniz")
# # Sayı üretme süresini teste dahil etmiyoruz, o yüzden dışarıda yapıyoruz.
# numbers = [randint(a=-100, b=100) for i in range(ADET)]
# print("Sayılar üretildi, yarış başlıyor!\n" + "-"*50)


# # --- PATH 1: List Comprehension ---
# timer_start = time_ns() # Kronometreyi başlat

# path_1 = [number for number in numbers if number > 0]
# #print(path_1) #test

# timer_finish = time_ns() # Kronometreyi durdur
# sure_path1 = timer_finish - timer_start

# size_path1 = sys.getsizeof(path_1) # Bellek Boyutu Ölçümü

# print(f"Path 1 (List Comp) : {sure_path1:,} ns") #Okunabilirlik için binlik ayırıcı (,)
# print(f"  Bellek Boyutu (Tahmini): {size_path1:,} byte")

# del path_1 # Belleği serbest bırak


# # --- PATH 2: Filter + Lambda ---
# timer_start = time_ns() # Kronometreyi başlat

# path_2 = list(filter(lambda x: x>0, numbers))
# #print(path_2) #test

# timer_finish = time_ns() # Kronometreyi durdur

# sure_path2 = timer_finish - timer_start
# size_path2 = sys.getsizeof(path_2) # Bellek Boyutu Ölçümü

# print(f"Path 2 (Filter)    : {sure_path2:,} ns")
# print(f"  Bellek Boyutu (Tahmini): {size_path2:,} byte")

# del path_2


# #PATH3 for loop
# timer_start = time_ns() # Kronometreyi başlat

# path_3 = []
# for number in numbers:
#     if number > 0:
#         path_3.append(number)
# #print(path_3) #test

# timer_finish = time_ns() # Kronometreyi durdur
# sure_path3 = timer_finish - timer_start

# size_path3 = sys.getsizeof(path_3)

# print(f"Path 3 (For Loop)  : {sure_path3:,} ns")
# print(f"  Bellek Boyutu (Tahmini): {size_path3:,} byte")
# del path_3


# print("-" * 30)


# en_hizli = min(sure_path1, sure_path2, sure_path3)
# if en_hizli == sure_path1: print("KAZANAN: Path 1 (List Comprehension)")
# elif en_hizli == sure_path2: print("KAZANAN: Path 2 (Filter)")
# else: print("KAZANAN: Path 3 (For Loop)")
# #endregion

# #region Benchmark Testing Hocanın Çözümü
# from random import randint
# import time
# import tracemalloc


# tracemalloc.start()
# t1 = time.perf_counter()

# # Sayı yaratırken aşağıdaki list comprehension kullanmak yerine generator pattern kullansaydınız işin rengi baya değişirdi. 
# # Sayı üretim hızı dramatik birşekilde artardı ve zaman maliyeti azalırdı.
# # numbers = [randint(a=-100, b=100) for _ in range(1000000)]
# numbers = (randint(a=-100, b=100) for _ in range(1000000))

# # List Comprehension
# positive_number = [number for number in numbers if number > 0]

# # Filter Func
# # positive_number = list(filter(lambda x: x > 0, numbers))

# # With For Loop
# # positive_number = []
# # for number in numbers:
# #     if number > 0:
# #         positive_number.append(number)

# print(positive_number)

# t2 = time.perf_counter()
# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()

# runtime_ms = (t2 - t1) * 1000
# peak_memory = peak / 1024 / 1024

# print(
#     '===============================\n'
#     'Method --> List Comprehension\n'
#     f'Runtime: {runtime_ms}\n'
#     f'Peak Memory: {peak_memory}'
    
# )

# """
# ===============================
# Method --> List Comprehension
# Runtime: 5728.366099996492
# Peak Memory: 28.39721393585205
# ===============================
# Method --> Filter Func
# Runtime: 3872.5149999954738
# Peak Memory: 28.40944004058838
# ===============================
# Method --> With For Loop
# Runtime: 4765.219499997329
# Peak Memory: 28.41720485687256
# """
# #endregion