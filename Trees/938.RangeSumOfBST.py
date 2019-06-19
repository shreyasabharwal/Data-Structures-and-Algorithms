'''938. Range Sum of BST

Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Example 1:
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
 

Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.'''

from TreesBasicOperations import Node


class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        sumNodes = 0
        if not root:
            return 0
        if root.val < L:
            return self.rangeSumBST(root.right, L, R)
        if root.val > R:
            return self.rangeSumBST(root.left, L, R)
        sumNodes += root.val
        sumNodes += self.rangeSumBST(root.left, L, R)
        sumNodes += self.rangeSumBST(root.right, L, R)
        return sumNodes


if __name__ == "__main__":
    new_node = Node(10)
    new_node.left = Node(5)
    new_node.right = Node(15)
    new_node.left.left = Node(3)
    new_node.left.right = Node(7)
    new_node.right.right = Node(18)
    obj = Solution()
    L, R = 7, 15
    print(obj.rangeSumBST(new_node, L, R))
