A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[2,0,0],
     [0,2,0],
     [0,0,2]]

result = []

def matrixmult(A,B):
    for i in range(len(A)):
        numlist = []

        for k in range(len(B[0])):
            sum = 0

            for j in range(len(B)):
                sum += A[i][k] * B[k][j]

            numlist.append(sum)

        result.append(numlist)
        
    print(result)

matrixmult(A,B)

# expected:
# [[2, 4, 6], [8, 10, 12], [14, 16, 18]]