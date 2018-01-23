
class QueueImplementation():
    def __init__(self):
        self.items = []

    def insert(self,item):
        self.items.append(item)

    def extract(self):
        element = self.items[0]
        self.items = self.items[1:]
        return element

    def isEmpty(self):
        return self.items == []

    def print_all(self):
        for x in self.items:
            print(x,end =' ')
        print()

    def size(self):
        return len(self.items)



queue = QueueImplementation()
queue.insert(3)
queue.insert(4)
print(queue.size())
queue.print_all()
print(queue.isEmpty())
print(queue.extract())
queue.print_all()
print(queue.size())

