class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int

        """


        sign = True

        if x < 0:
            sign = False
            x = x*-1
        reverse_str = str(x)[::-1]

        if sign:
            x = int(reverse_str)
            if (x > (2**31 -1)) or (x < -(2**31)):
                #print("i am here")
                return 0
            else:
                return x
        else:
            x = int(reverse_str)*-1
            if (x > (2**31 -1)) or (x < -(2**31)):
                return 0
            else:
                return x


sol = Solution()

x = 1534236469

print(sol.reverse(x))