
"""
Find the Union and Intersection of the two sorted arrays.
"""
print("\n ---------- Find the Union and Intersection of the two sorted arrays. ---------")

a = [1, 2, 3, 4, 5, 6]
b = [4, 5, 6, 7, 8, 9]

# Method 1 : by set method

a = set(a)
b = set(b)

print("\n union : ", list(a.union(b)))
print("\n intersection : ", list(a.intersection(b)))


# Method 2 :

a = [1, 2, 3, 4, 5, 6]
b = [4, 5, 6, 7, 8, 9]

u = []

intr = lambda x: x in b

uni = a + b

i = filter(intr, a)

print("\n union : ", list(set(uni)))
print("\n intersection : ", list(i))

