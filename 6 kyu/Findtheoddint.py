# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

def find_it(seq):
    unique_char = set(seq)
    new_list = []

    for num in unique_char:
        count = seq.count(num)
        new_list.append(count)

    for i in new_list:
        if i %2 != 0:
            index = new_list.index(i)
    return list(unique_char)[index]
find_it([20,1,1,2,2,3,3,5,5,4,20,4,5])
find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])

'''
def find_it(seq):
    for elem in set(seq):
        if seq.count(elem) % 2:
            return elem
'''
# This can be reduced to if seq.count(elem) % 2.
# Because of bool(0) --> False and bool(1) --> True