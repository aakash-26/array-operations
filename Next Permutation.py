
"""
Next Permutation
"""

print("\n ---------- Next Permutation ----------")

from itertools import permutations

a1 = [1, 2, 3]
p = permutations(a1)
a = [str(z) for z in a1]
ip = int("".join(a))
p_list = []
res = None
for i in p:
    i = [str(x) for x in i]
    k = int("".join(i))
    if k > ip:
        if res:
            if k < res:
                res = k
        else:
            res = k
if res:
    op = list(map(int, str(res)))

else:
    op = sorted(a1)
print("\n output : ", op)

