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

    def insertAtBeginning(self, data):
        "Insert node at the beginning"
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        return

    def insertAtEnd(self, data):
        "Insert element at the end"
        new_node = Node(data)
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

    def insertAtPos(self, pos, data):
        if pos > self.listLength() or pos < 0:
            return None
        elif pos == 0:
            self.insertAtBeginning(data)
        elif pos == self.listLength():
            self.insertAtEnd(data)
        else:
            current = self.head
            new_node = Node(data)
            count = 0
            while count < pos-2:
                count += 1
                current = current.next
            new_node.next = current.next
            current.next = new_node


if __name__ == "__main__":
    # Creating nodes
    node1 = Node("3")
    node2 = Node("5")
    node3 = Node("7")
    node1.next = node2
    node2.next = node3
    # Creating Linkedlist
    ll = LinkedList(node1)
    ll.printElements()

    # Inserting element at the beginning
    ll.insertAtBeginning("8")
    print("\nInterting element at the beginning; Length of LinkedList: ",
          ll.listLength())
    ll.printElements()

    # Interting element at the end
    ll.insertAtEnd("10")
    print("\nInterting element at the end; Length of LinkedList: ", ll.listLength())
    ll.printElements()

    # Inserting element at a specific position
    ll.insertAtPos(2, "20")
    print("\nInserting element at a specific position; Length of LinkedList: ", ll.listLength())
    ll.printElements()
