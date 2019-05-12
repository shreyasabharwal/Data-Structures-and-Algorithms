""" 2.4 Partition:
    Write code to partition a linked list around a value x, such that all nodes less than x come
    before all nodes greater than or equal to x. lf x is contained within the list, the values of x only need
    to be after the elements less than x (see below). The partition element x can appear anywhere in the
    "right partition"; it does not need to appear between the left and right partitions.
    EXAMPLE
    Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5)
    Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8"""


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

    def printElements(self):
        "Print elements of the linked list"
        current = self.head
        while current != None:
            print(current.data, end='\t')
            current = current.next

    def partition(self, x):
        current = self.head
        beforeHead = None
        beforeTail = None
        afterHead = None
        afterTail = None
        while current != None:
            if current.data < x:
                if beforeHead == None:
                    beforeHead = current
                    beforeTail = beforeHead
                    current = current.next
                else:
                    beforeTail.next = current
                    beforeTail = current
                    current = current.next
            else:
                if afterHead == None:
                    afterHead = current
                    afterTail = afterHead
                    current = current.next
                else:
                    afterTail.next = current
                    afterTail = current
                    current = current.next

        if beforeHead == None:
            return afterHead

        beforeTail.next = afterHead
        return beforeHead


if __name__ == "__main__":
    # Creating nodes
    node1 = Node(3)
    node2 = Node(5)
    node3 = Node(89)
    node4 = Node(17)
    node5 = Node(13)
    node6 = Node(215)
    node7 = Node(17)
    node8 = Node(23)
    node9 = Node(825)
    node10 = Node(27)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9
    node9.next = node10
    # Creating Linkedlist
    ll = LinkedList(node1)
    ll.printElements()

    ll.partition(23)
    print("##")
    ll.printElements()
