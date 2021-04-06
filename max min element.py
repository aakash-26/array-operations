
"""
Find the maximum and minimum element in an array (without sorting)
"""
print("\n ---------- Find the maximum and minimum element in an array (without sorting) ---------")
a = [1,32,6,4,78,9,21,5]

mn = a[0]
mx = a[0]

for i in a:

    if i > mx:
        mx = i
    elif i < mn:
        mn = i
    else:
        pass

print("\n minimum element : ", mn)
print("\n maximum element : ", mx)

