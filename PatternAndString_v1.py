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

def patter_match(words,chars):
    dict_pattern = {}
    dict_words = {}
    if(len(words) != len(chars)):
        return False
    elif(len(words) | len(chars) ==0):
        return False
    else:
        for index, p in enumerate(pattern):
            print(index)
            print(p)
            if p in dict_pattern:
                if dict_pattern[p] != words[index]:
                    return False
            else:
                if words[index] in dict_words:
                    return False
                dict_pattern[p] = words[index]
                dict_words[words[index]] =p
        return True




pattern = "abba"
str = "dog cat cat dog"
str1 = "dog cat cat fish"
words = str.split(" ")
#chars = list(pattern)
print(words)
#print(chars)

print(patter_match(words,pattern))



