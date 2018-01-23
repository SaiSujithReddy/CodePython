class BST:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

def isEmpty(root):
    return root.data == []

def insert(root,node):
    if root is None:
        root = node
    elif root.data > node.data:
        if root.left is None:
            root.left= node
        else:
            insert(root.left,node)
    elif root.data < node.data:
        if root.right is None:
            root.right= node
        else:
            insert(root.right,node)

def print_inorder(root):
    if not root:
        return
    print_inorder(root.left)
    if root is not None:
        print(root.data)
    print_inorder(root.right)


r = BST(3)
insert(r,BST(4))
insert(r,BST(2))
insert(r,BST(5))
insert(r,BST(1))
print_inorder(r)