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
from collections import Counter
import operator
import sys

class SortAWord:
    def __init__(self,word):
        self.word = word
        self.dict = {}
        self.sorted_dict = []
        #print(sys.version)

    def find_char_freq_v1(self):
        self.dict = Counter(self.word)

    def sort_dict_of_char(self):
        self.sorted_dict = sorted(self.dict.items(), key=operator.itemgetter(1), reverse=True)
        print(self.sorted_dict)

    def return_word(self):
        for x in self.sorted_dict:
            for i in range(0,x[1]):
                print(x[0],end="")

#input = "tree"
#input = "cccaaa"
input = "Aaaaabb"
sortWord = SortAWord(input)
sortWord.find_char_freq_v1()
sortWord.sort_dict_of_char()
sortWord.return_word()



'''
Better concise solution

from collections import Counter
classSolution(object):
    def frequencySort(self, s):   
        """:type s: str 
           :rtype: str        
        """      
        c1, c2 = Counter(s), {}
        for k,v in c1.items():       
            c2.setdefault(v, []).append(k*v)
        return "".join(["".join(c2[i]) for i in range(len(s), -1, -1) if i in c2])

'''