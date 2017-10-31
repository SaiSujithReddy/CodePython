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

class Solution:
    def reverse(self,word):
        words = []
        words = word.split(" ")
        print(' '.join(reversed(words)))

#sentence = "the sky is blue"
#sentence = " "
sentence = " a b "
sol = Solution()
sol.reverse(sentence)