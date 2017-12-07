'''

Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

'''


import sys

def find132_pattern(numbers) :

    minimum = sys.maxsize

    for j in range(0,len(numbers)):
        minimum = min(numbers[j],minimum)
        if min==numbers[j]:
            pass
        else:
            print("i is ",minimum)
            print("j is ", j)

            for k in range (len(numbers)-1,j,-1):
                print("k is", k)
                if minimum < numbers[k] and numbers[k] < numbers[j]:
                    return True
    return False


#numbers = [1,2,3,4,5]
numbers = [1,2,3,4,5,4]
print(find132_pattern(numbers))

#1  34 45 67 12



'''
Things learnt 
How do you iterate over range in decreasing order
range(5,0,-1)

python maximum integer 
sys.maxsize




'''