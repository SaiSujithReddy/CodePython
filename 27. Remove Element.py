class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length_nums = len(nums)
        if length_nums == 0:
            return 0

        count_other = 0
        list_index_val = []

        for x in range(length_nums):
            if nums[x] == val:
                list_index_val.append(x)
            else:
                count_other += 1

        nums = [i for j, i in enumerate(nums) if j not in list_index_val]

        print(nums)
        return count_other

sol = Solution()
nums = [[[3,2,2,3],3],[[0,1,2,2,3,0,4,2],2]]
for z in nums:
    [num, val] = z
    print(sol.removeElement(num, val))

'''

Though stdout is correct, the leetcode says output is incorrect

don't make a list of removable indices and then keep popping from list, it is a mistake since the indices changes as 
soon as you pop the first index

Time - O(2n) ~ O(n)
Space - O(n)

'''