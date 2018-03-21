'''
26. Remove Duplicates from Sorted Array

Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.

'''




class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            i =1
            for x in range(len(nums)):
                if nums[x] == nums[i]:
                    x += 1
                elif i == len(nums) -1:

                    return i+1
                else:
                    x += 1
                    i += 1
        return i


nums = [1,2,3,4,4,5]
list_nums = [nums,[1,1,2],[1],[1,2],[1,2,3]]
sol = Solution()
for x in list_nums:
    print(sol.removeDuplicates(x))
