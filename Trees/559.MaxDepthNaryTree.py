'''559. Maximum Depth of N-ary Tree

Given a n-ary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.'''


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        depth = 1
        return self.getDepth(root, depth)

    def getDepth(self, node, depth):
        if not node:
            return 0
        if not node.children:
            return 1
        temp = 0
        for child in node.children:
            temp = max(temp, self.getDepth(child, depth))
        depth += temp
        return depth
