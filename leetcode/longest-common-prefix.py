# 14. Longest Common Prefix

#* hala yapamıyorum :tear

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

strs = ["flower","flow","flight"]

# 1. min(strs) yapsaydık:
# Alfabetik sıraya göre karşılaştırır: "flight" < "flow" < "flower"
# Çıktı: 'flight' (Alfabetik olarak en küçük)

# 2. min(strs, key=len) yaptığımızda:
# Uzunlukları karşılaştırır: 4 < 6. En küçüğü 4'tür.
# Çıktı: 'flow' (Uzunluk olarak en küçük)

denek_kelime = min(strs, key=len) # çıktı olarak bana "flow" vermesi lazım, listedeki en kısayı denek kelime olarak alıyorum ki diğerleriyle kıyaslayabileyim.

for i in range(len(denek_kelime)):  #<-- Dış Döngü (M kadar döner)
    for kelime in strs:              #<-- İç Döngü (N kadar döner)
        if kelime[i] != denek_kelime[i]:
            pass
            #return strs[0][:i]      #<-- ERKEN ÇIKIŞ!


# strs[0][0] #yani 0. itemın 0. harfini (çünkü bu da string yani liste) kez checkliyorum, diğerlerinde ortak mı diye? hangisine bakıyoruz onların da 0. karakterine
# #ortaksa
# strs[0][1] #artık itemın 1. harfine geçiyoruz ve diğerlerinde de aynı mı diye checkliyoruz
# #... ve bu ortak bulamayana kadar devam ediyor.
# denek_kelime = strs[0]

    


#region gemini yardımıyla çözüm
# strs = ["flower", "flow", "flight"]

# # 1. REFERANS KELİMEYİ BULMA (Kodu hızlandırır)
# # Başlangıçta 0. kelimeyi referans alalım
# kontrol = strs[0] 

# # En kısa kelimeyi bul (Bu kısım doğru çalışıyor)
# for kelime in strs:
#     if len(kelime) < len(kontrol):
#         kontrol = kelime
# # kontrol = "flow"

# # 2. DİKEY TARAMA (LCP Mantığı)
# # Dış Döngü (i): Referans kelimenin harfleri (pozisyonları) üzerinde gezinir
# for i in range(len(kontrol)):
#     referans_karakter = kontrol[i] 

#     # İç Döngü (j): strs listesindeki 0. kelimeden (kendisi dahil) başlayıp sonuna kadar gezer
#     for j in range(len(strs)): 
        
#         # SADECE eşleşmeme durumunu kontrol et
#         if strs[j][i] != referans_karakter:
            
#             # Eşleşme bozuldu! 🛑
#             # i pozisyonuna kadar olan kısmı döndür ve programı bitir.
#             # Örn: i=2'de (o/i) bozulduysa, 0. ve 1. pozisyonları (fl) döndürür.
#             print(kontrol[:i]) 
#             # Normalde bu bir fonksiyon içinde olacağı için return kullanırdık.
#             exit() 

# # Eğer tüm döngüler HİÇBİR İHTİLAF olmadan biterse (tüm kelimeler eşleşirse),
# # o zaman en kısa kelimenin (kontrol) tamamı ortaktır.
# print(kontrol)
#endregion