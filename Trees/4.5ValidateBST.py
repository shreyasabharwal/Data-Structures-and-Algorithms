'''4.5 Validate BST: Implement a function to check if a binary tree is a binary search tree.
'''

import math
from TreesBasicOperations import Node


def checkBST(root):
    return isBST(root, -math.inf, math.inf)


def isBST(root, min, max):
    if root is None:
        return True
    # base condition
    if root.data < min or root.data > max:
        return False

    return (isBST(root.left, min, root.data-1) and isBST(root.right, root.data+1, max))


if __name__ == "__main__":
    new_node = Node(40)
    new_node.insert(60)
    new_node.insert(10)
    new_node.insert(5)
    new_node.insert(15)
    new_node.insert(45)
    new_node.insert(3)
    print(checkBST(new_node))

    node1 = Node(100)
    node1.right = Node(60)
    node1.left = Node(100)
    print(checkBST(node1))
