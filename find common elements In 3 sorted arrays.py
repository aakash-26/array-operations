
"""
find common elements In 3 sorted arrays
"""
print("\n find common elements In 3 sorted arrays")

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

# Method 1 : using set

print(" Common elements : ", set(ar1).intersection(set(ar2), set(ar2)))

# Method 2 : By traversing

check = lambda x, l1, l2: x in l1 and x in l2

if __name__ == "__main__":
    print("\n Common elements : ")
    for i in ar1:
        c = check(i, ar2, ar3)
        if c:
            print("\t\t", i)

