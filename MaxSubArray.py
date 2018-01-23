
import sys

def max_sub_array(array):
    max_sum = -sys.maxsize - 1
    temp_sum = 0

    for x in range(len(array)):
        print("entered for loop")
        if array[x] >= 0:
            temp_sum += array[x]
            if temp_sum > max_sum:
                max_sum = temp_sum
        else:
            temp_sum += array[x]
            if temp_sum <0:
                temp_sum = 0
        print(temp_sum,max_sum)
    print(max(max_sum,temp_sum))

# array = [1,2,3,-1,-5,-5,4]
# array = [1,2,3,-1,-5,-5,4,3]
# array = [1]
# array = [0]
# array = [-1]
# array = [-1,-1,3,0,-100,101]
# array = [1000,1,2,3,4,-2]
array = [-100,-99,-9800,1000,-2,2000,-90,-9000]
max_sub_array(array)