'''Delete Middle Node: Implement an algorithm to delete a node in the middle (Le., any node but
the fi rst and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
Input: the node c from the linked list a - >b- >c - >d - >e- >f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f'''


'''
In this problem, you are not given access to the head of the linked list. You only have access to that node.
The solution is simply to copy the data from the next node over to the current node, and then to delete the
next node.
'''
from NodeInsertion import Node, LinkedList


def deleteNode(node):
    "Delete middle node"
    if node is None or node.next is None:
        return False
    nextnode = node.next
    node.data = nextnode.data
    node.next = nextnode.next
    return True


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

    print("\n", deleteNode(node5))
