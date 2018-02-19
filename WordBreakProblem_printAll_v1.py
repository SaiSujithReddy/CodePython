'''
140. Word Break II


Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

'''

#https://leetcode.com/problems/word-break-ii/discuss/44311

# here we are iterating through each word in the dictionary which would be costly if the dictionary is too long
#Worst case is O(n**2) where n is no of keys in dictionary

def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: List[str]
    """
    return helper(s, wordDict, {})


def helper(s, wordDict, memo):
    if s in memo:
        return memo[s]
    if not s:
        return []

    res = []
    for word in wordDict:
        if not s.startswith(word):
            continue
        if len(word) == len(s):
            res.append(word)
        else:
            resultOfTheRest = helper(s[len(word):], wordDict, memo)
            for item in resultOfTheRest:
                item = word + ' ' + item
                res.append(item)
    memo[s] = res
    return res

str = "catsanddog"
dictionary = ["cat", "cats", "and", "sand", "dog"]

print(wordBreak(str,dictionary))




'''
Solution using DFS and Memorization
Trick is to print all possible sentences 

'''