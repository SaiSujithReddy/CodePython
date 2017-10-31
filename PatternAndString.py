'''
Question3(LeetCodeQ209):=========================================================================
Givenapatternandastringstr,findifstrfollowsthesamepattern.
Herefollowmeansafullmatch,suchthatthereisabijectionbetweenaletterinpatternandanon-emptywordinstr.
Examples:pattern="abba",str="dogcatcatdog"shouldreturntrue.
pattern="abba",str="dogcatcatfish"shouldreturnfalse.
pattern="aaaa",str="dogcatcatdog"shouldreturnfalse.
pattern="abba",str="dogdogdogdog"shouldreturnfalse.
Notes:Youmayassumepatterncontainsonlylowercaseletters,andstrcontainslowercaselettersseparatedbyasinglespace.
'''
#import nltk
import sys

pattern = "abba"
str = "dog cat cat dog"
str1 = "dog cat cat fish"


#str_tokens = tokens = nltk.word_tokenize(str)
#print(str_tokens)
print(sys.version)