'''
Implementing a Stack in Python

'''

class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self,item):
        return self.items.pop()

    def peek(self,item):
        self.items[len(self.items)-1]