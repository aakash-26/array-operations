
"""
Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
"""

print(
    "\n ---------- Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo ---------")

a = [0, 1, 2]

x = None
y = None

for i in range(len(a)):
    for j in range(len(a)):
        if j < len(a) - 1:

            x = a[j]
            y = a[j + 1]

            if x <= y:
                pass
            elif x > y:
                a[j] = y
                a[j + 1] = x

print("\n sorted list", a)

