"""
Reverse array
"""
print("\n ---------- Reverse array ---------")
a = [4, 1, 5, 7, 2, 8, 3, 9, 6]

# Method 1 : by shortcut
print("\n Reverse array", a[::-1])

# Method 2 :  by traversing
itr = len(a) - 1
for i in range(len(a)):
    print(a[itr], end=" ")
    itr -= 1

