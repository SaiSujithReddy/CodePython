class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        output = []
        i = 0

        for x in nums:
            if target -x in nums_dict:
                output.append(i)
                output.append(nums_dict[target - x])
                nums_dict.pop(target - x)
            else:
                nums_dict[x] = i
            i += 1

        #     i += 1
        # j = 0
        # for x in nums:
        #     if (target - x) in nums_dict and nums_dict[target - x] != j:
        #         #print([j, nums_dict[target - x]])
        #
        #
        #
        #         nums_dict.pop(x)
        #     j += 1
        return output

sol = Solution()
print(sol.twoSum([2,7,11,15],9))
print(sol.twoSum([3,2,4],6))
print(sol.twoSum([3,3],6))