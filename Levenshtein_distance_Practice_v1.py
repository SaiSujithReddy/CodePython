
def find_edit_distance(string1,string2):
    n = len(string1)
    m = len(string2)
    matrix = []
    for x in range(0,n+1):
        matrix.append([0 for x in range(0,m+1)])
    # Have to initilize the first row and first column 
    # TODO 
    # missing
    
    
    print(matrix)

    for i in range(n):
        for j in range(m):

            if string1[i] == string2[j]:
                matrix[i+1][j+1] = matrix[i][j]

            else:
                matrix[i+1][j+1] = \
                    min(matrix[i][j],
                        matrix[i][j+1],
                        matrix[i+1][j]) +\
                    1
    return matrix[n][m]


Str1 = "Hello"
Str2 = "Hellodude"
print(find_edit_distance(Str1,Str2))
