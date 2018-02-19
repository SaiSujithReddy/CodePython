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




#Better sol in StockPrices_Single_Sell_Find_Days_Practice.py
input = [7, 1, 5, 3, 6, 4]

local_max = 0
global_max = 0

buying_index =0
selling_index =0

for x in range(len(input)-1):
    for y in range(x,len(input)):
        if input[y] > input[x]:
            local_max = input[y] - input[x]
            if local_max > global_max:
                buying_index = x
                selling_index = y
                global_max = local_max
print(global_max,buying_index,selling_index)