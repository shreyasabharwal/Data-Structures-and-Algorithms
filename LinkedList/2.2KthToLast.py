# 2.2 Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

'''Use two pointers k data notes apart. Then keep incrementing both till the fast pointer moves to the last element. When one reaches the end, the other is at kth to last position '''

from NodeInsertion import Node, LinkedList


def kthtolast(headNode, k):
    p1 = headNode.head
    p2 = headNode.head
    count = 0
    while count < k:
        if not p1:
            return
        p1 = p1.next
        count += 1

    while p1:
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

    print("\n Kth to last element: ", kthtolast(ll, 4))
