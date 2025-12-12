# 67. Add Binary

# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

a = "11"
b = "1"

#burda 10luk sisteme çevirerek çözmeye çalıştım ama tıkandım.
toplam = 0
for index, ch in enumerate(a):
    toplam = toplam + (2**index) * int(ch)
for index, ch in enumerate(b):
    toplam = toplam + (2**index) * int(ch)
print(toplam)

# bolum = (bolunen / bolen) + kalan
# 4'ü 2ye böldük, kalan varsa onu 2^^0 olarak aldık
# if bölen >= 2 ise: tekrar böl
# aynı mantık devam
# ne zaman dur? bölen <2 ise durdurduk


