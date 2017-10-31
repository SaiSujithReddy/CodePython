# Find indices of all elements in an array that add up to a given target
# What if we want to return all the indices which can sum ? - Done

# Improvements
# TC - O(n)
# SC - O(1)


def find_indices_of_array(array_num,target):
    dict_indices = {}
    i = 0
    list_of_indices = []
    for index, num in enumerate(array):
        dict_indices[num] = index
        if target - num in dict_indices:
            list_of_indices.append((index, dict_indices.get(target - num)))
    return list_of_indices

array = [1,2,3,4,5,6,9]
target = 10
print(find_indices_of_array(array,target))


