#This one solves no extra space but with O(n^2)
'''
2.Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime?
You may assume the returned list does not count as extra space.
(Give the hint if approach is not clear in about 10 mins)
Example: Input: [4,3,2,7,8,2,3,1] Output: [5,6]
'''

def get_left_out_elements(given_array,output_array):
    given_array = (x*-1 for x in given_array if given_array(abs(x)) >0)
    output_array = [x for x in output_array if x not in given_array]
    print(output_array)


given_array = [1,3,4,5,5,6,6]
output_array = range(1,len(given_array)+1)
get_left_out_elements(given_array,output_array)
