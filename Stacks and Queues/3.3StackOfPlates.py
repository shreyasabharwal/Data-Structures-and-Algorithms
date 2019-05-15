'''3.3 Stack of Plates: Imagine a(literal) stack of plates. If the stack gets too high, it might topple.
    Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
    threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
    composed of several stacks and should create a new stack once the previous one exceeds capacity.
    SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
    (that is, pop() should return the same values as it would if there were just a single stack).
'''


class Node:
    # constructor
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack(object):
    def __init__(self, capacity=None, data=None):
        self.top = None
        self.capacity = capacity
        self.size = 0
        if not data and data:
            for d in data:
                self.push(d)

    def push(self, data):
        "Push/add an element"
        if self.size > self.capacity:
            return False
        node = Node(data)
        node.next = self.top
        self.top = node
        self.size += 1
        return True

    def pop(self):
        "Pop/remove an element"
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def isEmpty(self):
        return self.top == None

    def isFull(self):
        return self.size == self.capacity

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def printElements(self):
        "Print elements of the linked list"
        current = self.top
        while current != None:
            print(current.data, end='\t')
            current = current.next


class SetOfStacks(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.listOfStacks = []

    def getLastStack(self):
        if not self.listOfStacks:
            return None
        return self.listOfStacks[-1]

    def push(self, data):
        last = self.getLastStack()
        if last and not last.isFull():
            last.push(data)
        else:
            newStack = Stack(self.capacity)
            newStack.push(data)
            self.listOfStacks.append(newStack)

    def pop(self):
        last = self.getLastStack()
        if last.isEmpty():
            return None
        data = last.pop()
        if last.isEmpty():
            del self.listOfStacks[-1]
        return data

    def printStack(self, stackNum=None):
        if stackNum and len(self.listOfStacks) != 0:
            print('##############', 'Stcak Number: ',
                  stackNum, '##############')
            stack = self.listOfStacks[stackNum]
            stack.printElements()


if __name__ == "__main__":
    # Creating Stack
    s1 = SetOfStacks(3)
    s1.push(7)
    s1.push(5)
    s1.push(3)
    s1.push(2)
    s1.push(6)
    s1.push(15)
    s1.pop()
    s1.printStack(1)
