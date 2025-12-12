# 67. Add Binary

# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

a = "1010"
b = "1011"
#deneme2
#ters çevir #basamaklar için, indexlerini eşitlicez aslında, 0. index 0. basamak olcak ve 0 + 0 0. basamak olarak kalcak
# reversed(a)
# reversed(b)

# if len(reversed(a)) != len(reversed(b)):
#     pass #kısa olanı bul, bu bir edge case şimdilik siktir et

#print(list(zip(reversed(a),reversed(b)))) #ters çevirdik, indexleri eşitledik aslında

result_int = (int(x) + int(y) for x,y in zip(reversed(a),reversed(b))) #ters çevirdik, sonucu topladık.
#print(result_int)
#listedeki her itemı string olarak yazdırmak istiyorum: 
result_str = "".join(str(item) for item in result_int)
print(result_str)

#eğer 1+1 ise sonucu 0 yazdırıp bir sonraki indexe +1 değer gönderticez gibi bir şey deneyebiliriz?

#hemen list built in func incelemesi xd
#0. indexlerini topla (inte çevirip topla)
#tekrar ters çevir ve stringe çevir

new_ls = result_str.replace("2","01")
print(new_ls)
result = "".join(reversed(new_ls))
print(result)

#yorumlarda birisi böyle demiş, acaba 10luk sisteme geçirmeden çözebilir miyim? ama en sağdan başlamam lazım, listenin sonundan ya da?
# 1+1=0 with carry 1
# 1+0=1 with carry 0
# 0+1=1 with carry 0
# 0+0=0 with carry 0
# Imp:1+1=1 with carry 1 if previous carry was 1.
# The carry gets added in next step(scanning from right to left).

# Know the algorithm first,then write your own code~Problem solving



#deneme1
# #burda 10luk sisteme çevirerek çözmeye çalıştım ama tıkandım.
# toplam = 0
# for index, ch in enumerate(a):
#     toplam = toplam + (2**index) * int(ch)
# for index, ch in enumerate(b):
#     toplam = toplam + (2**index) * int(ch)
# print(toplam) #10'luk sistemdeki karşılığını veriyor mis gibi

# #buralarda bir şeyleri yanlış yapıyorum



