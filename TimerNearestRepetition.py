

'''
Problem
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits.
There is no limit on how many times a digit can be reused.
You may assume the given input string is always valid.
For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.
'''

class Solution(object):
    def nextClosestTime(time):
        cur = 60*int(time[:2]) + int(time[3:])
        allowed = {int(x) for x in time if x!= ':'}
        while True:
            cur = (cur+1)%(24*60)
            #print(cur)
            if all (digit in allowed
                    for block in divmod(cur,60)
                    for digit in divmod(block,10)):
                return "{:02d}:{:02d}".format(*divmod(cur,60))

    print(nextClosestTime("21:35"))
    # for block in divmod(45,13):
    #     print(block)
    #     print("hello")
    #     for digit in divmod(block,10):
    #         print(digit)
    #         print("bye")
