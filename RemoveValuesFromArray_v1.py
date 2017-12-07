#This works
'''
1. Given an array and a value, remove all instances of that value in place and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
The order of elements can be changed.
It doesn't matter what you leave beyond the new length.
Example: Given input array nums = [3,2,2,3], val = 3 Your function should return length = 2,
with the first two elements of nums being 2
'''

def remove_given_value_from_array(array,value):
    array = [x for x in array if x != value]
    return array


input_array1 = [1,2,3,4,4,4,4,4,5,6,7,8]
input_array = [1]
input_array = [1,2,3]
input_array = [4,4,44,4,4]
input_array = [4,4,4,4,4,4]

output_array = remove_given_value_from_array(input_array1,4)
print(output_array)
print(len(output_array))