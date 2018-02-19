
def calc_distance(str1,str2):
    m = len(str1)
    n = len(str2)

    #create an array with zeroes of size m+1*n+1
    output = []
    for i in range(m+1):
        output.append([0 for j in range(n+1)])

    print(output)


    for i in range(m):
        for j in range(n):
            if str1[i] == str2[j]:
                output[i+1][j+1] = output[i][j]
            else:
                output[i+1][j+1] = 1+ min(output[i][j+1],output[i+1][j],output[i][j])

    print(output)

str1 = "Hello"
str2 = "Hellodude"


calc_distance(str1,str2)