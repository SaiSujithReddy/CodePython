'''
Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.


Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we want to return an integer,
the decimal part will be truncated.

'''

import sys
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x ==0:
            return 0
        left =1
        right = sys.maxsize
        print(right)
        while left < right:
            mid = left + (right - left)/2
            if mid > x/mid:
                right = mid -1
            else:
                if mid +1 > x / (mid +1):
                    return mid
                left = mid+1

sol = Solution()
print(sol.mySqrt(40))


'''
THings learnt 

python max value 

python 3
sys.maxsize

python 2
sys.maxint
sys.minint
'''