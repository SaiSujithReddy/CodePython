#http://isharemylearning.blogspot.com/2012/08/minimum-number-of-insertions-in-string.html
'''
This  problem can be two steps
step 1:- find longest common subsequence
step 2:- total string - common sub sequence = no of insertions
'''

#Things learnt
# creating a matrix and initializing with zeores
import math

def find_common_subsequence(str1,str2):
    i = len(str1)+1
    j = len(str2)+1

    matrix = [[0] * i for x in range(j)]
    print(matrix)

    # Another way of initializing the matrix with None or zero
    matrix_v2 = []
    matrix_v1 = [0] * i
    for x in range(j):
        matrix_v2.append(matrix_v1)
    print(matrix_v2)


    #matrix[0][0] = 0
    for x in range(i):
        for y in range(j):
            print("x values is {}, y value is {}",x,y)
            if x == 0 or y == 0:
                matrix[y][x] = 0
            elif str1[x-1] == str2[y-1]:
                matrix[x][y] = matrix[x-1][y-1] + 1
            else:
                matrix[x][y] = max(matrix[x][y-1],matrix[x-1][y])
    print(matrix)
    print("Value of i j are", i ,j)
    print(matrix[i-1][j-1])
    return matrix[i-1][j-1]

string = "hotoh"
print(string[::-1])
common = find_common_subsequence(string,string[::-1])

min_insertions = len(string) - common
print("min_insertions is ",min_insertions)




# hello
#heolloeh
#min insertions = 3

# hi
# hih
#min insertions = 1

# abcdd - 3
# abcd  - 3
# hotoh
