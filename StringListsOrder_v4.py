text=["abcd","ce","fghijkl"]
# print list(text[0])

converted_list=[list(x) for x in text]
max_length= len(max(converted_list,key=len))

for l in converted_list:
    padding=max_length-len(l)
    l.extend(['']*padding)
# print converted_list

built_string= ','.join(["converted_list["+str(i)+"][i]" for i in range(len(converted_list))])

output=[]

for i in range(0,max_length):
    output.extend(list(eval(built_string)))

print(''.join(output))