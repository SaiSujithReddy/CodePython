class Node():
    def __init__(self,data=None,nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def get_data(self):
        return self.data



def get_middle_element(head):
    fast_pointer = head
    slow_pointer = head

    while fast_pointer.nextNode != None and fast_pointer.nextNode.nextNode != None:
        fast_pointer = fast_pointer.nextNode.nextNode
        slow_pointer = slow_pointer.nextNode
    print(slow_pointer.get_data())


#Testcase 1
n1 = Node(5)
n2 = Node(4,n1)
n3 = Node(3,n2)
n4 = Node(2,n3)
n5 = Node(1,n4)
head = n5
get_middle_element(head)

#Testcase2
n6 = Node(6)
head = n6
get_middle_element(head)

#Testcase3
n7 = Node(7)
n8 = Node(8,n7)
head = n8
get_middle_element(head)


#Testcase4
n9 = Node()
head = n9
get_middle_element(head)



#Time complexity - O(n)
#SPace complexity - O(1)
