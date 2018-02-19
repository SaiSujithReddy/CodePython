'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''

# DFS recursively
class FindSubSets:
    def subsets1(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res


    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)

# Iteratively
def subsets(self, nums):
    res = [[]]
    for num in sorted(nums):
        res += [item + [num] for item in res]
    return res

nums = [1,2,3]
s = FindSubSets()
print(s.subsets1(nums))