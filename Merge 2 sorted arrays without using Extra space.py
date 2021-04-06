
"""
Merge 2 sorted arrays without using Extra space.
"""

print("\n ---------- Merge 2 sorted arrays without using Extra space. ----------")

a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]

l1 = len(a)
l2 = len(b)

c = a + b
c.sort()

a = c[:l1]
b = c[l1:]

print("\n output arrays : ", a, " ", b)

