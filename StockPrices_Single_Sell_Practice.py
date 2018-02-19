

def find_max_profit(input_list):
    #local_min,global_min,local_max,global_max = input[0]
    #local_min_index,global_min_index,local_max_index,global_max_index = 0

    buy = input_list[0]
    sell = input_list[0]

    for value in input_list:
        if value < buy:
            buy = value

        if value - buy > sell:
            sell = value
    return sell-buy


def find_max_loss(input_list):
    buy = input_list[0]
    sell = input_list[0]

    for value in input_list:
        if value > buy:
            buy = value

        if value - buy > sell:
            sell = value
    return sell-buy


sample_input_list = [1,5,3,9,2,6,4,1,8]
print(find_max_profit(sample_input_list))
print(find_max_loss(sample_input_list))