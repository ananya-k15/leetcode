class MinStack:
    
    def __init__(self):
        self.stack = []
        self.minElement = 0

    def push(self, val: int) -> None:
        if self.stack == [] : 
            self.minElement = val
        else : 
            self.minElement = min(self.minElement, val)
        self.stack.append(val)

    def pop(self) -> None:
        element = self.stack.pop()
        if self.stack == [] : 
            self.minElement = 0
        else : 
            self.minElement = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minElement


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()