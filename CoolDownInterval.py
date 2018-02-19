'''
https://careercup.com/question?id=5675602320293888

Given a list of input tasks to run, and the cooldown interval, output the minimum number of time slots required to run them.
// Tasks: 1, 1, 2, 1, 2
// Recovery interval (cooldown): 2
// Output: 8 (order is 1 _ _ 1 2 _ 1 2 )

=========
Tasks are task numbers in that order coming in for execution. Cooling time is time interval required to cool down the machine after executing a task. So it's like if CPU executed task 1 then it needs 2 cooling time intervals before executing another task 1 but meanwhile, it can execute other tasks which are not same as 1 and so on. So before executing any task, you have to check if you have executed same task number before and if yes, then if its cooling time interval is done or not.
The output is basically the number of cycles/time slots CPU took to execute these tasks in that order (including when task executed and cooling intervals).

'''
#start = 3:14


# Things learnt
# array[i:i+1] returns an array not a value
# within elif block make sure you are not missing the else case

input_array = [1,1,2,1,2]

def cool_down(input_array):
    output_array = []
    output_array.append(input_array[0])

    for i in range(1,len(input_array)):

        if input_array[i] == input_array[i - 1]:
            if len(output_array) == 1:
                if output_array[0] == input_array[i]:
                    output_array.append(" ")
                    output_array.append(" ")
                    output_array.append(input_array[i])
            elif output_array[len(output_array)-1:len(output_array)] == input_array[i]:
                output_array.append(" ")
                output_array.append(" ")
                output_array.append(input_array[i])
            elif output_array[len(output_array) - 2:len(output_array)-1] == input_array[i]:
                output_array.append(" ")
                output_array.append(input_array[i])

        elif input_array[i] == input_array[i-2]:
            print(output_array)
            print("value of output_array[len(output_array) - 2s] is ", output_array[len(output_array)-2])
            print("value of input_array is ",input_array[i])
            if len(output_array) == 1:
                output_array.append(" ")
                output_array.append(input_array[i])
            elif output_array[len(output_array) - 2] == input_array[i]:
                output_array.append(" ")
                output_array.append(input_array[i])
            else:
                output_array.append(input_array[i])

        else :
            output_array.append(input_array[i])
    print(output_array)

cool_down(input_array)
