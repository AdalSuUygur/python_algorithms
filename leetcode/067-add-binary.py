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

#deneme2 - 2'lik sistemde toplamaları tersten yapmaya çalışıyorum

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
if len(a) < len(b):
    a = a.zfill(len(b))
elif len(b) < len(a):
    b = b.zfill(len(a))

#Burdaki adımda, index değeri -1'den başlamam gerek ve -2, -3 olarak ilerlemem gerek, neden? çünkü basamaklar en sağdan başlıyor ve sola doğru ilerliyor.

# result_int = (int(x) + int(y) if int(x) + int(y) < 2 else 10 for x,y in zip(a,b)) #yanlış çalışıyor ama bi kalsın
# print(list(result_int))

print(a[::-1]) # bu da ters çeviriyor ama yapamadım



#ters çevir #basamaklar için, indexlerini eşitlicez aslında, 0. index 0. basamak olcak ve 0 + 0 0. basamak olarak kalcak
# if len(reversed(a)) != len(reversed(b)):
#     pass #kısa olanı bul, bu bir edge case şimdilik siktir et

#print(list(zip(reversed(a),reversed(b)))) #ters çevirdik, indexleri eşitledik aslında

# result_int = (int(x) + int(y) for x,y in zip(reversed(a),reversed(b))) #ters çevirdik, sonucu topladık.
# #print(result_int)
# #listedeki her itemı string olarak yazdırmak istiyorum: 
# result_str = "".join(str(item) for item in result_int)
# print(result_str)

#eğer 1+1 ise sonucu 0 yazdırıp bir sonraki indexe +1 değer gönderticez gibi bir şey deneyebiliriz?

#hemen list built in func incelemesi xd
#0. indexlerini topla (inte çevirip topla)
#tekrar ters çevir ve stringe çevir

# new_ls = result_str.replace("2","01")
# print(new_ls)
# result = "".join(reversed(new_ls))
# print(result)





#deneme1 - 10'luk sisteme çevirip hesap yaptırıp tekrar 2liğe döndürmek istedim tıkandım.
# #burda 10luk sisteme çevirerek çözmeye çalıştım ama tıkandım.
# toplam = 0
# for index, ch in enumerate(a):
#     toplam = toplam + (2**index) * int(ch)
# for index, ch in enumerate(b):
#     toplam = toplam + (2**index) * int(ch)
# print(toplam) #10'luk sistemdeki karşılığını veriyor mis gibi
