
"""
Move all the negative elements to one side of the array 
"""
print("\n ---------- Move all the negative elements to one side of the array ---------")
a = [1, -20, 21, -3, -4, 56, 43, -92]

for i in a:
    if i < 0:
        ind = a.index(i)
        del a[ind]
        a.insert(0, i)

    else:
        pass

print("\n Negative at one side : ", a)
