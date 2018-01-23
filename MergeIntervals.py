'''
Leet code
56. Merge Intervals
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

'''
'''
Initial try with lists merging 

j =0
new_list = [list_ofLists[i][0],list_ofLists[i][1]]

for i in range(0, len(list_ofLists)):
    #print(list_ofLists[i][1])
    print("list_ofLists[i][1]",list_ofLists[i][1])
    print("list_ofLists[i + 1][0]",list_ofLists[i + 1][0])

    if new_list[j][1] > new_list[i][0]:
        # list_of_lists.remove(i,i+1)
        new_list.append([list_ofLists[i][0], list_ofLists[i + 1][1]])
        # list_of_lists.append(i[0],)
    print("new list is ",new_list)

'''


list_ofLists = [[1,3],[2,6],[8,10],[15,18]]
def print_lists(list_ofLists):
    for i in list_ofLists:
        print(i[0],i[1])

print_lists(list_ofLists)
new_list = []
for i in range(len(list_ofLists)-1):
    print(i)
    print(list_ofLists[i])
    if list_ofLists[i][1] > list_ofLists[i+1][0]:
        #temp = list_ofLists[i][1]
        #list_ofLists[i][1] = list_ofLists[i+1][1]
        #list_ofLists[i + 1][0] = list_ofLists[i][0]
        new_list.append([list_ofLists[i][0],list_ofLists[i+1][1]])
        #list_ofLists[i+1][0] = temp
        i += 1
    else:
        new_list.append([list_ofLists[i][0], list_ofLists[i][1]])
print_lists(new_list)


#merge_intervals(list_ofLists)


'''
list_of_lists

Things learnt - How to print list_of_lists 


    for i in lists_of_lists:
        
        if i[1] < i+1[0]:

The above will fail because of list_of_lists out of bound

corect one is 




'''