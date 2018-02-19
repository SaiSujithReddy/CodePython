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


#
# local_max = 0
# global_max = 0
#
# buying_index =0
# selling_index =0
#
# for x in range(len(input)-1):
#     for y in range(x,len(input)):
#         if input[y] > input[x]:
#             local_max = input[y] - input[x]
#             if local_max > global_max:
#                 buying_index = x
#                 selling_index = y
#                 global_max = local_max
# print(global_max,buying_index,selling_index)
#

#input = [7, 1, 5, 3, 6, 4]
#input = [1, 5, 3, 6, 4]


#Better sol in StockPrices_Single_Sell_Find_Days_Practice.py
input = [1, 2, 3, 4, 5]
global_max = 0
buy = input[0]
sell = 0
buying_index = 0
selling_index = 0


for x in range(len(input)):
    if input[x] < buy:
        buy = input[x]
        buying_index = x
    if input[x] - buy > global_max:
        selling_index = x
        global_max = input[x] - buy
print(global_max,buying_index,selling_index)