'''


'''
import random
list_A = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]



def weighted_choice(weights):
    totals = []
    running_total = 0

    for w in weights:
        running_total += w
        totals.append(running_total)

    rnd = random.random() * running_total
    print("rnd value is {}, running_total value is {} ",rnd, running_total)
    for i, total in enumerate(totals):
        if rnd < total:
            return i

for i in range(15):
    print(list_A[weighted_choice(list_A)])