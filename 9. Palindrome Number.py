class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            x_string = str(x)
            return x_string == x_string[::-1]

sol = Solution()
list_x = [121,-121,3,435]
for x in list_x:
    print(sol.isPalindrome(x))