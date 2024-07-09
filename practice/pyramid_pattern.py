row = int(input("Enter the number of rows: "))

for i in range(row):
    for k in range(row-i-1):
        print(" ", end ="")
    for z in range(2*i+1):
        print("*",end="")
    print()
