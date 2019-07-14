'''2.7 Intersection: Given two(singly) linked lists, determine if the two lists intersect. Return the
        intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
        kth node of the first linked list is the exact same node(by reference) as the jth node of the second
        linked list, then they are intersecting.
'''


'''
Refer 160.IntersectionOfLinkedLists.py
'''
from NodeInsertion import Node, LinkedList


def findTailAndSize(headNode):
    'Return the tail node and size of linked list'
    if not headNode:
        return None
    tail = headNode
    count = 0
    while tail.next:
        tail = tail.next
        count += 1
    return tail, count


def increment(headNode, count):
    'Increment the pointer by given count'
    current = headNode
    while count != 0 and current != None:
        current = current.next
        count -= 1
    return current


def findIntersection(l1headNode, l2headNode):
    'Find intersection of 2 linked lists'
    l1tail, l1size = findTailAndSize(l1headNode)
    l2tail, l2size = findTailAndSize(l2headNode)

    if l1tail != l2tail:
        return None

    diffLen = abs(l1size-l2size)
    if diffLen != 0:
        longer = increment(
            l1headNode, diffLen) if l1size > l2size else increment(l2headNode, diffLen)
        shorter = l2headNode if l1size > l2size else l1headNode

    while shorter and longer:
        if shorter == longer:
            return shorter
        shorter = shorter.next
        longer = longer.next
    return None


if __name__ == "__main__":
    # Creating nodes
    node1 = Node("3")
    node2 = Node("5")
    node3 = Node("89")
    node4 = Node("17")
    node5 = Node("13")
    node6 = Node("215")
    node7 = Node("17")
    node8 = Node("23")
    node9 = Node("825")
    node10 = Node("27")

    node11 = Node("3")
    node12 = Node("5")

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9
    node9.next = node10

    node11.next = node12
    node12.next = node6
    # Creating Linkedlist
    l1 = LinkedList(node1)
    l1.printElements()

    l2 = LinkedList(node11)
    print('\n')
    l2.printElements()

    node = findIntersection(l1.head, l2.head)
    print('\n'+node.data)
