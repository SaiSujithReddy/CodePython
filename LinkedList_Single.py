class Node():
    def __init__(self,data=None,nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def get_data(self):
        return self.data

    def set_data(self,data):
        self.data = data

    def get_nextNode(self):
        return self.nextNode

    def set_nextNode(self,new_node):
        self.nextNode = new_node



class UnorderedList():
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.set_nextNode(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count =0
        while current != None:
            count += 1
            current = current.get_nextNode()
        return count

    def search(self,item):
        current = self.head

        while current.get_nextNode != None:
            if current.get_data() == item:
                return current
            else :
                current = current.get_nextNode()

        return current

    def remove(self,item):

        current = self.head
        previous = self.head
        if self.head == None:
            return None

        if current.get_data() == item:
            self.head = current.get_nextNode()
        else :
            while current.get_nextNode() != None:
                if current.get_data() == item:
                    previous.set_nextNode(current.get_nextNode())
                    current.set_nextNode(None)
                else:
                    previous = current
                    current = current.get_nextNode()


    def print_all(self):
        if self.head == None:
            return
        else :
            current = self.head
            #current.
            while current != None:
                print(current.get_data())
                current = current.get_nextNode()
        # else :
        #     current = self.head
        #     #current.
        #     while current.get_data() != None:
        #         print(current.get_data)
        #         current = current.get_nextNode

myLinkedList = UnorderedList()
myLinkedList.add(1)
myLinkedList.add(2)
myLinkedList.add(3)
myLinkedList.add(4)
myLinkedList.add(5)

myLinkedList.print_all()

length = myLinkedList.size()
print (length)
