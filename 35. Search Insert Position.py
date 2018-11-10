class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        for x in range(len(nums)):
            if nums[x] >= target:
                return x
        return x+1




'''
Time - O(n)
Space - O(1)

'''