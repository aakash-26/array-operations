
"""
find all pairs on integer array whose sum is equal to given number
"""
print("\n find all pairs on integer array whose sum is equal to given number")

a = [1, 5, 7, -1, 5]
from itertools import combinations

cmb = combinations(a,2)
a = [1, 5, 7, -1, 5]
from itertools import combinations
sm = 6
cmb = combinations(a,2)
# print(list(cmb))
cnt = 0
for i in list(cmb):
    if i[0] + i[1] == sm:
        cnt += 1
print("\n sum output : ",cnt)

