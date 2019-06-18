'''4.3 List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth(e.g., if you have a tree with depth D, you 'll have D linked lists).
'''

from TreesBasicOperations import Node as TreeNode


class LinkedListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insertAtEnd(self, data):
        "Insert element at the end"
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = new_node

    def printElements(self):
        "Print elements of the linked list"
        current = self.head
        while current != None:
            print(current.data, end='\t')
            current = current.next


def getListOfDepths(root):
    list_ll = []
    listOfDepths(root, list_ll, level=0)
    return list_ll


def listOfDepths(root, list_ll, level):
    '''Create a list of linkedlist of each level'''
    if root is None:
        return

    # if linkedlist of this level doesn't exist in the list, create a new linkedlist and add it to the list.
    if len(list_ll) == level:
        ll = LinkedList()
        list_ll.append(ll)
    ll = list_ll[level]
    ll.insertAtEnd(root.data)

    listOfDepths(root.left, list_ll, level+1)
    listOfDepths(root.right, list_ll, level+1)


if __name__ == "__main__":
    new_node = TreeNode(40)
    new_node.insert(60)
    new_node.insert(10)
    new_node.insert(5)
    new_node.insert(15)
    new_node.insert(45)
    list_linkedlist = getListOfDepths(new_node)
    for ll in list_linkedlist:
        ll.printElements()
        print("##")
