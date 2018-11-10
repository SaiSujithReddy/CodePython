class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict_parentesis = {"}":"{", ")":"(",">":"<","]":"[" }

        stack = []
        for char in s:
            if len(stack) == 0:
                stack.append(char)
            else:
                # temp =
                #print()
                if char in dict_parentesis:
                    if dict_parentesis[char] == stack[-1]:
                        stack.pop()
                    else:
                        stack.append(char)
                else:
                    stack.append(char)
        if len(stack) == 0:
            return True
        else:
            return False

        #return True



sol = Solution()

z_list = ["()","()[]{}","(]","([)]","{[]}"]
for z in z_list:
    print(sol.isValid(z))


'''
Time - O(n)
Space - O(n)

'''