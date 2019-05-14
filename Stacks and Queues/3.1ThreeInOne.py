'''
3.1 Three in One: Describe how you could use a single array to implement three stacks.
'''


class MultiStack:

    def __init__(self, stackSize):
        # Num of stacks to be created
        self.numStacks = 3
        # Tracking current size of each of the stacks
        self.sizes = [0]*self.numStacks
        # Placeholder for stack values
        self.stackValues = [0]*(self.numStacks*stackSize)
        # Fixed stack size
        self.stackSize = stackSize

    def push(self, data, stackNum):
        if self.isFull(stackNum):
            raise Exception('Stack is Full')
        self.sizes[stackNum] += 1
        self.stackValues[self.indexOfTop(stackNum)] = data

    def pop(self, stackNum):
        if self.isEmpty(stackNum):
            raise Exception('Stack is Empty')
        self.sizes[stackNum] -= 1
        val = self.stackValues[self.indexOfTop(stackNum)]
        self.stackValues[self.indexOfTop(stackNum)] = 0
        return val

    def peek(self, stackNum):
        if self.isEmpty(stackNum):
            raise Exception('Stack is Empty')
        return self.stackValues[self.indexOfTop(stackNum)]

    def isEmpty(self, stackNum):
        return self.sizes[stackNum] == 0

    def isFull(self, stackNum):
        return self.sizes[stackNum] == self.stackSize

    def indexOfTop(self, stackNum):
        # offset: calculate spaces occupied by prior stacks
        offset = stackNum*self.stackSize
        return offset+self.sizes[stackNum]-1


if __name__ == "__main__":
    ss = MultiStack(2)
    print(ss.isEmpty(1))
    ss.push(40, 1)
    ss.push(31, 1)
    print(ss.peek(1))
    ss.push(89, 0)
    ss.pop(1)
    print(ss.peek(1))
    print(ss.peek(2))
