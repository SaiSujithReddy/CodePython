'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

from collections import deque


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack_string = deque()

        if len(s)%2 == 1:
            return False
        else:
            for x in s:
                if len(stack_string) != 0 :
                    y = stack_string.pop()
                    if self.match(x, y):
                        continue
                    else:
                        stack_string.append(y)
                        stack_string.append(x)
                else:
                    stack_string.append(x)
            if len(stack_string) == 0:
                return True
            else:
                return False

    def match(self,charB,charA):
        if charA is '(' and charB is ')':
            return True
        elif charA is '{' and charB is '}':
            return True
        elif charA is '[' and charB is ']':
            return True

        return False


list_of_strings = ["{}[]()","{[]()","[{}()]","["]
sol = Solution()
for x in list_of_strings:
    print(sol.isValid(x))



'''
Things learnt
stack in python
There is no peek on list

you have to use deque
from collections import deque
q = deque()

'''