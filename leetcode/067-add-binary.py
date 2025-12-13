# 67. Add Binary

# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

a = "1011"
b = "1"

#region deneme2 - 2'lik sistemde toplamaları tersten yapmaya çalışıyorum

#1. adım: string nesnelerini ters çevir.
# reversed(a)
# reversed(b)

#2. adım: Bunları birleştir. zip(reversed(a),reversed(b))

#3. adım Bu zip nesnesindeki aynı indexteki string ifadeleri integera çevir ve topla. (int(x) + int(y) for x,y in zip(reversed(a),reversed(b)))

#*Burda tıkanıyoruz.
#0. indexteki ifadelerin toplamı (Yani, normalde 2^0. basamak, yani 10'luk sistemdeki birler basamağı) 2 ise, 01 olarak yaz ve tersten düşünmesi aşırı zor

#* Düzden düşünecek olursam:
#* eşit basamak olmadığı taktirde nasıl yapıcam? kısa olana 0 eklemek bir çözüm değil sayıyı büyütür, başına 0 eklemek?
#* şu an daha mantıklı oldu gibi.
#yorumlarda birisi böyle demiş, acaba 10luk sisteme geçirmeden çözebilir miyim? ama en sağdan başlamam lazım, listenin sonundan ya da?
# 1+1=0 with carry 1
# 1+0=1 with carry 0
# 0+1=1 with carry 0
# 0+0=0 with carry 0
# Imp:1+1=1 with carry 1 if previous carry was 1.
# The carry gets added in next step(scanning from right to left).

#* 0 zaman 0. adım geliyor, o da string ifadeye 0 eklemek ama başına eklemek, ki bu noktada da nasıl başına ekleyeceğimi bilmiyorum.
#* gemini yardımıyla basamakları eşitledik :D zfill FTW

#artık a_str ve b_str olarak iki stringimiz var eşit uzunlukta, -1. indexinden başlayarak toplamam lazım.
carry = 0
number_str = ""

for i in range(-1, -len(a)-1, -1):
    basamak_degeri = int(a_str[i]) + int(b_str[i]) + carry # bu değerin toplamı 2den büyükse:
    #int(a[i]) + int(b[i]) ikisini toplayınca değer 2 olursa bunu diğer adıma taşı
    if basamak_degeri >= 2:
        carry = 1
    else:
        carry = 0 #carry'e 0 atadık ki sonraki adımda patlamayalım

    number_str += str(basamak_degeri%2)  #burda tersten yazdırıyor
    print(number_str)
match carry:
    case 1:
        number_str += str(carry)
    case 2:
        number_str = "10" + number_str 

result = reversed(number_str)
print(result)
#endregion

#region gemini çözümü
# 1. Adım: String uzunluklarını eşitleme (zfill ile)
max_len = max(len(a), len(b))
a_str = a.zfill(max_len)
b_str = b.zfill(max_len)

# 2. Adım: Sağdan Sola Toplama
carry = 0
result = []  # Basamakları doğru sırayla biriktirmek için liste kullanmak daha kolaydır

# range(max_len - 1, -1, -1) ile indexleri sağdan sola gezebiliriz (örneğin 3, 2, 1, 0)
for i in range(max_len - 1, -1, -1):
    # Basamak değerlerini integer'a çevir
    digit_a = int(a_str[i])
    digit_b = int(b_str[i])

    # Toplamı hesapla (iki basamak + elde)
    total = digit_a + digit_b + carry

    # Yeni basamak değeri (Toplamın 2'ye göre kalanı)
    current_digit = total % 2
    
    # Yeni elde (Toplamın 2'ye bölümü)
    carry = total // 2

    # Yeni basamağı sonucun BAŞINA ekle.
    # Alternatif olarak sona ekleyip sonra ters çevirebiliriz. (Burada sona ekleyelim, sonra ters çevirelim)
    result.append(str(current_digit))

# 3. Adım: Son Eldeyi Ekleme
if carry == 1:
    result.append("1")

# 4. Adım: Sonucu ters çevirip string'e dönüştürme (çünkü basamakları tersten ekledik)
final_sum = "".join(result[::-1]) 
# Alternatif: final_sum = "".join(reversed(result))

print(f"Input A: {a}, Input B: {b}")
print(f"Output: {final_sum}")
#endregion


#deneme1 - 10'luk sisteme çevirip hesap yaptırıp tekrar 2liğe döndürmek istedim tıkandım.
# #burda 10luk sisteme çevirerek çözmeye çalıştım ama tıkandım.
# toplam = 0
# for index, ch in enumerate(a):
#     toplam = toplam + (2**index) * int(ch)
# for index, ch in enumerate(b):
#     toplam = toplam + (2**index) * int(ch)
# print(toplam) #10'luk sistemdeki karşılığını veriyor mis gibi
