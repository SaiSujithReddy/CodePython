'''
Question2(LeetcodeQ151):
=========================================================================
Givenaninputstring,reversethestringwordbyword.
Forexample,Givens="the sky is blue",return"blue is sky the".

MAKESUREYOURCODECANPASSTHETESTCASES--Testcases--
reserve_words("theskyisblue")=="blueisskythe"
reserve_words(""))==""
reserve_words("ab"))=="ba"

BONUS
Supposetheinputisalist,
solvetheproblemin
O(1)space
--TestcasesforBONUS--
reserve_words(list("theskyisblue"))==['b','l','u','e','','i','s','','s','k','y','','t','h','e']


'''

def reverse_words(input):
    if input is None or input.strip() is None:
        return None
    y = input.split()
    return ' '.join(reversed(y))
    '''  
    for x in range(len(y)-1,0,-1):
        print(y[x])
    for x in input.split():
    '''


input = "the sky is blue"
input = ""
input = "a b"
input = " "
print(reverse_words(input))


'''
Now lets solve for no extra space 
'''

def reverse_words_v1(input):
    if input is None:
        return None
    return ' '.join(reversed(input.split()))

input1 = "the sky is blue"
input = ""
input = "a b"
print(reverse_words(input1))

'''
Now lets solve for lists of words
'''

def reverse_words_list(input_list):
    if input is None:
        return None
    for x in range(len(input_list)-1,-1,-1):
        print(input_list[x], end=" ")

input_list = ['the','sky','is','blue']

reverse_words_list(input_list)
