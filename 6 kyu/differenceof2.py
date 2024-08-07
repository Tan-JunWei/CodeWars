# The objective is to return all pairs of integers from a given array of integers that have a difference of 2.

# The result array should be sorted in ascending order of values.

# Assume there are no duplicate integers in the array. The order of the integers in the input array should not matter.

# Examples
# [1, 2, 3, 4]  should return [(1, 3), (2, 4)]

# [4, 1, 2, 3]  should also return [(1, 3), (2, 4)]

# [1, 23, 3, 4, 7] should return [(1, 3)]

# [4, 3, 1, 5, 6] should return [(1, 3), (3, 5), (4, 6)]

def twos_difference(lst):
    lists_diff_2 = []
    for i in range(len(lst)):
        if lst[i] - 2 in lst:
            diff_2 = (lst[i]-2,lst[i])
            lists_diff_2.append(diff_2)
        diff_2 = []
    print(sorted(lists_diff_2))
    return sorted(lists_diff_2)

twos_difference([3, 1, 6, 4])# [(1, 3), (4, 6)]
twos_difference([1, 3, 5, 6, 8, 10, 15, 32, 12, 14, 56]) # [(1, 3), (3, 5), (6, 8), (8, 10), (10, 12), (12, 14)])

'''
def twos_difference(lst): 
    return [(i, i + 2) for i in sorted(lst) if i + 2 in lst]
'''
