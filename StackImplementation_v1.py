

class Stack_Implementation:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def pop(self):
        element = self.items[-1]
        self.items = self.items[:len(self.items)-1]
        return element

    def push(self,item):
        self.items.append(item)


S= Stack_Implementation()
S.push(1)
S.push(4)

print(S.peek())
print(S.pop())
print(S.peek())
print(S.isEmpty())
print(S.pop())
print(S.isEmpty())
