


class queue:
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def length(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def dequeue

