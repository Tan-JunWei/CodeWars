# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in
# a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that 
# fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# Examples (input --> output):
# 255, 255, 255 --> "FFFFFF"
# 255, 255, 300 --> "FFFFFF"
# 0, 0, 0       --> "000000"
# 148, 0, 211   --> "9400D3"

def rgb(r, g, b):
    values = [r,g,b]
    for i in range(0, len(values)):
        if values[i] < 0:
            values[i] = 0
        if values[i] > 255:
            values[i] = 255
    # print(values)
    print(f"{values[0]:02X}{values[1]:02X}{values[2]:02X}")
    return f"{values[0]:02X}{values[1]:02X}{values[2]:02X}"

rgb(-28 ,224 ,386)

'''
def limit(num):
    if num < 0:
        return 0
    if num > 255:
        return 255
    return num


def rgb(r, g, b):
    return "{:02X}{:02X}{:02X}".format(limit(r), limit(g), limit(b))
'''