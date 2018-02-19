import unittest

class Node:
    def __init__(self):
        self.prefix_count = 0
        self.children = {}
        self.end_node = False

class Trie:
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

    def search(self, key):
        current = self.root
        for k in key:
            if k not in current.children:
                return False
            current = current.children[k]
        return current.end_node

    def _walk(self, root, prefix):
        out = []
        if root.end_node:
            out.append(prefix)
        for x in root.children:
           temp = self._walk(root.children[x], prefix+x)
           out.extend(temp)
        return out

    def enumerate(self,key):
        current = self.root
        for k in key:
            if k not in current.children:
                return []
            current = current.children[k]
        return self._walk(current, key)

    def count(self,key):
        current = self.root
        for k in key:
            if k not in current.children:
                return 0
            current = current.children[k]
        return current.prefix_count


trie = Trie()
trie.insert("Hello")
trie.insert("How")
trie.insert("Heater")

search_list = ["Hello", "Howdo", "Heater"]
for x in search_list:
    print(trie.search(x))

walk_list = ["H","Ho","He"]
for x in walk_list:
    print(trie.enumerate(x))

for x in walk_list:
    print(trie.count(x))


class TestTrieMethods(unittest.TestCase):

    def setUp(self):
        self.trie1 = Trie()
        self.trie1.insert("Banana")
        self.trie1.insert("BungyJump")

    def tearDown(self):
        #self.trie1.dispose()
        self.trie1 = None

    def test_search(self):
        result = self.trie1.search("Hello")
        self.assertEqual(result, False)
        result = self.trie1.search("Banana")
        self.assertEqual(result, True)

    def test_insert(self):
        self.trie1.insert("Bunty")
        result = self.trie1.search("Bunty")
        self.assertEqual(result, True)
        result = self.trie1.search("Bunty")
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()