class Node():
    def __init__(self,end_node=False):
        self.end_node = end_node
        self.prefix_count = 0
        self.children = {}


class Trie_v1():
    def __init__(self):
        self.root = Node()

    def insert(self, key):
        current = self.root
        for k in key:
            if k not in current.children:
                current.children[k] = Node()
            current = current.children[k]
            current.prefix_count += 1
        current.end_node = True

    def search(self,key):
        current = self.root
        for k in key:
            if k not in current.children:
                return False
            current = current.children[k]
        return current.end_node

    def count(self,key):
        current = self.root
        for k in key:
            if k not in current.children:
                return 0
            current = current.children[k]
        return current.prefix_count

    def _walk(self,root,prefix):
        out = []
        if root.end_node == True:
            out.append(prefix)
        for k in root.children:
            temp = self._walk(root.children[k],prefix+k)
            out.extend(temp)
        return out

    def enumerate(self,key):
        current = self.root
        for k in key:
            if k not in current.children:
                return []
            current = current.children[k]

        return self._walk(current,key)


db = Trie_v1()

db.insert("apple")
db.insert("apples")
db.insert("banana")
db.insert("applet")

print(db.search("apple"))
print(db.search("app"))
print(db.search("bananaa"))
print(db.search(""))
print(db.count("app"))
db.insert("apple")
print(db.count("app"))
print(db.count("b"))
print("*******")
print("")
print(db.enumerate("app"))
print("")
print("")
