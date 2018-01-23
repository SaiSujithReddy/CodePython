
'''
70. Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 or 3 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

'''

dic = {1: 1, 2: 2, 3:4}
def climbStairs(n):
    if n not in dic:
        dic[n] = climbStairs(n-1)+climbStairs(n-2)+climbStairs(n-3)
    return dic[n]