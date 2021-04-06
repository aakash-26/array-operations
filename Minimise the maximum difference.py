
"""
Minimise the maximum difference between heights [V.IMP]
"""
print("\n ---------- Minimise the maximum difference between heights [V.IMP] ---------")

a = [1, 10, 15]
k = 6  # minimize or max height by k

mn = min(a)
mx = max(a)

res = [abs((mn + k) - (mx + k)), abs((mn - k) - (mx - k)), abs((mn + k) - (mx - k)), abs((mn - k) - (mx + k))]

print("\n Minimize difference is : ", min(res))
