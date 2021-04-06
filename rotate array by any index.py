
"""
Write a program to cyclically rotate an array by any index (Both shift).
"""
print("\n ---------- Write a program to cyclically rotate an array by any index (Both shift). ---------")

rotating_index = 1

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = []
res1 = []
l = len(a)

for i in range(l):
    check = 0
    new_index = None

    new_index = i + rotating_index
    check = new_index - l

    if check >= 0:
        new_index = check - l

    res.append(a[new_index])

    new_index = l - rotating_index + i

    if new_index >= 0:
        new_index = new_index - l

    res1.append(a[new_index])

print("\n rearranged array (Left shift) : ", res)
print("\n rearranged array (Right shift): ", res1)

