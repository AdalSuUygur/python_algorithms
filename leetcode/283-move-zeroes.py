#283. Move Zeroes

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

nums = [0,1,0,3,12]
#önce düzden başladım saydırmaya ama indexler kayıyodu poplayınca
#bu yüzden sondan başladım gezmeye ki çıkardığım elemanın sonrasındaki indexler kaymasın
for i in range(len(nums)-1, -1, -1):
    if nums[i] == 0:
        nums.pop(i)
        nums.append(0)

#region leetcode çözümü
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for i in range(len(nums)-1, -1, -1):
#             if nums[i] == 0:
#                 nums.pop(i)
#                 nums.append(0)
#endregion

#region big-o-notation çözümü
non_zero_pointer = 0 # Sıfır olmayan bir sonraki elemanın yazılacağı index

# 1. Geçiş: Sıfır olmayanları öne taşı
for i in range(len(nums)): # i, diziyi baştan sona okur (O(N) zaman)
    if nums[i] != 0:
        # Sıfır olmayan elemanı, yazma pozisyonuna taşı
        nums[non_zero_pointer] = nums[i]
        non_zero_pointer += 1
# 2. Geçiş: Kalanı sıfırla doldur
# non_zero_pointer'dan başlayarak listenin sonuna kadar 0 yaz (O(N) zaman)
for i in range(non_zero_pointer, len(nums)):
    nums[i] = 0

# Toplam: O(N) + O(N) = O(N)
#endregion