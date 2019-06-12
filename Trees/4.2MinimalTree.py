'''4.2 Minimal Tree: Given a sorted(increasing order) array with unique integer elements, write an
    algorithm to create a binary search tree with minimal height.
'''

'''
Approach: To create a tree of minimal height, we need to match the number of nodes in the left subtree to the number
of nodes in the right subtree as much as possible. The middle of each subsection of the array
becomes the root of the node. The left half of the array will become our left subtree, and the right half of
the array will become the right subtree.'''


class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def printInOrder(self):
        '''print elements - in-order traversal'''
        if self.left:
            self.left.printInOrder()
        print(self.data)
        if self.right:
            self.right.printInOrder()


def minimalTree(arr):
    return createMinimalTree(arr, 0, len(arr)-1)


def createMinimalTree(arr, start, end):
    if start > end:
        return
    mid = (start+end)//2
    # the middle element should be the root for the tree to be balanced.
    root = TreeNode(arr[mid])
    root.left = createMinimalTree(arr, start, mid-1)
    root.right = createMinimalTree(arr, mid+1, end)
    return root


if __name__ == "__main__":
    arr = [2, 5, 7, 9, 10, 45, 70]
    root = minimalTree(arr)
    # in-order traversal should list the elements in ascending order
    root.printInOrder()
