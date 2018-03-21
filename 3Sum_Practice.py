'''

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets
 in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sorted_nums = sorted(nums)
        #print(sorted_nums)
        final_list = []

        for x in range(len(sorted_nums)-2):
            if sorted_nums[x] >0:
                return final_list
            else:
                # if x > 0 and sorted_nums[x] == sorted_nums[x - 1]:
                #     continue
                y = x + 1
                # while sorted_nums[x] == sorted_nums[y] and y < len(sorted_nums)-2:
                #     y += 1
                z = len(sorted_nums) -1
                target = sorted_nums[x]*-1
                while z > y:
                    if sorted_nums[y] + sorted_nums[z] > target:
                        z -= 1
                    elif sorted_nums[y] + sorted_nums[z] < target:
                        y += 1
                    else:
                        if [sorted_nums[x],sorted_nums[y],sorted_nums[z]] in final_list:
                            pass
                        else:
                            final_list.append([sorted_nums[x],sorted_nums[y],sorted_nums[z]])
                            while sorted_nums[x] == sorted_nums[y] and y < z:
                                y += 1
                            while sorted_nums[x] == sorted_nums[z] and z > y:
                                z -= 1
                        z -= 1
                        y += 1
        return final_list


S = [-1, 0, 1, 2, -1, -4]
#S = [-1, 0, 1, 2,2,2, -1, -4]
#S = [0,0,0]

sol = Solution()
print(sol.threeSum(S))

'''
Complexity
nlogn for sorting 
n**n for iterations
n for checking in lists

so finally O(n**2)

'''
'''
Status: Time Limit Exceeded
'''


'''
Things learnt

How to check if an element exists in list

O(n)
if myItem in list:
    # do something

'''