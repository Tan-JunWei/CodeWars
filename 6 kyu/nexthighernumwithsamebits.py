# Your task is to find the next higher number (int) with same '1'- Bits.

# I.e. as much 1 bits as before and output next higher than input. Input is always an int in between 1 and 1<<30 (inclusive). 
# No bad cases or special tricks...

# Some easy examples:
# Input: 129  => Output: 130 (10000001 => 10000010)
# Input: 127 => Output: 191 (01111111 => 10111111)
# Input: 1 => Output: 2 (01 => 10)
# Input: 323423 => Output: 323439 (1001110111101011111 => 1001110111101101111)

def next_higher(n):
    binary_string = f"0{n:b}" #convert into binary. append 0 at start for rfind to work
    index = binary_string.rfind("01")
    binary_string = binary_string[:index] + "10" + "".join(sorted(binary_string[index+2:]))
    new_binary = int(binary_string,2)
    print(new_binary)
    return new_binary

next_higher(128) 
next_higher(127) 
next_higher(1253343)