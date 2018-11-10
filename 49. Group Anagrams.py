class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #for y in range(len(strs))
        strs_dict = {}
        final_list = []
        for x in strs:
            sorted_x = ''.join(sorted(x))
            #print(sorted_x)
            if sorted_x in strs_dict:
                strs_dict[sorted_x].append(x)

            else:
                strs_dict[sorted_x] = [x]

        for x in strs_dict:
            final_list.append(strs_dict[''.join(sorted(x))])

        return final_list







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


It could be improved further by by not joining a sorted string

'''