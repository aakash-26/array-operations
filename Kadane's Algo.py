
"""
Kadane's Algo [V.V.V.V.V IMP]

The simple idea of Kadane’s algorithm is to look for all positive contiguous segments of the array
(max_ending_here is used for this). And keep track of maximum sum contiguous segment among all positive 
segments (max_so_far is used for this). Each time we get a positive-sum compare it with max_so_far and 
update max_so_far if it is greater than max_so_far.
"""
a = [-2, -3, 4, -1, -2, 1, 5, -3]

max_pos_sum = 0

tem_sum = 0

for i in a:
    tem_sum += i

    if tem_sum > max_pos_sum:
        max_pos_sum = tem_sum

    if tem_sum < 0:
        tem_sum = 0

print("\n Kadane's Algo output : ", max_pos_sum)

