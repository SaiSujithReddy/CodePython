
matrixA = [[1,3],
           [2,4]]

matrixB = [[1,5],
           [2,6]]


def matrix_join(A,B):
    output = []

    for x in range(len(A)):
        output.append([0 for i in range(len(A)+len(B)-1)])

    print(output)
    for x in range(len(A)):
        for y in range(len(A[0])):
            output[x][y] = A[x][y]
    for x in range(len(B)):
        for y,z in zip(range(len(A),len(A)+len(B)-1),range(1,len(B))):
            output[x][y] = B[x][z]
    print(output)


matrix_join(matrixA,matrixB)