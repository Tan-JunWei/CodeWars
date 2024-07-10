value = 65
row = 5

for i in range(row):
    for k in range(i+1):
        print(chr(value),end = " ")
        value += 1
    print()
    