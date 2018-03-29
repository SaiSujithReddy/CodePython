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
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        output = '1'
        if n == 1:
            return output
        else:
            start = 1
            while start < n:

                output_int = (int(output))
                list_output_int = [int(x) for x in str(output_int)]
                continuous_count = 1
                for x in range(len(list_output_int)):
                    if x != len(list_output_int) -1:
                        if list_output_int[x] == list_output_int[x+1]:
                            continuous_count += 1
                            continue
                        else:
                            if continuous_count != 1:
                                output += str(continuous_count)+str(output_int[x])
                            else:
                                output += str(continuous_count) + str(list_output_int[x])
                    else:
                        output = str(continuous_count) + str(list_output_int[x])

                start += 1
            return output




sol = Solution()
print(sol.countAndSay(1))
print(sol.countAndSay(2))
print(sol.countAndSay(3))
print(sol.countAndSay(4))
#
# num = '123'
# print(int(num))
# list_A = [int(x) for x in str(num)]
# print(len(list_A))