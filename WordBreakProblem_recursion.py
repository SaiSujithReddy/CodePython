'''
Word Break Problem: Given a string and a dictionary of words,
determine if string can be segmented into a space-separated sequence of one or more dictionary words.


dict = {"a","k", "br","bre", "break", "brea", "ak","problem","this","th", "is", "famous", "word", "break", "b","r", "e"}
string = "wordbreakproblem"

<p>Word b r e a k problem<br />
Word b r e ak problem<br />
Word br e a k problem<br />
Word br e ak problem<br />
Word bre a k problem<br />
Word bre ak problem<br />
Word brea k problem<br />
Word break problem<br />

#source - http://www.techiedelight.com/word-break-problem/
'''

def word_assemble(dict,string):

    #end of string ? print string
    if len(string) ==0:
            return True

    for i in range(0,len(string)+1):
        prefix = string[:i]
        if prefix in dict and word_assemble(dict,string[i:]):
            return True
    return False

dict = {"a","k", "br","bre", "break", "brea", "ak","problem","this","th", "is", "famous", "word", "break", "b","r", "e"}
string = "wordbreakproblem"

print(word_assemble(dict,string))


# Time - O(n**2)