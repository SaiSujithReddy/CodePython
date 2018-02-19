array1 = [1,3,2,4,5,6]
array2 = [2,3,7,8,9]

set1 = set()
for x in array1:
    set1.add(x)
for x in array2:
    if x in set1:
        print(x)

sorted_set1 = sorted(set1)
print(sorted_set1)