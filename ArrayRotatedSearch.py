'''
33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

'''
import math

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        pivot = 0

    def find_pivot(self,nums,index1,index2):
        #for x in range(len(nums))

        if len(nums) ==1:
            return index1
        elif len(nums) ==2:
            if nums[index1] < nums[index2]:
                return index2
            else:
                return index1
        else:
            if nums[index1] < nums[index2]:
                if nums[index1] < nums[index2]:
                    return index2
                else:
                    return index1
            else:

                if nums[index1] > nums[math.ceil((index2-index1)/2)] and nums[math.ceil((index2-index1)/2)] >

                if nums[index1] > nums[math.ceil((index2-index1)/2)] < nums[index2]:
                    return self.find_pivot(nums,math.floor((index2-index1)/2),index2)
                else:
                    return self.find_pivot(nums,index1,math.ceil((index2-index1)/2))



list_integers = [4,5,6,7,8,9,10,1,2,3]
sol=Solution()
index = sol.find_pivot(list_integers,0,len(list_integers)-1)
print(index)
print(list_integers[index])

# print(13%2)
# print(math.ceil(13/2))



'''
Things learnt 
if you want to divide and get upper boundary
use 
math.ceil()

lower boundary 
math.floor()
'''