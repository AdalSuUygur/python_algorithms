# 217. Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation: The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation: All elements are distinct.

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Constraints:
# 1 <= nums.length <= 10**5
# -10**9 <= nums[i] <= 10**5

#region Time Limit Exceeded
nums = [1,2,3,1]
is_occur = False #başlangıçca tekrarlanıyor mu değişkenini false olarak tanımladık.
if 1 <= len(nums) <= 10**5:
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if (nums[i] == nums[j]) and (i != j):
                is_occur = True
print(is_occur) #test
#* Çalışıyor ancak leetcode kabul etmiyor çünkü zaman sınırlamasına uymuyor.
#endregion

#region set() function ile leetcode çözümü:

#? set() fonksiyonu
#* matematikteki küme (set) kavramının birebir karşılığı ve temel olarak iki ana amaç için kullanılır:
#* 1: Unique Elements: Bir set içine aynı elemandan birden fazla eklenilemez.
#* 2: Çok Hızlı Arama ve Üyelik Kontrolü: Bunu anlamadım xd

# nums = [1,2,3,4]
# seen = set() #boş küme tanımladık

# for num in nums: #her elemanı geziyoruz
#     if num in seen: #eğer görüldüyse daha önce
#         return True #direkt döngüden çıktık ve true döndürdük
#     else: #yok anam daha görmediysek
#         seen.add(num) #ekledik kümeye
# return False #bu da döngüdeki tüm elemanlar bittikten sonra
#endregion