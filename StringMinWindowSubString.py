'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

'''


def lastIndex(words, keywords):
    last = 0
    for keyword in keywords:
        try:
            i = words.index(keyword)
            words = words[i + 1:]
            last += i
        except ValueError:
            raise
    return last + 1


def minSubstring(words, keywords):
    first = keywords[0]
    startIndex = endIndex = 0

    for i, word in enumerate(words):
        if first != word:
            continue
        try:
            start = i
            end = lastIndex(words[start + 1:], keywords[1:])
            if end - start > startIndex - endIndex:
                startIndex = start
                endIndex = start + end
        except ValueError:
            continue

    if startIndex != 0:
        return words[startIndex:endIndex + 1]
    else:
        return ''