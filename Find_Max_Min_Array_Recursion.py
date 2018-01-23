
def find_min_array_recursion(input_array,n):
    if len(input_array) ==1:
        return input_array[0]
    else:
        return min(input_array[0],find_min_array_recursion(input_array[1:],n-1))



def find_max_array_recursion(input_array,n):
    if len(input_array) ==1:
        return input_array[0]
    else:
        return max(input_array[0],find_max_array_recursion(input_array[1:],n-1))



array1 = [3,6,1,0,-19,100,8,1,1,2,5]
n = len(array1)
print(find_min_array_recursion(array1,n))
print(find_max_array_recursion(array1,n))