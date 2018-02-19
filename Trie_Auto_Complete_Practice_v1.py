class Node:
    def __init__(self,end_node=False):
        self.end_node = end_node
        self.children = {}
        self.count = 0

class AutoComplete:
    def __init__(self):
        self.root = Node()

    def insert(self,key):
        current = self.root

        for k in key:
            if k not in current.children:
                current.children = Node(k)
            current.count += 1
            current = current.children[k]
        current.end_node = True

    def remove(self,key):
        current = self.root

        #for

    def _walk(self,root,prefix):
        output = []
        #current = self.root

        if root.end_node:
            output.append(prefix)
        for k in root.children:
            output.extend(self._walk(root.children[k],prefix+k))
        return output

    def enumerate(self,key):
        current = self.root
        return self._walk(current,key)


db = AutoComplete()
db.insert("apple")
db.insert("apples")
db.insert("banana")
db.insert("applet")
print(db.enumerate("app"))
