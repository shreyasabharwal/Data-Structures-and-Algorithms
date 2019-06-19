'''589. N-ary Tree Preorder Traversal

Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:
Return its preorder traversal as: [1,3,5,6,2,4].

Note:
Recursive solution is trivial, could you do it iteratively?'''

from collections import deque

# Definition for a Node.


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return None
        l_nodes = []
        return self.getPreOrder(root, l_nodes)

    def getPreOrder(self, node, l_nodes):
        l_nodes.append(node.val)
        for child in node.children:
            self.getPreOrder(child, l_nodes)
        return l_nodes

    # Iterative
    def preorderIter(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return None
        l_nodes = []
        que = deque()
        que.append(root)
        while(que):
            node = que.popleft()
            l_nodes.append(node.val)
            for child in node.children[::-1]:
                que.appendleft(child)
        return l_nodes
