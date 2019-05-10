# Node Insertion


class Node:
    # constructor

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def listLength(self):
        "Print number of elements"
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def deleteFirstNode(self):
        "Delete node at the beginning"
        if self.head is None:
            return
        else:
            current = self.head
            self.head = current.next
            current.next = None
        return

    def deleteLastNode(self):
        "Delete last element"
        if self.head is None:
            return
        else:
            previous = self.head
            current = self.head
            while (current.next != None):
                previous = current
                current = current.next
            previous.next = None

    def printElements(self):
        "Print elements of the linked list"
        current = self.head
        while current != None:
            print(current.data, end='\t')
            current = current.next

    def deleteAtPos(self, pos):
        "Delete node at a specific position"
        if pos > self.listLength() or pos < 0:
            return None
        elif pos == 0:
            self.deleteFirstNode()
        elif pos == self.listLength():
            self.deleteLastNode()
        else:
            current = self.head
            count = 0
            while count < pos-2:
                count += 1
                current = current.next
            current.next = current.next.next

    def deleteNode(self, val):
        "Delete node with a specific value"
        current = self.head
        previous = self.head
        while (current.next != None):
            if current.data == val:
                previous.next = current.next
                return
            previous = current
            current = current.next


if __name__ == "__main__":
    # Creating nodes
    node1 = Node("3")
    node2 = Node("5")
    node3 = Node("7")
    node4 = Node("16")
    node5 = Node("1")
    node6 = Node("50")
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    # Creating Linkedlist
    ll = LinkedList(node1)
    ll.printElements()

    # Delete first element
    ll.deleteFirstNode()
    print("\nDeleting first element; Length of LinkedList: ",
          ll.listLength())
    ll.printElements()

    # Deleting last element
    ll.deleteLastNode()
    print("\nDeleting last element; Length of LinkedList: ", ll.listLength())
    ll.printElements()

    # Deleting element from a specific position
    ll.deleteAtPos(2)
    print("\nDeleting element from a specific position; Length of LinkedList: ", ll.listLength())
    ll.printElements()

    ll.deleteNode("16")
    print("\nDeleting value; Length of LinkedList: ", ll.listLength())
    ll.printElements()
