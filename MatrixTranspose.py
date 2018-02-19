# learnt how to initialize a matrix in python


#Assumption all rows are have equal columns

class matrixTranspose:

    def transpose(input):
        print("Input is ",input)
        x = len(input[0])
        y = len(input)
        print("value of x is ",x)
        print("value of y is ",y)
        output = []
        for z in range(x):
            output.append([0 for i in range(y)])
        #print(output)
        for x in range(len(input)):
            for y in range(len(input[x])):
                #print(input[x][y])
                output[y][x] = input[x][y]

        print(output)
        return output


input = [[1,2,3],
         [4,5,6],
         [7,8,9],
         [10,11,12]]
matrixTranspose.transpose(input)