
"""
find duplicate in an array of N+1 Integers
"""
print("\n --------- find duplicate in an array of N+1 Integers --------")
a = [1, 3, 4, 2, 2]
res = []
for i in a:
    if a.count(i) > 1:
        if i not in res:
            res.append(i)
print("\n Duplicate elements : ", *res)

