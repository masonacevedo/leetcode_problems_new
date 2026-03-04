class MinStack:

    def __init__(self):
        self.normalStack = []
        self.minStack = []
        self.currentMin = float('inf')
        

    def push(self, val: int) -> None:
        self.normalStack.append(val)
        self.currentMin = min(self.currentMin, val)
        self.minStack.append(self.currentMin)
        

    def pop(self) -> None:
        # print("popping:")
        # print("normalStack:", self.normalStack)
        # print("minStack:", self.minStack)
        # print("currentMin:", self.currentMin)
        # input()
        self.normalStack.pop()
        self.minStack.pop()
        if len(self.normalStack) == 0:
            self.currentMin = float('inf')
        else:
            self.currentMin = self.minStack[-1]
        print()
        

    def top(self) -> int:
        return self.normalStack[-1]

    def getMin(self) -> int:
        return self.currentMin
        


# Your MinStack object will be instantiated and called as such:

myStack = MinStack()
myStack.push(1)
myStack.push(2)

assert(myStack.getMin() == 1)
myStack.pop()
assert(myStack.getMin() == 1)
myStack.pop()
myStack.push(3)
myStack.push(2)
myStack.push(1)
myStack.push(4)
assert(myStack.getMin() == 1)

myStack.pop()
