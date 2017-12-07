class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

class MergeLinkedLists:
    def mergelists(self,list1,list2):
        temp = None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.data < list2.data:
            temp = list1
            temp.next = self.mergelists(list1.next,list2)
        else:
            temp = list2
            temp.next = self.mergelists(list2.next,list1)

        return temp



print('first list is: ')
llist1 = LinkedList()
llist1.push(301)
llist1.push(99)
llist1.push(75)
llist1.push(55)
llist1.push(16)
llist1.push(2)
llist1.printlist()
print
print('second list is: ')
llist2 = LinkedList()
llist2.push(299)
llist2.push(103)
llist2.push(89)
llist2.push(57)
llist2.push(19)
llist2.push(10)
llist2.printlist()


print('Sorted list is: ')
llist3 = LinkedList()
merge = MergeLinkedLists()
llist3.head = merge.mergelists(llist1.head,llist2.head)
llist3.printlist()
