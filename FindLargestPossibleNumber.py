'''
Question1(LeetcodeQ179):==============
Givenalistofnonnegativeintegers,arrangethemsuchthattheyformthelargestnumber.
Forexample,given[3,30,34,5,9],thelargestformednumberis 9534330.
Note:Theresultmaybeverylarge,soyouneedtoreturnastringinsteadofaninteger

--Testcases--
largestNumber([3,30,34,5,9])=="9534330"
largestNumber([])=="0"
'''

class Solution:
        #self.num = num
    # @param num, a list of integers
    # @return a string
    def largestNumber(self,num):
        num = [str(x) for x in num]
        print(num)
        num.sort(cmp=lambda x, y: cmp(y+x, x+y))
        print(num)
        print(''.join(num).lstrip('0') or '0')


array = [3,30,34,5,9]
solution = Solution()
solution.largestNumber(array)
