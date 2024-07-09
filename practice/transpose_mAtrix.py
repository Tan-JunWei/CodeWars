A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

row = len(A)
col = len(A[0])

transposed = [[0 for i in range(row)] for k in range(col)]

for i in range(row):
        for j in range(col):
            transposed[j][i] = A[i][j]

print(transposed)