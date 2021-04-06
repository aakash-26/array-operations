
"""
Find the "Kth" max and min element of an array 
"""

print("\n ---------- Find the Kth max and min element of an array ---------")

k = 1

# Method 1 : using sorting

a.sort()

print("\n accending", a)

if k < len(a) - 1:
    print("\n kth smallest element : ", a[k - 1])
    print("\n kth largest element : ", a[::-1][k - 1])

else:
    print("\n Invalid index")

