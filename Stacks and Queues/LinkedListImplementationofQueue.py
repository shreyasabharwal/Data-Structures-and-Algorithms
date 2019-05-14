# Node Insertion


class Node:
    # constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Queue(object):
    def __init__(self):
        self.front = self.rear = None

    def EnQueue(self, data):
        "Add an element at the rear"
        node = Node(data)
        if self.rear == None:
            self.front = self.rear = node
            return
        self.rear.next = node
        self.rear = node

    def DeQueue(self):
        "Remove an element from the front"
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
        return temp.data

    def isEmpty(self):
        return self.front == None

    def peek(self):
        if self.front is None:
            return None
        return self.front.data

    def length(self):
        "Print number of elements"
        current = self.front
        count = 0
        while current != None:
            count += 1
            current = current.next
        return count

    def printElements(self):
        "Print elements of the linked list"
        current = self.front
        while current != None:
            print(current.data, end='\t')
            current = current.next


if __name__ == "__main__":
    # Creating Queue
    q = Queue()
    q.EnQueue('23')
    q.EnQueue('81')
    q.EnQueue('50')
    q.EnQueue('65')
    q.EnQueue('10')
    q.EnQueue('12')

    q.DeQueue()
    q.DeQueue()
    q.printElements()
