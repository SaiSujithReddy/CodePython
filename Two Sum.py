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
            if x in nums_dict:
                nums_dict
            else:
                nums_dict[x] = i
            i += 1
        j = 0
        for x in nums:
            #if (target - x)
            if (target - x) in nums_dict and nums_dict[target - x] != j:
                #print([j, nums_dict[target - x]])
                output.append(j)
                output.append(nums_dict[target - x])
                nums_dict.pop(target - x)
                nums_dict.pop(x)
            j += 1
        print(output)


sol = Solution()
#sol.twoSum([2,7,11,15],9)
#sol.twoSum([3,2,4],6)
sol.twoSum([3,3],6)