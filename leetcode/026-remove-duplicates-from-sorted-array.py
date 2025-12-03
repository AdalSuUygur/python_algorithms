# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same.
# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. 

# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# #inputu dışarıdan alacaksak çalışacak kod bloğu
# while True:
#     try:
#         number = int(input("Enter a number to add list, e to exit: "))
#         nums.append(number)
#     except (TypeError, ValueError):
#         print("Liste tanımı tamamlandı.")
#         break
# print(nums) #test

# #inputu dışarıdan alacaksak çalışacak kod bloğu try-exceptsiz.
# count = int(input("liste uzunluğu: "))
# for i in range(count):
#     number = int(input("sayı gir: "))
#     nums.append(number)
# print(nums) #test

nums = [15,15,16,16,16,17,17,18,18,19] #input olarak alacağımız liste
k = 1 #kaç tane unique sayı var bunu tutan değişken, 0. indexteki değer her türlü unique diye varsayarak 1den başlatıyoruz.

j = 0 #bir sonraki adımdaki değerden farklıysa, j. indexteki değeri farklı olan sayıyla değiştirmemizi sağlayan counter
for i in range(1, len(nums)):
    if nums[i] == nums[i-1]: #bir önceki indexteki değerle eşit mi
        continue
    else: #değilse
        k += 1 #unique counterı 1 artır
        j += 1 #index değişmesini 1 artır
        nums[j] = nums[i] #indexteki değeri değiştirdik
# print(k) #test
# print(nums) #test

for i in range(k, len(nums)):
    nums[i] = "_"
# print(nums) #test

print(f"{k}, nums = {nums}")


#leetcode çözümü
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         k = 1 #kaç tane unique sayı var bunu tutan değişken, 0. indexteki değer her türlü unique diye varsayarak 1den başlatıyoruz.

#         j = 0 #bir sonraki adımdaki değerden farklıysa, j. indexteki değeri farklı olan sayıyla değiştirmemizi sağlayan counter
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i-1]: #bir önceki indexteki değerle eşit mi
#                 continue
#             else: #değilse
#                 k += 1 #unique counterı 1 artır
#                 j += 1 #index değişmesini 1 artır
#                 nums[j] = nums[i] #indexteki değeri değiştirdik
#         # print(k) #test
#         # print(nums) #test

#         for i in range(k, len(nums)):
#             nums[i] = "_"
#         # print(nums) #test

#         return k