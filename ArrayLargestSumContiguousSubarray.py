#https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

#Kadane’s Algorithm:

def find_max_sum_continguos_array(input_array):
    max_sum_temp = 0
    max_sum_so_far = 0

    for x in input_array:
        max_sum_temp += x
        if max_sum_temp <0:
            max_sum_temp = 0
        if max_sum_so_far < max_sum_temp:
            max_sum_so_far = max_sum_temp
    return max_sum_so_far

in_ar = [-2, -3, 4, -1, -2, 1, 5, -3]
print(find_max_sum_continguos_array(in_ar))