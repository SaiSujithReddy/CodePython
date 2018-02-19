import random
import os


def create_matrix(row_count,col_count):
    matrix = [[0 for x in range(row_count)] for y in range(col_count)]
    return matrix

def fill_bombs(matrix,probability):
    for i in range(col_count):
        for j in range(row_count):
            matrix[i][j] = (random.random() < probability)

    #print(matrix)
    return matrix

def write_bombs(matrix):
    for i in range(col_count):
        for j in range(row_count):
            if matrix[i][j]:
                os.write(1,bytes('* ','UTF-8'))
            else:
                os.write(1,bytes('. ','UTF-8'))
        os.write(1,bytes('\n','UTF-8'))
    return matrix

def print_matrix(matrix):
    temp_row_count = len(matrix)
    temp_col_count =  len(matrix[0])
    for x in range(temp_row_count):
        for y in range(temp_col_count):
            print(matrix[x][y], end='')
        print()

def write_number_of_bombs(matrix,row_count,col_count):
    solution = create_matrix(row_count+2,col_count+2)
    for r in range(1, col_count+1):
        for c in range(1, row_count + 1):
            # (rr, cc) indexes neighboring cells.
            for rr in range(r - 1, r + 2):
                for cc in range(c - 1, c + 2):
                    if matrix[rr][cc]:
                        solution[r][c] += 1
    print_matrix(solution)
    return solution

def write_solution(matrix,row_count,col_count,matrix_with_bombs):
    # Write solution.
    os.write(1, bytes('\n', 'UTF-8'))
    for r in range(1, col_count + 1):
        for c in range(1, row_count + 1):
            if matrix[r][c]:
                os.write(1, bytes('* ', 'UTF-8'))
            else:
                os.write(1, bytes(str(matrix_with_bombs[r][c]) + ' ', 'UTF-8'))
        os.write(1, bytes('\n', 'UTF-8'))
    return matrix


row_count = 8
col_count = 8
matrix = create_matrix(row_count+2,col_count+2)
print("After creating matrix")
print(matrix)
matrix = fill_bombs(matrix,0.5)
print("After Filling matrix")
print(matrix)
matrix = write_bombs(matrix)
matrix_with_bombs = matrix
print("After Writing matrix")
print(matrix)
solution = write_number_of_bombs(matrix,row_count,col_count)
print("After writing number of bombs")
print(matrix)
final_solution = write_solution(solution,row_count,col_count,matrix_with_bombs)
#print("After writing number of bombs")
#print_matrix(final_solution)