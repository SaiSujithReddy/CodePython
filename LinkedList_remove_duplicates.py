class Node:
    def __init__(self,data=None,nextNode=None):
        self.data = data
        self.next = nextNode

    def get_data(self):
        return self.data


    def print_all(self):
        while self.next is not None:
            print(self.data)
            self = self.next
        print(self.data)

    def check_and_remove_duplicates(self):
        dictionary = {self.data: 1}
        while self.next is not None:
            if self.next.data in dictionary:
                if self.next.next is None:
                    self.next = None
                else:
                    self.next = self.next.next

            else:
                dictionary[self.next.data] = 1
            self = self.next


n1 = Node(1)
n2 = Node(2,n1)
n3 = Node(3,n2)
n4 = Node(2,n3)
n5 = Node(5,n4)
n6 = Node(6,n5)
n7 = Node(7,n6)
n8 = Node(8,n7)

n8.print_all()
n8.check_and_remove_duplicates()
n8.print_all()