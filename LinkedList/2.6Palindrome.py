'''2.6 Palindrome: Implement a function to check if a linked list is a palindrome.
'''

# Node Insertion


class Node:
    # constructor
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def length(self):
        "Print number of elements"
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def printElements(self):
        "Print elements of the linked list"
        current = self.head
        while current != None:
            print(current.data, end='\t')
            current = current.next


def printElements(current):
    "Print elements of the linked list"
    while current != None:
        print(current.data, end='\t')
        current = current.next


def reverse(node):
    head = None
    while(node != None):
        newNode = Node(node.data)
        newNode.next = head
        head = newNode
        node = node.next
    return head


def isEqual(nodel1, nodel2):
    while nodel1 != None and nodel2 != None:
        if nodel1.data != nodel2.data:
            return False
        nodel1 = nodel1.next
        nodel2 = nodel2.next
    return True


def isPalindrome(headNode):
    reversed = reverse(headNode)
    return isEqual(headNode, reversed)


if __name__ == "__main__":
    # Creating nodes
    node1 = Node("3")
    node2 = Node("5")
    node3 = Node("8")
    node4 = Node("9")
    node5 = Node("8")
    node6 = Node("5")
    node7 = Node("3")

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7

    # Creating Linkedlist
    ll = LinkedList(node1)
    ll.printElements()

    print('\n')
    print(isPalindrome(ll.head))
