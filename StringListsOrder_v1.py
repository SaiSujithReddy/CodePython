output=[]
text=["abcd","ce","", "","fgh"]
converted_list=[list(x) for x in text]

max_length= len(max(converted_list,key=len))

for l in converted_list:
    padding=max_length-len(l)
    l.extend(['']*padding)

for items in zip(*converted_list):
    output.extend(list(items))
print(''.join(output))

#order is O(n+m) where n is the number of characters of the longest word and m is the number of words in the input





#
# input = ['aaa...aaa', 'a', 'a', 'a'..., 'a', 'a', 'a', 'a']
# len(input[0]) = 10 ^ 9
# len(input) = 10 ^ 9
#
# 10 ^ 9 * 10 ^ 9

# // reverse
# sort
# of
# all
# the
# words
# based
# on
# length
# // remove
# the
# words
# no
# longer
# present - reduces
# the
# loop
# complexity or create
# a
# new
# array
# with remaning characters of the word
# // Can
# you
# hear
# me ?
#
# // time - O(n + m + m) - O(2
# mn) - O(mn)
#
#
# def string_to_char_array(element):
#     return list(element)
#
#
# input = ['abc', 'd', 'ef']
# input_list = []
#
# for x in input:
#     input_list.append(string_to_char_array(x))
#
# print(input_list)
#
# # get largest word length
# max_length_word = max([len(x) for x in input_list])
#
# for i in range(0, max_length_word):
#     for y in input_list:
#
#         if (len(y) > i):
#             print(y[i])
#         else:
#             continue