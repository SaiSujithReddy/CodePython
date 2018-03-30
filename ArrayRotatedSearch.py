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
        if len(nums) > 0:
            pivot = self.find_pivot(nums,0,len(nums)-1)
            print("pivot is ",pivot)
            print("pivot element is ", nums[pivot])
            if nums[0] == target:
                return 0
            elif nums[len(nums) - 1] == target:
                return len(nums) - 1
            elif nums[pivot] == target:
                return pivot

        else:
            return -1

    def search_inside(self, nums, target):
        if nums[0] == target:
            return 0
        elif nums[len(nums)-1] == target:
            return len(nums)-1
        elif nums[pivot] == target:
            return pivot
        else:
            if nums[0]



    def find_pivot(self,nums,index1,index2):
        #for x in range(len(nums))

        # print("elemnts are", nums)
        # print("index1 element is {} and index is {}",nums[index1],index1)
        # print("index2 element is {} and index is {}", nums[index2], index2)

        if len(nums[index1:(index2)+1]) ==1:
            return index1
        elif len(nums[index1:(index2)+1]) ==2:
            if nums[index1] < nums[index2]:
                return index2
            else:
                return index1
        else:

                if nums[index1] > nums[math.ceil((index2+index1)/2)] and nums[math.ceil((index2+index1)/2)] < nums[index2]:
                    #print("Hi1")
                    return self.find_pivot(nums,index1,math.ceil((index2+index1)/2))
                elif nums[index1] < nums[math.ceil((index2+index1)/2)] and nums[math.ceil((index2+index1)/2)] > nums[index2]:
                    #print("Hi2")
                    return self.find_pivot(nums,math.floor((index2+index1)/2),index2)
                elif nums[index1] < nums[math.ceil((index2+index1)/2)] and nums[math.ceil((index2+index1)/2)] < nums[index2]:
                    #print("Hi3")
                    return index2
                elif nums[index1] > nums[math.ceil((index2+index1)/2)] and nums[math.ceil((index2+index1)/2)] > nums[index2]:

                    # print("value of nums[index1] is",nums[index1] )
                    # print("value of nums[index2] is", nums[index2])
                    # print("value of nums[math.ceil((index2+index1)/2)] is", nums[math.ceil((index2+index1)/2)])
                    # print("Hi4")
                    return index1




list_integers = [4,5,6,7,8,9,10,1,2,3]
sol=Solution()
#index = sol.find_pivot(list_integers,0,len(list_integers)-1)
sol.search(list_integers,2)

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