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

for x in dictionary:
    print(x)

def word_break(string):
    len_of_string = len(string)
    if len_of_string == 0:
        return True

    print("String is ", string)

    for i in range(0,len_of_string+1):
        print("searching for rest of the word", string[:i])
        if string[:i] in dictionary and word_break(string[i:len_of_string]):
            return True
    return False


print(word_break("ilikesamsung"))

# Time - O(n**2)  where n is the length of the string
