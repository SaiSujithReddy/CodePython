import math
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # for x in range(len(strs)):
        #     temp =""
        #     for

        if len(strs) == 0:
            return ""

        least_length = len(min(strs, key=len))

        # least_length = math.inf
        # for x in strs:
        #     if least_length > len(x):
        #         least_length = len(x)


        i = 0
        least_common_prefix = ""

        while i < least_length:
            temp = strs[0][i]
            for x in range(len(strs)):
                if strs[x][i] == temp:
                    if x == len(strs) -1:
                        least_common_prefix += temp

                    continue
                else:
                    return least_common_prefix
            i += 1
        return least_common_prefix


sol = Solution()
z_list = [["flower","flow","flight"],["dog","racecar","car"],["aca","cba"]]
for z in z_list:
    print(sol.longestCommonPrefix(z))


'''
Time complexity is O(n*m) - n = number of strings, m= length of shortest string
Space = O(1) 

Learnt how to find min length in one line - least_length = min(strs, key=len)


'''