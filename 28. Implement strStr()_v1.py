class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            return haystack.index(needle)
        except ValueError:
            return -1



sol = Solution()
haystack = "hello"
needle = "ll"
print(sol.strStr(haystack, needle))



'''

things learnt - 
Above solution from discussion. it beat 96 % users.simple and elegant.

time - O(n)
space - O(1)

'''