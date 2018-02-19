'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one
and sell one share of the stock multiple times).

However, you may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).

'''

import sys

#Not working solution
def find_max_profit(input_list):

    buy = sys.maxsize
    sell = - sys.maxsize -1

    buy_index =0
    sell_index =0

    buy_list = []
    sell_list = []

    buy_index_list = []
    sell_index_list = []

    for index, value in enumerate(input_list):
        if value < buy:

            buy = value
            buy_index = index

        if value - buy > sell and index >= sell_index:
            if sell != (- sys.maxsize -1) and buy != sys.maxsize:
                sell_list.append(sell)
                sell_index_list.append(sell_index)
                buy_list.append(buy)
                buy_index_list.append(index)

            sell = value
            sell_index = index
    if sell == (- sys.maxsize -1) or buy == sys.maxsize:
        return (0,0,0)
    if buy_index == len(input_list)-1 and sell_index == 0:
        return (0,0,0)
    #return (sell-buy,buy_index,sell_index)
    print(sell,buy)
    return (sell_list,buy_list,sell_index_list,buy_index_list)




sample_input_list = [[1,5,3,9,2,6,4,1,8],
                    [1,2,3,4,5,6,7,8,9],
                    [7,6,5,4,3,2,1],
                     [1,10]]

for x in sample_input_list:
    print("max gain is ",find_max_profit(x))
    # print("max loss is ",find_max_loss(x))