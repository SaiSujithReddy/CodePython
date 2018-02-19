class Node:
    def __init__(self,data):
        self.val = data
        self.leftChild = None
        self.rightChild = None


def bst_insert(root,data):
    if root is None:
        root = Node(data)
    else:
        if root.val > data:
            if root.leftChild:
                bst_insert(root.leftChild,data)
            else:
                root.leftChild = Node(data)
        else:
            if root.rightChild:
                bst_insert(root.rightChild,data)
            else:
                root.rightChild = Node(data)


def print_inorder(root):
    if root.leftChild:
        print_inorder(root.leftChild)
    print(root.val)
    if root.rightChild:
        print_inorder(root.rightChild)

#Queue based approach
def printLevelOrder_using_queue(root):
    print("inside quque")
    # Base Case
    if root is None:
        return

    # Create an empty queue for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(root)

    while (len(queue) > 0):
        # Print front of queue and remove it from queue
        print(queue[0].val)
        node = queue.pop(0)

        # Enqueue left child
        if node.leftChild is not None:
            queue.append(node.leftChild)

        # Enqueue right child
        if node.rightChild is not None:
            queue.append(node.rightChild)



node = Node(5)
bst_insert(node,4)
bst_insert(node,6)
bst_insert(node,7)
bst_insert(node,8)
bst_insert(node,3)
print_inorder(node)
printLevelOrder_using_queue(node)
'''
     5
    / \
   4   6
  /     \
 3      7
         \
         8
'''