'''

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
sFind two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

'''


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_value = 0
        for index, value in enumerate(height):
            for index1, value1 in enumerate(height):

                if index1 <= index:
                    continue

                else:
                    # print(index,index1,value,value1)
                    if value1 == 0 or value == 0:
                        j = 0
                    else:
                        j = min(value1, value)
                    # print(j)
                    i = index1 - index
                    # print(i)

                    product = i * j
                    # print(product)
                    if (i * j) < 0:
                        product = -1 * (i * j)
                    max_value = max(product, max_value)
                    # max_value = max(((index1 - index)**2**0.5)*((value1-value)**2**0.5))
        return max_value



'''

complexity - O(n**2)
Time limit exceeded

'''


'''
Things learnt
read question more thoroughly 

'''