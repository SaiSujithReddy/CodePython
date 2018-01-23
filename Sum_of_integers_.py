

def find_sum_subtract_of_words_exist(input,sum):

    print("Input is ", input)
    print("Sum is ", sum)

    if sum > 0:
        sum = sum - input[0]
        if (len(input)) > 1:
            find_sum_subtract_of_words_exist(input[1:],sum)
        else:
            return sum == 0
    else:
        sum = sum + input[0]
        if (len(input)) > 1:
            find_sum_subtract_of_words_exist(input[1:],sum)
        else:
            return sum == 0




input = [2,3,30,1]
sum =24

print(find_sum_subtract_of_words_exist(input,sum))