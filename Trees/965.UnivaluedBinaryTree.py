'''
965. Univalued Binary Tree

A binary tree is univalued if every node in the tree has the same value.
Return true if and only if the given tree is univalued.

Example 1:
Input: [1,1,1,1,1,null,1]
Output: true

Example 2:
Input: [2,2,2,5,2]
Output: false
 
Note:
The number of nodes in the given tree will be in the range [1, 100].
Each node's value will be an integer in the range [0, 99].
'''


class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isTreeUnival(root, root.val)

    def isTreeUnival(self, node, value):
        # base condition
        if not node:
            return True
        if node.val != value:
            return False
        return node.val == value and self.isTreeUnival(node.left, value) and self.isTreeUnival(node.right, value)
