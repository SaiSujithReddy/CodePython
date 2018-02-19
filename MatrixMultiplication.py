
from MatrixTranspose import matrixTranspose


class matrixMultiplication:
    def matrix_multiplication(matrixA,matrixB):

        for x in range(len(matrixA)):
            for y in range(len(matrixA[0])):
                matrixA[x][y] = matrixA[x][y]*matrixB[x][y]
        print(matrixA)
        return matrixA


A = [[1,2]]
B = [[3],[4]]
transposed_matrix = matrixTranspose.transpose(A)
print(transposed_matrix)
print("matrix B is ", B)
matrixMultiplication.matrix_multiplication(transposed_matrix,B)
