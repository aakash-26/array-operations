
"""
Merge Intervals
"""

print("\n ---------- Merge Intervals ----------")

a = [[6, 8], [1, 9], [2, 4], [4, 7]]

c = 1
while c == 1:
    if len(a) > 1:
        i = a[0]
        j = a[1]

        if i[0] < j[1]:
            k = [min(i[0], j[0]), max(i[1], j[1])]
            del a[1]
            del a[0]
            a.insert(0, k)
    else:
        c = 0

print("\n Merge Intervals : ", *a)

