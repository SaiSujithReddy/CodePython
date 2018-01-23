string1 = 'Hello'
string2 = 'oehll'

if sorted(string1) == sorted(string2):
    print("{} and {} are anagrams".format(string1, string2))
else :
    print("{} and {} are NOT anagrams".format(string1, string2))



# lower case == upper case
if sorted(string1.lower()) == sorted(string2.lower()):
    print("{} and {} are anagrams".format(string1, string2))
else :
    print("{} and {} are NOT anagrams".format(string1, string2))



from collections import Counter

def is_anagram(str1, str2):
   return Counter(str1) == Counter(str2)

print(is_anagram(string1,string2))
