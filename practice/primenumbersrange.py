import math

for i in range(2,100):
    prime = True
    num = i
    for number in range(2,int(math.sqrt(num))):
        if num % number == 0:
            prime = False
            break
        else:
            prime = True
    if prime:
        print(num, end= " ")