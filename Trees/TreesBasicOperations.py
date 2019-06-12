'''
Binary Search Tree basic operations - insertion, traversal, findElements
'''


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        '''insert a new node'''
        if self is None:
            self = Node(data)
        if data < self.data:  # left node
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = Node(data)

    def contains(self, data):
        '''check if a node exists with data'''
        if self.data == data:
            return True

        elif data < self.data:
            if self.left:
                return self.left.contains(data)
            else:
                return False

        else:
            if self.right:
                return self.right.contains(data)
            else:
                return False

    def printInOrder(self):
        '''print elements - in-order traversal'''
        if self.left:
            self.left.printInOrder()
        print(self.data)
        if self.right:
            self.right.printInOrder()

    def printPreOrder(self):
        '''print elements - pre-order traversal'''
        print(self.data)
        if self.left:
            self.left.printInOrder()
        if self.right:
            self.right.printInOrder()

    def printPostOrder(self):
        '''print elements - post-order traversal'''
        if self.left:
            self.left.printInOrder()
        if self.right:
            self.right.printInOrder()
        print(self.data)


if __name__ == "__main__":
    new_node = Node(40)
    new_node.insert(60)
    new_node.insert(10)
    new_node.insert(5)
    new_node.insert(15)
    new_node.insert(45)
    new_node.insert(3)
    contains = new_node.contains(10)
    print('Does 10 already exist: ', contains)
    new_node.printInOrder()
