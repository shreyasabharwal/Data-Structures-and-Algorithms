'''104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.'''


from TreesBasicOperations import Node


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 1
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        depth += max(self.maxDepth(root.left), self.maxDepth(root.right))
        return depth


if __name__ == "__main__":
    new_node = Node(3)
    new_node.left = Node(9)
    new_node.right = Node(20)
    new_node.right.left = Node(15)
    new_node.right.right = Node(7)
    obj = Solution()
    print(obj.maxDepth(new_node))
