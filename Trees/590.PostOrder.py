'''590. N-ary Tree Postorder Traversal

Given an n-ary tree, return the postorder traversal of its nodes' values.

For example, given a 3-ary tree:

Return its postorder traversal as: [5,6,3,2,4,1].

 
Note:

Recursive solution is trivial, could you do it iteratively?'''

from collections import deque


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        l_nodes = []
        self.getPostOrder(root, l_nodes)
        return l_nodes

    def getPostOrder(self, root, l_nodes):
        if not root:
            return None
        for child in root.children:
            self.getPostOrder(child, l_nodes)
        l_nodes.append(root.val)

    # iterative
    def postorderIter(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return None
        stack, res = [], deque()
        stack.append(root)
        while stack:
            n1 = stack.pop()
            res.appendleft(n1.val)
            for child in n1.children:
                stack.append(child)
        return res
