'''3.2 Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.'''


class Node:
    # constructor
    def __init__(self, data=None):
        self.data = data
        self.next = None


class NodeWithMin(Node):
    def __init__(self, data=None, min=None):
        self.data = data
        self.min = min


class Stack(object):
    def __init__(self, data=None):
        self.top = None
        if data:
            for d in data:
                # print('##super init##')
                self.push(d)

    def push(self, node):
        "Push/add an element"
        #node = Node(data)
        # print('##super push##')
        node.next = self.top
        self.top = node

    def pop(self):
        "Pop/remove an element"
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def isEmpty(self):
        return self.top == None

    def peek(self):
        if self.top is None:
            return None
        return self.top

    def length(self):
        "Print number of elements"
        current = self.top
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def printElements(self):
        "Print elements of the linked list"
        current = self.top
        while current != None:
            print(current.data, end='\t')
            current = current.next


class stackWithMin(Stack):
    def push(self, data):
        # print('###### min push ######')
        new_min = data if data < self.min() else self.min()
        node = NodeWithMin(data, new_min)
        super().push(node)

    def min(self):
        if self.isEmpty():
            return float('inf')
        return super().peek().min


if __name__ == "__main__":
    # Creating Stack
    ll = stackWithMin(data=[190, 87, 98, 45, 90, 9, 30])
    print('Minimum element: ', ll.min())
    # ll.printElements()
