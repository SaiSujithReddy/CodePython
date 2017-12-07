'''
Given an array of integers with possible duplicates, randomly output the index of a given target number.
You can assume that the given target number must exist in the array.
'''

import random
array = [3,5,1,1,2,4,5]
dict = {}
def feed_to_dict(array):
    #i = 0
    for x in range(0,len(array)):
        if array[x] in dict.keys():
            dict[array[x]].append(x) #= [y for y in dict[x],i]
        else:
            dict[array[x]] = [x]
        #i += 1

feed_to_dict(array)
print(dict)
#
# input = 1
# output = dict[input]
# if(isinstance( output, int )):
#     print(output)
# else:
#     print(random.choice(output))

