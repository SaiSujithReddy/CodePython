

input1 = ['abc', 'de', 'ghi']


input_list = []
for x in input1:
    input_list.append(list(x))
#y = [x for x in list(input1)]
#print(y)



for a,b,c in zip (*input_list):
    print(a,b,c)



print(input_list)
for a,b,c in zip (*input_list):
    print(a,b,c)

