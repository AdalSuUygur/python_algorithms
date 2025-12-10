#13. Roman to Integer

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two ones added together. 
# 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. 
# However, the numeral for four is not IIII. 
# Instead, the number four is written as IV. 
# Because the one is before the five we subtract it making four. 
# The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#burda nasıl düşünüyorum?
#en önce en büyük sayı var yani M = 1000
#sonra C var, C = 100
#C'den sonra, C'den daha büyük olan bir değer var M = 1000; bu durumda C'yi çıkartıcaz, 1000-100
#CM olunca 900 oldu çünkü C M'den daha küçük ve önüne yazılmış çıkartma anlamı taşıyor.
#1000 + (-100+1000) = 1900 oldu
#X var, X = 10, sonra C var, x < c olduğu için; -10+100 yani 90
# 1900 + (-10 +100) = 1990
#I var yani 1, sonra V var yani 5 i < v olduğu için çıkartıyoruz -1 + 5 = 4
# 1990 + (-1+5) = 1994


#en küçükten başlayarak var olan karakterleri listeye ekleyelim, index değeri büyük olan büyük değeri karşılasın
#veya, zip ile 2 liste birleştirebiliriz, harf ve karşılığı listeleri, deneyelim.

# s = ["I", "V", "X", "L", "C", "D", "M"] #input sadece bunlar olabilir.
number_equalities = [1, 5, 10, 50, 100, 500, 1000]
character_equalities = ["I", "V", "X", "L", "C", "D", "M"]
print(list( #burası test
    zip(character_equalities, number_equalities #burda 0.eleman character'i 1. eleman sayısal değerini ifade ediyor.
        )))

# s = "III"
# for char in s: #gelen input içerisindeki her elemanı geziyorum
#     char = #character_equalities listesinde var mı diye bakmak lazım.

#burda tıkandım, geminiden yardım istedim ve ziplenmiş değerleri sözlüğe çevirmem gerektiğini söyledi. sözlük konusunu henüz bilmediğim için pass.
