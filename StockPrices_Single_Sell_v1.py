'''
Leet code
121. Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

'''

#start_time = 4:46PM

import sys
input = [7, 1, 5, 3, 6, 4]

#local_max = sys.minInt
#global_max = sys.minInt
global_max = 0
buy = input[0]
sell = 0


for x in range(len(input)-1):
    if input[x] < buy:
        buy = input[x]
        #sell = input[x+1]
    if input[x] - buy > global_max:
        global_max = input[x] - buy
print(global_max)