""" 2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
    FOLLOW UP
    How would you solve this problem if a temporary buffer is not allowed?"""


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

    def removeDupsBuffer(self):
        "Remove duplicates with temporary buffer"
        track_dict = {}
        current = self.head
        previous = self.head
        while current.next != None:
            if current.data not in track_dict:
                track_dict[current.data] = 1
                previous = current
                current = current.next
            else:
                previous.next = current.next
                current = current.next
    #Complexity = O(n)

    def removeDuplicatesWOBuffer(self):
        "Remove Duplicates without buffer"
        current = self.head
        while current.next != None:
            runner = current
            while runner.next != None:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next
    # Time Complexity = O(n^2), space complexity:O(1)


if __name__ == "__main__":
    # Creating nodes
    node1 = Node("23")
    node2 = Node("5")
    node3 = Node("215")
    node4 = Node("7")
    node5 = Node("13")
    node6 = Node("215")
    node7 = Node("17")
    node8 = Node("23")
    node9 = Node("215")
    node10 = Node("97")
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

    ll.removeDuplicatesWOBuffer()
    print("\nDuplicates Removed:")
    ll.printElements()
