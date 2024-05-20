# Complete the greatestProduct method so that it'll find the greatest product of five consecutive digits 
#in the given string of digits.

# For example: the greatest product of five consecutive digits in the string "123834539327238239583" is 3240.

# The input string always has more than five digits.

# Adapted from Project Euler.

def greatest_product(str):
    list_of_digits = list(int(digit) for digit in str)
    # print(list_of_digits)
    highest = 0
    for i in range(0, len(list_of_digits)-4):
        five_consecutive = list_of_digits[i:i+5]
        product_of_five_consecutive = 1
        for number in five_consecutive:
            product_of_five_consecutive *= number 
        # print(five_consecutive)
        # print(product_of_five_consecutive)
        if product_of_five_consecutive > highest:
            highest = product_of_five_consecutive
        i +=1
    # print(highest)
    return highest

greatest_product("10080")
greatest_product("09587793089127527480320985")