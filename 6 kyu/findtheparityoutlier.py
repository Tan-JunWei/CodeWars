# You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
# Write a method that takes the array as an argument and returns this "outlier" N.

# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

# [160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)

def equal_or_odd(list):
    even = []
    odd = []
    for char in list:
        if char % 2 == 0:
            even.append(char)
        else:
            odd.append(char)
    return True if len(even) > len(odd) else False
        

def find_outlier(integers):
    boolean = equal_or_odd(integers)
    if boolean: #even
        for num in integers:
            if num %2 !=0:
                return num
    else:
        for num in integers:
            if num %2 ==0:
                return num


find_outlier([160, 3, 1719, 19, 11, 13, -21])