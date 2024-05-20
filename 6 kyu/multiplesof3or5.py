# if we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

# Additionally, if the number is negative, return 0.

# Note: If the number is a multiple of both 3 and 5, only count it once.

def solution(number):
    multiples_of_three_or_five = []
    if number < 0:
        return 0
    for integer in range(1, number):
        if (integer % 3 == 0) or (integer % 5 == 0):
            multiples_of_three_or_five.append(integer)
    total = sum(multiples_of_three_or_five)
    
    print(total)
    return total


solution(10)

'''
#without the need for list and list append. Just straight up increase the sum from 0

def solution(number):
    sum = 0
    for i in range(number):
        if (i % 3) == 0 or (i % 5) == 0:
            sum += i
    return sum
'''