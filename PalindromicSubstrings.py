'''

647. Palindromic Substrings

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.

'''
#import xrange

'''
Python3 range = python2 xrange

Initial thought process
each letter
put_in_to dictionary each unique letter and add count as value
'''

#solution from leetcode

# Time - o(n**2)


def count_substrings(S):
    N = len(S)
    ans = 0
    for center in range(2*N - 1):
        left = int(center / 2)
        right = int(left + center % 2)
        # print(left)
        # print(right)
        # print(N)
        # print(left)
        # print(right)
        # print(S[left])
        # print(S[right])
        while left >= 0 and right < N and S[left] == S[right]:
            ans += 1
            left -= 1
            right += 1
    return ans


print(count_substrings("aabcde"))
