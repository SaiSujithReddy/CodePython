class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strs_dict = {}
        for x in strs:
            key = tuple(sorted(x))
            strs_dict[key] = strs_dict.get(key, []) + [x]
        return strs_dict.values()








sol = Solution()
list_z = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(sol.groupAnagrams(list_z))

'''
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

'''


'''
Things learnt 

"

Sort a string in python
''.join(sorted(string))


It is improved version in run time

'''