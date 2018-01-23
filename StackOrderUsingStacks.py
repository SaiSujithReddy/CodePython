
def stack_order_using_stacks(list_of_numbers):
    stack_temp = []
    stack_temp_2 = []
    stack_temp.push(list_of_numbers[0])
    for x in range(1,len(list_of_numbers)):
        if list_of_numbers[x] < stack_temp[-1]:
            print("stack_temp[-1] is ", stack_temp[-1])
            continue
        else:
            stack_temp_2.push(stack_temp.pop())
            stack_temp.push(list_of_numbers[x])
            stack_temp.push(stack_temp_2.pop())

        print("stack_temp is ", stack_temp)
        print("stack_temp_2 is ", stack_temp_2)
        #print("stack_temp is ", stack_temp)


list_of_numbers = [3,2,7,9,5,6,1,19,4]
stack_order_using_stacks(list_of_numbers)