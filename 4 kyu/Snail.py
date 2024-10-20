# Snail Sort
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]


# NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell
# pattern.
# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

def snail(snail_map):
    snail_list = []
    while snail_map:
        snail_list.append(snail_map.pop(0))
        snail_map = list(map(list, zip(*snail_map)))[::-1]
    
    return [j for i in snail_list for j in i]

'''
hard!
'''

snail([[1,2,3],
       [4,5,6],
       [7,8,9]])

