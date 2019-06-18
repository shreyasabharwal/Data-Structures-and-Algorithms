from TreesBasicOperations import Node


def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    depth = 1
    if root is None:
        return 0
    if root.left == None and root.right == None:
        return 1
    depth += max(maxDepth(root.left), maxDepth(root.right))
    return depth


if __name__ == "__main__":
    new_node = Node(3)
    new_node.left = Node(9)
    new_node.right = Node(20)
    new_node.right.left = Node(15)
    new_node.right.right = Node(7)
    print(maxDepth(new_node))
