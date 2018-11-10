class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length_of_nums = len(nums)

        if length_of_nums == 0:
            return 0
        if length_of_nums == 1:
            return 1
        else:
            count_unique = 0
            for x in range(length_of_nums):
                if x ==0:
                    unique_number = nums[0]
                    count_unique += 1
                else:
                    if nums[x] != unique_number:
                        unique_number = nums[x]
                        count_unique += 1
                        nums[count_unique -1 ] = nums[x]
        return count_unique

nums = [1,2,3,4,4,5]
list_nums = [[1,1,2],[1],[1,2],[1,2,3]]
# list_nums = [[1,1,2]]
sol = Solution()
for x in list_nums:
    print(sol.removeDuplicates(x))



'''
Try again
Simple but tricky.

Time - O(n)
Space - O(1)

'''