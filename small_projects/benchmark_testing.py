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