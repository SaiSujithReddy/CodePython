'''

Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. See following examples for more details.
This is a famous Google interview question, also being asked by many other companies now a days.

Consider the following dictionary
{ i, like, sam, sung, samsung, mobile, ice,
  cream, icecream, man, go, mango}

Input:  ilike
Output: Yes
The string can be segmented as "i like".

Input:  ilikesamsung
Output: Yes
The string can be segmented as "i like samsung"
or "i like sam sung".

'''



dictionary = {"mobile", "samsung", "sam", "sung",
              "man", "mango", "icecream", "and",
              "go", "i", "like", "ice", "cream"}

def word_break(string):
    len_of_string = len(string)
    if len_of_string == 0:
        return True

    wb = []
    wb = [ False for i in range(0,len_of_string)]


    for i in range(0,len_of_string+1):
        print("String is ",string[:i])
        print(wb)
        if (wb[i] == False and string[:i] in dictionary):
            wb[i] = True

        if (wb[i] == True):
            if i == len_of_string:
                return True
            for j in range(i,len_of_string):
                if wb[j] == False and string[i:j-i] in dictionary:
                    wb[j] = True
                if j == len_of_string and wb[j] == True:
                    return True


print(word_break("ilikesamsung"))


#Things learnt - how to initialize a list in python with all false values
# wrong answer
# for i in range(0,something):
#     new_list[i] = False
#
# Correct
# new_list = [False for i in range(0,something)]