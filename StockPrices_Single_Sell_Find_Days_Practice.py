#Previous

import sys


def find_max_profit(input_list):

    buy = sys.maxsize
    sell = - sys.maxsize -1

    buy_index =0
    sell_index =0

    buy_list = []
    sell_list = []

    for index, value in enumerate(input_list):
        if value < buy:
            buy = value
            buy_index = index

        if value - buy > sell and index >= sell_index:
            sell = value
            sell_index = index
    if sell == (- sys.maxsize -1) or buy == sys.maxsize:
        return (0,0,0)
    if buy_index == len(input_list)-1 and sell_index == 0:
        return (0,0,0)
    return (sell-buy,buy_index,sell_index)



# def find_max_loss(input_list):
#     buy = - sys.maxsize -1
#     sell = sys.maxsize
#
#     buy_index =0
#     sell_index =0
#
#     for index, value in enumerate(input_list):
#         if value > buy:
#             buy = value
#             buy_index = index
#
#         if value - buy > sell and index >= buy_index:
#             sell = value
#             sell_index = index
#     if sell == (- sys.maxsize -1) or buy == sys.maxsize:
#         return (0,0,0)
#     return (sell-buy,buy_index,sell_index)


sample_input_list = [[1,5,3,9,2,6,4,1,8],
                    [1,2,3,4,5,6,7,8,9],
                    [7,6,5,4,3,2,1],
                     [1,10]]

for x in sample_input_list:
    print("max gain is ",find_max_profit(x))
    # print("max loss is ",find_max_loss(x))