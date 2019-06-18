'''101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Note:
Bonus points if you could solve it both recursively and iteratively.'''

#from queue import Queue
from LinkedListImplementationofQueue import Queue


class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.next = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return t1.data == t2.data and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)

    # def isSymmetricIterative(self, root):
    #     if root is None:
    #         return True
    #     myqueue = Queue()
    #     myqueue.put(root.left)
    #     myqueue.put(root.right)
    #     while(not myqueue.isEmpty()):
    #         node1 = myqueue.get()
    #         node2 = myqueue.get()
    #         if node1 is None and node2 is None:
    #             continue
    #         if node1 is None or node2 is None:
    #             return False
    #         if node1.data != node2.data:
    #             return False
    #         if node1 and node2:
    #             myqueue.put(node1.left)
    #             myqueue.put(node2.right)
    #             myqueue.put(node1.right)
    #             myqueue.put(node2.left)

    #     return True


if __name__ == "__main__":
    new_node = TreeNode(1)
    new_node.left = TreeNode(2)
    new_node.right = TreeNode(2)
    new_node.left.left = TreeNode(3)
    new_node.left.left.left = TreeNode(5)
    new_node.left.right = TreeNode(4)
    new_node.right.left = TreeNode(4)
    new_node.right.right = TreeNode(3)
    new_node.right.right.right = TreeNode(5)
    obj = Solution()
    # print(obj.isSymmetric(new_node))
    print(obj.isSymmetric(new_node))
