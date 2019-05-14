'''3.2 Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
'''


'''Implementing this using stacks'''


class Node:
    # constructor
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack(object):
    def __init__(self, data=None):
        self.top = None
        if data:
            for d in data:
                self.push(d)

    def push(self, data):
        "Push/add an element"
        node = Node(data)
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
        return self.top.data

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
    smin = Stack()

    def push(self, data):
        if data <= self.min():
            self.smin.push(data)
        super().push(data)

    def pop(self, data):
        val = super().pop()
        if val == self.min():
            self.smin.pop()
        return val

    def min(self):
        if self.isEmpty():
            return float('inf')
        return self.smin.peek()


if __name__ == "__main__":
    # Creating Stack
    ll = stackWithMin(data=[190, 87, 98, 45, 90, 9, 30])
    print('Minimum element: ', ll.min())
    # ll.printElements()
