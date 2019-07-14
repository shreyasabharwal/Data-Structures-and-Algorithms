'''2.8 Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
        beginning of the loop.
        DEFINITION
        Circular linked list: A(corrupt) linked list in which a node's next pointer points to an earlier node, so
        as to make a loop in the linked list.
        EXAMPLE
        Input: A -> B -> C - > D -> E -> C[the same C as earlier)
        Output: C
'''
'''
https://www.youtube.com/watch?v=-YiQZi3mLq0&feature=youtu.be

N = Total nodes moved by fast pointer
2N = Total nodes moved by slow pointer
D = nodes before start of the loop
k = nodes from start of the loop y intersection point 
C= length of cycle
i, j = number of iterations made by fast and slow pointer respectively.
N = D+k+C(i)
2N = D+k+C(j)

2D+2k+2C(i) = D+k+C(j)
D+k = C(j-2i)
D = C(j-2i)-k

This implies after covering (j-2i) cycles we are going to fall short by k nodes from start of the loop
'''
from NodeInsertion import Node, LinkedList


def detectLoop(headNode):
    "Return the starting node of the loop"
    slow = headNode
    fast = headNode
    # keep 2 pointers - slow and fast. slow moves one step, fast moves 2 steps
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # meeting point
        if slow == fast:
            break
    # check for no loop
    if not fast or fast.next:
        return None
    # head and meeting point are at k steps from loop start
    slow = headNode
    while(slow != fast):
        slow = slow.next
        fast = fast.next

    return fast


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
    node11 = Node("7")
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node9
    node9.next = node10
    node10.next = node11
    node11.next = node4

    # Creating Linkedlist
    ll = LinkedList(node1)
    node = detectLoop(ll.head)
    print(node.data)
