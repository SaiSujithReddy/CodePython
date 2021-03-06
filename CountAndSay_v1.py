'''

38. Count and Say
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"



'''


class Solution:
    def countAndSay_v1(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n - 1):
            let, temp, count = s[0], '', 0
            for l in s:
                if let == l:
                    count += 1
                else:
                    temp += str(count) + let
                    let = l
                    count = 1
            temp += str(count) + let
            s = temp
        return s



sol = Solution()
print(sol.countAndSay_v1(1))
print(sol.countAndSay_v1(2))
print(sol.countAndSay_v1(3))
print(sol.countAndSay_v1(4))
print(sol.countAndSay_v1(50))
#
# num = '123'
# print(int(num))
# list_A = [int(x) for x in str(num)]
# print(len(list_A))