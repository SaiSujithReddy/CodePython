'''
Question:-
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:Input:"tree" Output:"eert" Explanation:'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.


Example 2:Input:"cccaaa" Output:"cccaaa" Explanation:Both 'c' and 'a' appear three times,
so "aaaccc" is also a valid answer. Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:Input:"Aabb" Output:"bbAa" Explanation:"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

'''

'''
Forgot how to use operator

'''
import operator

def sortDecOrder(input):
    dict_char = {}
    print(list(input))

    for x in list(input):
        if x in dict_char:
            dict_char[x] += 1
        else:
            dict_char[x] = 1

    sorted_dict_char_by_value = []
    sorted_dict_char_by_value = sorted(dict_char.items(),key=operator.itemgetter(1),reverse=True)

    for x in sorted_dict_char_by_value:
        for y in range(0,x[1]):
            print(x[0],end="")



sortDecOrder("tree")


