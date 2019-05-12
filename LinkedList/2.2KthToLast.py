# 2.2 Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

'''Use two pointers k data notes apart. Then keep incrementing both till the fast pointer moves to the last element. When one reaches the end, the other is at kth to last position '''


class Node:
    # constructor

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def printElements(self):
        "Print elements of the linked list"
        current = self.head
        while current != None:
            print(current.data, end='\t')
            current = current.next

    def kthtolast(self, k):
        p1 = self.head
        p2 = self.head
        count = 0
        while count < k:
            if p1 is None:
                return None
            p1 = p1.next
            count += 1

        while p1 != None:
            p1 = p1.next
            p2 = p2.next

        return p2.data


if __name__ == "__main__":
    # Creating nodes
    node1 = Node("3")
    node2 = Node("5")
    node3 = Node("7")
    node4 = Node("13")
    node5 = Node("25")
    node6 = Node("37")
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    # Creating Linkedlist
    ll = LinkedList(node1)
    ll.printElements()

    print("\n Kth to last element: ", ll.kthtolast(4))
