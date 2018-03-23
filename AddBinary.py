'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".


'''


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        length_a = len(a)
        length_b = len(b)
        if length_a == 0:
            return b
        if length_b == 0:
            return a
        # print(a[-1])
        # print(a[0:-1])
        if a[-1] =='1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
        elif a[-1] =='0' and b[-1] == '0':
            return self.addBinary(a[0:-1],b[0:-1])+'0'
        else:
            return self.addBinary(a[0:-1],b[0:-1])+'1'
        # for x in range(len(a)-1,-1,-1):
        #     print(a[x])
        #
        # while length_a > -1 and length_b > -1:
        #     result += a[length_a]





a = "11"
b = "1"
sol = Solution()
print(sol.addBinary(a,b))


'''
Things learnt
Say a = "1234"
How do you print 4 ?
a[-1]
How do you print 123 ?
a[0:-1]


Try to match with string not int

wrong way 

if a[-1] ==1 and b[-1] == 1:

correct

if a[-1] =='1' and b[-1] == '1':

    return self.addBinary(a[0:-1],b[0:-1])+1
TypeError: must be str, not int



'''