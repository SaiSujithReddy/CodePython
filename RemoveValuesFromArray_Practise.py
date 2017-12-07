#Doesn't work because remove will remove index but not value
'''
1. Given an array and a value, remove all instances of that value in place and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
The order of elements can be changed.
It doesn't matter what you leave beyond the new length.
Example: Given input array nums = [3,2,2,3], val = 3 Your function should return length = 2,
with the first two elements of nums being 2
'''




def remove_number_from_array(array_int,value):
    fake_index = 0
    duplicates = 0
    initial_len = len(array_int) - 1
    for x in range(0,initial_len):
        if array_int[x] == value:
            array_int.remove(array_int[x])
            duplicates += 1
    return [duplicates,array_int[:len(array_int)-duplicates]]




array_int = [1,4,5,6,2,3,8,9,3]
value = 3

print(remove_number_from_array(array_int,value))