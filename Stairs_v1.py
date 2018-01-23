
'''
70. Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 or 3 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

'''
class Solution:

    def __init__(self):
        self.dic = {1: 1, 2: 2, 3:4}

    def climbStairs(self,n):
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2) + self.climbStairs(n - 3)
        return self.dic[n]

solution = Solution()
print(solution.climbStairs(4))

# improved with memorization