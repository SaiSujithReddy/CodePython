'''
33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

'''

class Solution:
    # @param {integer[]} numss
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = int(low + (high-low) / 2)

            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

list_integers = [4,5,6,7,8,9,10,1,2,3]
sol=Solution()
print(sol.search(list_integers,11))

'''
Things learnt 
if you want to divide and get upper boundary
use 
math.ceil()

lower boundary 
math.floor()


for mid never use (low+high)/2
always use low + (high-low)/2
because if low and higher are both very large numbers it could overflow
 
'''