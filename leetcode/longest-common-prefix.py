# 14. Longest Common Prefix

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

strs = ["flower", "flow", "flight"]

# 1. REFERANS KELİMEYİ BULMA (Kodu hızlandırır)
# Başlangıçta 0. kelimeyi referans alalım
kontrol = strs[0] 

# En kısa kelimeyi bul (Bu kısım doğru çalışıyor)
for kelime in strs:
    if len(kelime) < len(kontrol):
        kontrol = kelime
# kontrol = "flow"

# 2. DİKEY TARAMA (LCP Mantığı)
# Dış Döngü (i): Referans kelimenin harfleri (pozisyonları) üzerinde gezinir
for i in range(len(kontrol)):
    referans_karakter = kontrol[i] 

    # İç Döngü (j): strs listesindeki 0. kelimeden (kendisi dahil) başlayıp sonuna kadar gezer
    for j in range(len(strs)): 
        
        # SADECE eşleşmeme durumunu kontrol et
        if strs[j][i] != referans_karakter:
            
            # Eşleşme bozuldu! 🛑
            # i pozisyonuna kadar olan kısmı döndür ve programı bitir.
            # Örn: i=2'de (o/i) bozulduysa, 0. ve 1. pozisyonları (fl) döndürür.
            print(kontrol[:i]) 
            # Normalde bu bir fonksiyon içinde olacağı için return kullanırdık.
            exit() 

# Eğer tüm döngüler HİÇBİR İHTİLAF olmadan biterse (tüm kelimeler eşleşirse),
# o zaman en kısa kelimenin (kontrol) tamamı ortaktır.
print(kontrol)
#bunu yaptım ama gemini yardımıyla, tekrar üstünden gitmem ŞART


