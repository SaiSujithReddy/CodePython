
list1 = [2,3,30,1]
list2 = ['+','-']
sum =24

import itertools
#perm = itertools.permutations(input,operations)
#print(list(map(''.join, itertools.chain(itertools.product(list1, list2), itertools.product(list2, list1)))))

#print(perm)
#print(list(itertools.product(list1, list2)))

# perm = [(a,b,c,d,e,f,g,h) for a,c,e,g in list1 for b,d,f,h in list2]
# print(perm)



perm = [(number,operation) for number in list1 for operation in list2]
print(perm)

s = [list1,list2]
permutations = list(itertools.product(*s))
print(permutations)

