#242. Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

#region Kendi çözümüm, az maliyet için set() kullandım ama gemini beğenmedi, 17.58 mb kullandık
# s = "anagram"
# t = "nagaram"
# is_anagram = True
# harf = set()

# if len(s) != len(t):
#     is_anagram = False #fonksiyonda return false döndür

# for char in s:
#     if char not in harf:
#         if s.count(char) != t.count(char):
#             is_anagram = False
#     harf.add(char)

# print(is_anagram)
#endregion

#region bilgim dahilinde sorting metodu ile denemece 18.49 mb kullandık
s = "anagram"
t = "nagaram"
is_anagram = True

if len(s) != len(t):
    is_anagram = False #fonksiyonda return false döndür

s_sorted = sorted(s)
t_sorted = sorted(t)

if s_sorted != t_sorted:
    is_anagram = False

#endregion