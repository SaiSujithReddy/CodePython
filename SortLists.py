my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]


def do_merge(list1,list2):
    i = len(list1)

    for x in range(len(list1)):
        list1[len(list1)+x] = 0

    k = len(list1)
    j = len(list2)

    while i > 0:
        if list1[i-1] > list2[j-1]:
            list1[k] = list1[i-1]
        else:
            list2[j-1] = list1[i - 1]

def merge_lists(list1,list2):
    if len(list1) > len(list2):
        do_merge(list1,list2)
    else:
        do_merge(list2,list1)

print(merge_lists(my_list, alices_list))
# prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]