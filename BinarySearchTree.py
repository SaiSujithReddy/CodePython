class Node:
    def __init__(self,val):
        self.data = val
        self.leftChild = None
        self.rightChild = None

def binary_insert(root,node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.leftChild is None:
                root.leftChild = node
            else:
                binary_insert(root.leftChild,node)
        else:
            if root.rightChild is None:
                root.rightChild = node
            else:
                binary_insert(root.rightChild,node)

def in_order(root):
    if not root:
        return
    in_order(root.leftChild)
    print root.data
    in_order(root.rightChild)

r = Node(3)
binary_insert(r, Node(7))
binary_insert(r, Node(1))
binary_insert(r, Node(5))

in_order(3)