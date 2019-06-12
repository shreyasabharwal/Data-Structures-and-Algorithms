'''4.6 Successor: Write an algorithm to find the "next" node(i.e., in-order successor) of a given node in a
    binary search tree. You may assume that each node has a link to its parent.
'''
'''
Approach: For any node, left most child of right subtree will be the next in-order successor.
If node.right is null and node is the left child of the parent, the next successor will be the parent.
If node.right is null and node is the right child of the parent, the parent has already been traversed. We need to navigate to the parent till the node is the right child of the parent.
'''


class Node:
    def __init__(self, data=None, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent


def successor(node):
    if node is None:
        return
    if node.right:
        return leftMostChild(node.right)
    else:
        q = node
        x = q.parent
    # while node is the right child of node.parent
    while(x is not None and x.right == q):
        q = x
        x = x.parent
    return x


def leftMostChild(node):
    if node.left is None:
        return node
    while(node.left != None):
        node = node.left
    return node


def createTree():
    root = Node(40)
    node1 = Node(10, parent=root)
    node2 = Node(60, parent=root)
    node3 = Node(5, parent=node1)
    node4 = Node(15, parent=node1)
    node5 = Node(45, parent=node2)
    node6 = Node(3, parent=node3)
    node7 = Node(4, parent=node3)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node3.left = node6
    node3.right = node7

    return root


if __name__ == "__main__":
    root = createTree()
    suc = successor(root.left.right)
    if suc:
        print(suc.data)
    else:
        print(None)
