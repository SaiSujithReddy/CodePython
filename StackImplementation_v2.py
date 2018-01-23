

class Stack_Implementation:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()

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
