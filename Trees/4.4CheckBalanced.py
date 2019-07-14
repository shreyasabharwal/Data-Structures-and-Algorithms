'''4.4 Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
    this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
    node never differ by more than one.
'''

import math
from TreesBasicOperations import Node


def checkHeight(root):
    # base case
    if root is None:
        return -1
    leftHeight = checkHeight(root.left)
    rightHeight = checkHeight(root.right)

    heightDiff = abs(leftHeight-rightHeight)

    if heightDiff > 1:
        return math.inf
    else:
        return max(leftHeight, rightHeight)+1


def checkBalanced(root):
    if checkHeight(root) != math.inf:
        return True
    else:
        return False


if __name__ == "__main__":
    # check for balanced tree
    new_node = Node(40)
    new_node.insert(60)
    new_node.insert(10)
    new_node.insert(5)
    new_node.insert(15)
    new_node.insert(45)
    print(checkBalanced(new_node))

    # check for unbalanced tree
    node1 = Node(1)
    node1.left = Node(2)
    node1.left.left = Node(3)
    node1.left.left.left = Node(4)
    node1.right = Node(2)
    node1.right.right = Node(3)
    node1.right.right.right = Node(4)
    print(checkBalanced(node1))
