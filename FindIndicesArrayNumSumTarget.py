# Find indices of all elements in an array that add up to a given target

#TC - O(n^2)
#SC - O(1)

def find_indices_of_array(array_num,target):
    dict_indices = {}
    for x in array_num:
        i =0
        dict_indices[x] = i
        i += 1

    for x in array_num:
        if target-x in dict_indices:
            return dict_indices.get(target - x)


array = [1,2,3,4,5,6,9]
target = 7
print(find_indices_of_array(array,target))


