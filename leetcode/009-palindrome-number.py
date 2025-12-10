# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

#region with Big-o-notation knowledge:
#* 10 ms, 17.90 MB
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         #1. adım: x'i stringe çevirelim ki her bir adımda elemanlarını dolaşalım
#         x_str = str(x)
#         #2. adım: Slicing ile string olan ifadeyi ters çevirelim ki kontrol edebilelim:
#         x_str_reversed = x_str[::-1]
#         if x_str == x_str_reversed:
#             return True
#         return False
#endregion

#region leetcode fonksiyon
#* 23 ms, 17.95 MB
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         is_palindrome = False
#         str_x = str(x) #stringe çevirdik ki teker teker dolaşabilelim basamaklarını
#         lst_x = list(char for char in str_x) #hooop hemen list comprehension ile liste oluşturduk ki ters çevirebilelim

#         ters = ""
#         for i in range(len(lst_x)-1,-1,-1):
#             ters += lst_x[i]

#         if str_x == ters:
#             is_palindrome = True
        
#         return is_palindrome
#endregion

#region first try
# is_palindrome = False
# x = 101010101
# str_x = str(x) #stringe çevirdik ki teker teker dolaşabilelim basamaklarını
# lst_x = list(char for char in str_x) #hooop hemen list comprehension ile liste oluşturduk ki ters çevirebilelim
# ters = ""
# for i in range(len(lst_x)-1,-1,-1):
#     ters += lst_x[i]
# if str_x == ters:
#     is_palindrome = True
# print(is_palindrome) #test
#endregion
