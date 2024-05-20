# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers 
#in the form of a phone number.

def create_phone_number(n):
    first3 = []
    for i in range(0,3):
        first3.append(n[i])
    first_3 = ''.join(map(str,first3))

    next3 = []
    for i in range(3,6):
        next3.append(n[i])
    next_3 = ''.join(map(str,next3))
    
    remaining = []
    for i in range(6,len(n)):
        remaining.append(n[i])
    remaining_numbers = ''.join(map(str,remaining))
    print(f"({first_3}) {next_3}-{remaining_numbers}")
    return f"({first_3}) {next_3}-{remaining_numbers}"

create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0])


'''
cleaner method without use of lists 

def create_phone_number(n):
  str1 =  ''.join(str(x) for x in n[0:3])
  str2 =  ''.join(str(x) for x in n[3:6])
  str3 =  ''.join(str(x) for x in n[6:10])


  return '({}) {}-{}'.format(str1, str2, str3)

'''