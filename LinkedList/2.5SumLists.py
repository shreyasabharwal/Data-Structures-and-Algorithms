''' 2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single
        digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a
        function that adds the two numbers and returns the sum as a linked list.
        EXAMPLE
        Input: (7-> 1 -> 6) + (5 -> 9 -> 2) .Thatis, 617 + 295.
        Output: 2 - > 1 - > 9. That is, 912.

        FOLLOW UP
        Suppose the digits are stored in forward order. Repeat the above problem.
        Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).Thatis, 617 + 295.
        Output: 9 - > 1 - > 2. That is, 912.
'''


class Node:
    # constructor
    def __init__(self, data=None):
        self.data = data
        self.next = None


def length(current):
    "Return length of linked list"
    count = 0
    while current != None:
        count += 1
        current = current.next
    return count


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def printElements(self):
        "Print elements of the linked list"
        current = self.head
        while current != None:
            print(current.data, end='\t')
            current = current.next


def sumList(l1, l2, carry):
    'Sum the linked list with digits stored in reverse order'
    # Base case
    if l1 is None and l2 is None and carry == 0:
        return None
    value = carry
    if l1 != None:
        value += l1.data
    if l2 != None:
        value += l2.data
    # calculate carry over for next node
    carry = value//10
    # calculate data of the node
    value = value % 10
    sumNode = Node(value)
    if l1 != None and l2 != None:
        nextNode = sumList(l1.next if l1 != None else None,
                           l2.next if l2 != None else None, carry)
        sumNode.next = nextNode
    return sumNode


def padZeros(ll, num_of_zeros):
    'Pad linked list with number of zeros specified'
    for i in range(num_of_zeros):
        zeroNode = Node(0)
        zeroNode.next = ll
        ll = zeroNode
        return ll


def callRecSumList(l1, l2, carry=0):
    sumNode = Node()
    if l1.next != None and l2.next != None:
        sumNode.next, carry = callRecSumList(l1.next, l2.next)
    value = carry
    if l1 != None:
        value += l1.data
    if l2 != None:
        value += l2.data
    carry = value//10
    #print(value, ',', carry, '\n')
    value = value % 10
    sumNode.data = value
    return sumNode, carry


def sumListFwd(l1, l2):
    'Sum the linked list with digits stored in forward order'
    # if lengths are not equal, pad the smaller one with zeros
    num_of_zeros = length(l1)-length(l2)
    if num_of_zeros > 0:
        # pad l2 with zeros
        l2 = padZeros(l2, abs(num_of_zeros))
    elif num_of_zeros < 0:
        # pad l1 with zeros
        l1 = padZeros(l1, abs(num_of_zeros))
    node, carry = callRecSumList(l1, l2, carry=0)
    node.data += carry
    return node


if __name__ == "__main__":
    # Creating nodes
    node1 = Node(7)
    node2 = Node(1)
    node3 = Node(6)

    node4 = Node(5)
    node5 = Node(9)
    node6 = Node(2)
    node7 = Node(1)

    node1.next = node2
    node2.next = node3

    node4.next = node5
    node5.next = node6
    node6.next = node7
    # Creating 1st Linkedlist
    l1 = LinkedList(node1)
    # Creating 2nd Linkedlist
    l2 = LinkedList(node4)

    print("Digits store in reverse order")
    l1.printElements()
    print('+')
    l2.printElements()
    sumNode = sumList(l1.head, l2.head, 0)
    ll = LinkedList(sumNode)
    print('=')
    ll.printElements()

    print("\nDigits store in forward order")
    l1.printElements()
    print('+')
    l2.printElements()
    sumNode1 = sumListFwd(l1.head, l2.head)
    ll1 = LinkedList(sumNode1)
    print('=')
    ll1.printElements()
