class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        len_needle = len(needle)
        len_haystack = len(haystack)
        if len_haystack == 0 and len_needle == 0:
            return 0
        elif len_needle > len_haystack:
            return -1
        elif len_needle == 0 and len_haystack > 0:
            return -1
        else:
            for x in range(len_haystack):
                if haystack[x:x+len_needle] == needle:
                    return x
            return -1




sol = Solution()
haystack = "hello"
needle = "ll"
print(sol.strStr(haystack, needle))



'''

things learnt - check the null . corner cases before submitting
Above solution beat just 36% users.

time - O(n)
space - O(1)

'''