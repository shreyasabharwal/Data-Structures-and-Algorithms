# Node Insertion


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


if __name__ == "__main__":
    # Creating Stack
    ll = Stack(data=[1, 87, 98, 45, 90, 9, 3])
    ll.printElements()
    print(ll.pop())
