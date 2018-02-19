'''
140. Word Break II

https://leetcode.com/problems/word-break-ii/description/
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

'''



# Solution with name _v1 is working code
new_dict ={}

def word_break_2(string):
    len_of_string = len(string)
    result = []
    if len_of_string == 0:
        return result

    if string in new_dict:
        result.append(string)

    for i in range(0, len_of_string):
        if string[i:] in dictionary:
            temp = word_break_2(string[:i])
            if temp is not None:
                for j in range(0, len(temp)):
                    result.append(temp[j] + " " + temp)

    new_dict[string] = result
    return result


str = "catsanddog"
dictionary = ["cat", "cats", "and", "sand", "dog"]

print(word_break_2(str))




'''
Solution using DFS and Memorization
Trick is to print all possible sentences 

'''