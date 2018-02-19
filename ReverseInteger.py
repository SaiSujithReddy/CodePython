'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
 For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.



'''


def reverseInteger(x):

    output = ""
    if x > 2**31 -1:
        return 0
    elif x < -2**31:
        return 0
    elif x > 0 :
        while x > 9:
            output += str(x % 10)
            x = int(x / 10)
        output += str(x)
    elif x < 0 :
        output += "-"
        x *= -1
        while x > 9:
            output += str(x % 10)
            x = int(x / 10)
        output += str(x)
    else:
        return 0
    return int(output)


list_integers = [123,-987,0,-6,8,100]

for x in list_integers:
    print(int(reverseInteger(x)))

