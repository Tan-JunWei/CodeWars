# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(lst):
    number_list = []
    zero_counter = 0
    for num in lst:
        if num != 0:
            number_list.append(num)
        else:
            zero_counter += 1

    for i in range(zero_counter): #by counting number of zeroes, we know how many to append to the end of the list
        number_list.append(0)

    return number_list
move_zeros([1, 0, 1, 2, 0, 1, 3])