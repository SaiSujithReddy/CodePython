#Doesn't work because remove will remove index but not value
'''
1. Given an array and a value, remove all instances of that value in place and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
The order of elements can be changed.
It doesn't matter what you leave beyond the new length.
Example: Given input array nums = [3,2,2,3], val = 3 Your function should return length = 2,
with the first two elements of nums being 2
'''

def remove_given_value_from_array(array,value):
    j =0;
    print(array)
    for x in array:
        print(x,value)
        print("value of x is ", x)
        if(x == value):
            array.remove(x)
        else:
            j += 1
    return [array,j]


input_array = [1,2,3,4,4,4,4,4,5,6,7,8]

print(remove_given_value_from_array(input_array,4))