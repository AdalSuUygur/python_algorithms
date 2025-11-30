
# Given the root of a binary tree, imagine yourself standing on the right side of it and your best friend standing on the left side, both observing the tree from their respective sides.
# Return the values of the nodes you can both see, first from the left side (bottom to top), followed by those from the right side (top to bottom)
# Example:
# Left View (bottom-up): [5, 2, 1]
# Right View (top-down): [1, 3, 4]
# OutPut: [5, 2, 1, 3, 4]
# Example 2:
# Left View: [5, 4, 2, 1]
# Right View: [1, 3]
# Output: [5, 4, 2, 1, 3]

top_part = type(int) #bu tepedeki eleman olsun.
left_view = [] #soldaki taraf
right_view = [] #sağdaki taraf
binary_tree = []

all_parts = [ #bize input olarak gelmesi gereken değer.
    [1],        # Katman 1 (En Üst)
    [2, 3],     # Katman 2
    [4, 6],     # Katman 3
    [5, 9, 7]   # Katman 4 (En Alt)
]

for part in all_parts:
    left_view.append(part[0])
    right_view.append(part[-1])
left_view.reverse() #ters çevirdik bottom to top olduğu için.
print(left_view) #test
print(right_view) #test

if left_view[-1] == right_view[0]:
    top_part = left_view[-1]
print(top_part) #test

binary_tree = left_view + right_view
binary_tree.remove(top_part)

print(binary_tree)