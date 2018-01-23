class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

def binary_insert(root,node):
    if root is None:
        print("root is None, Node value is ", node)
        root = node
    else:
        #print(root.data)
        #print(node.data)
        if root.data < node.data:
            print("Inserting right")
            if root.right is None:
                root.right = node
            else :
                binary_insert(root.right,node)
        else:
            print("Inserting left")
            if root.left is None:
                root.left = node
            else :
                binary_insert(root.left,node)

def binary_print_inorder(root):
    if not root:
        return
    binary_print_inorder(root.left)
    print(root.data)
    binary_print_inorder(root.right)

def binary_print_inorder(root):
    if not root:
        return
    binary_print_inorder(root.left)
    print(root.data)
    binary_print_inorder(root.right)


def binary_print_preorder(root):
    if not root:
        return
    print(root.data)
    binary_print_inorder(root.left)
    binary_print_inorder(root.right)

#calculate height of tree
def height(root):
    if not root:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)

        if left_height > right_height:
            return left_height+1
        else:
            return right_height+1



# Function to  print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printGivenLevel(root, i)


# Print nodes at a given level
def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(" {}".format(root.data))
    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)

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
        print(queue[0].data)
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)


r = Node(3)
binary_insert(r, Node(7))
binary_insert(r, Node(1))
binary_insert(r, Node(5))
binary_insert(r, Node(2))
binary_insert(r, Node(4))
binary_insert(r, Node(8))
binary_insert(r, Node(6))

#binary_print_inorder(r)
print("")
#binary_print_preorder(r)

#printLevelOrder(r)
printLevelOrder_using_queue(r)