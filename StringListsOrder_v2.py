import itertools

output=[]
text=["abcd","ce","fgh"]

#converted_list=[list(x) for x in text]

#for i in itertools.zip_longest(converted_list): print(i)

# spacious = "   xyz   "
# print(spacious.strip())
#
# spacious = "   xyz   "
# print(spacious.lstrip())
#
# spacious =  "xyz   "
# print(spacious.rstrip())

max_length= len(max(text,key=len))
output = []

def print_first_each_letter(text):
    # for x in range(0,max_length):
    #     print( [s[x] for s in text if len(s) > x ])

    for x in range(0,max_length):
        output.append([s[x] for s in text if len(s) > x ])

print_first_each_letter(text)
for x in output:
    print(x)