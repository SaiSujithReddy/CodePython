i = 2
j = 5

matrix = [[0] * i for x in range(j)]
print(matrix)

# Another way of initializing the matrix with None or zero
matrix_v2 =[]
matrix_v1 = [0] * i
for x in range(j):
    matrix_v2.append(matrix_v1)
print(matrix_v2)


print("---------------------------------------")

array = [1,2,3,4]

for i, j in enumerate(array,7):
    print(i)
    print(j)

print("---------------------------------------")