class Node:
    def __init__(self,val):
        self.data = val
        self.rightChild = None
        self.leftChild = None

def binary_insert(root,node):
    if not root:
        root = node
    elif node.data > root.data:
        if root.rightChild == None:
            root.rightChild = node
        else:
            binary_insert(root.rightChild,node)
    elif node.data < root.data:
        if root.leftChild == None:
            root.leftChild = node
        else:
            binary_insert(root.leftChild,node)

def print_inorder(root):
    # left , root , right
    if not root:
        return
    print_inorder(root.leftChild)
    print(root.data)
    print_inorder(root.rightChild)

def print_preorder(root):
    # root, left, right
    if not root:
        return
    print(root.data)
    print_preorder(root.leftChild)
    print_preorder(root.rightChild)

def print_postorder(root):
    # left, right, root
    if not root:
        return
    print_preorder(root.leftChild)
    print_preorder(root.rightChild)
    print(root.data)

def min_depth_of_tree(root):
    if (root == None):
        return 0
    else:
        if (root.leftChild and root.rightChild ):
            return min([min_depth_of_tree(root.leftChild), min_depth_of_tree(root.rightChild)]) + 1
        elif (root.leftChild ):
            return min_depth_of_tree(root.leftChild) + 1
        elif root.rightChild:
            return min_depth_of_tree(root.rightChild) + 1
        else:
            return 1

def max_depth_of_tree(root):
    if (root == None):
        return 0
    else:
        if (root.leftChild and root.rightChild ):
            return max([max_depth_of_tree(root.leftChild), max_depth_of_tree(root.rightChild)]) + 1
        elif (root.leftChild ):
            return max_depth_of_tree(root.leftChild) + 1
        elif root.rightChild:
            return max_depth_of_tree(root.rightChild) + 1
        else:
            return 1

root = Node(7)
binary_insert(root,Node(18))
binary_insert(root,Node(8))
binary_insert(root,Node(19))
binary_insert(root,Node(6))
binary_insert(root,Node(4))
binary_insert(root,Node(2))
binary_insert(root,Node(1))

print("Inorder print of the tree is as follows")
print_inorder(root)
print("Pre-order print of the tree is as follows")
print_preorder(root)
print("Post-order print of the tree is as follows")
print_postorder(root)
print("\nMin depth of tree")
print(min_depth_of_tree(root))
print("\nMax depth of tree")
print(max_depth_of_tree(root))