'''617. Merge Two Binary Trees

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
 

Note: The merging process must start from the root nodes of both trees.'''

from TreesBasicOperations import Node as TreeNode


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        elif not t2:
            return t1
        elif not t1:
            return t2

        newNode = TreeNode(t1.data+t2.data)
        newNode.left = self.mergeTrees(t1.left, t2.left)
        newNode.right = self.mergeTrees(t1.right, t2.right)

        return newNode


if __name__ == "__main__":
    new_node1 = TreeNode(1)
    new_node1.left = TreeNode(2)
    new_node1.left.left = TreeNode(3)
    new_node2 = TreeNode(1)
    new_node2.right = TreeNode(2)
    new_node2.right.right = TreeNode(3)
    obj = Solution()
    node = obj.mergeTrees(new_node1, new_node2)
    node.printInOrder()
