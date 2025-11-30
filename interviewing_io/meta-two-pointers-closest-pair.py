

#Find and return a pair of integers in a sorted list (all integers are positive) that
#when summed up, bring you the closest to the value of k
#Example Input: [5, 8, 14, 17, 25]
#Expected Output: (8, 25) since 8 + 25 = 33 which is closest to 35 (sum could be equals to, smaller or larger than k)

list_example = [5, 8, 14, 17, 25]
k = 35
#her ikisini inputa çevir
pairs = [] #çifti tanımladım

for item in list_example: #listedeki her elemanı gezdim
    for i in range(0, len(list_example)): # sayacı da listedeki eleman sayısına kadar gezdim
        if item != list_example[i]: #eğer seçtiğim item 0. indezteki item değilse
            Toplam = item + list_example[i] #toplamını buldum
            uzaklik = abs(k-Toplam) #uzaklık hesapladım
            pairs.append([uzaklik, item, list_example[i]]) #pairs listeme ekledim ve bunu her bir eleman için tekrarladım

print(len(pairs)) #test
print(pairs) #test

uzaklik = 999999999 #çok büyük bir değer

for pair in pairs:
    if pair[0] < uzaklik:
        uzaklik = pair[0]
        duo = [pair[1], pair[2]]

print(duo) #test
print(uzaklik) #test
print(f"Output: {duo} since sum of pair equals to {duo[0] + duo[1]} which is closest to {k}") #dry prensibine uyamadım