
"""
find Largest sum contiguous Subarray [V. IMP]
"""

print("\n ---------- find Largest sum contiguous Subarray [V. IMP] ---------")

a = [-2, -3, 4, -1, -2, 1, 5, -3]

max_sum = 0
m = 0
for i in a:

    m += i
    if max_sum < m:
        max_sum = m

    if m < 0:
        m = 0

print("\n max sum : ", max_sum)

