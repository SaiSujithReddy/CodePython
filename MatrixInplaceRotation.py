# def say_hello():
#     print('Hello, World')

# for i in range(5):
#     say_hello()


'''
    Give N*N matrix
    rotate in-place image by 90 (clockwise)

    [[1,2,3]
     [4,5,6]
     [7,8,9]
     ]

     rotateImage

     [[7,4,1]
      [8,5,2
      [9,5,3]
     ]
'''


def anticlockWiseRotation(matrix):
    row = len(matrix)
    # print(row)

    for x in range(0, int(row / 2)):

        for y in range(x, row - x - 1):
            temp = matrix[x][y]

            # to top
            matrix[x][y] = matrix[y][row - x - 1]

            matrix[y][row - x - 1] = matrix[row - x - 1][row - y - 1]
            # print("Past line 46")
            # to bottom
            matrix[row - x - 1][row - y - 1] = matrix[row - y - 1][x]

            matrix[row - y - 1][x] = temp




def printMatrix(matrix):
    row = len(matrix)
    for i in range(row):
        for j in range(row):
            print(matrix[i][j], end="")
        print("")


test_matrix = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]
               ]

# 1 2 3
# 4 5 6
# 7 8 9



# 3 2 3
# 4 5 6
# 7 8 9


# 3 2 9
# 4 5 6
# 7 8 9

# 3 2 9
# 4 5 6
# 7 8 7

# 3 2 9
# 4 5 6
# 1 8 7


# 3 6 9
# 4 5 6
# 1 8 7


printMatrix(test_matrix)
print("")
anticlockWiseRotation(test_matrix)
print("")
#clockWiseRotation(test_matrix)
printMatrix(test_matrix)
