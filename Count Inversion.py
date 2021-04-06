
"""
Count Inversion
"""
print("\n ---------- Count Inversion ----------")
a = [8, 4, 2, 1]
# a = [3, 1, 2]
p = []

for i in range(len(a)):
    for j in a[i + 1:]:
        p.append([a[i], j])

cnt = 0

for i in p:
    if i[0] > i[1]:
        cnt += 1
print("\n output : ", cnt)

