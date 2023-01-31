class Stack2:
    def __init__(self):
        self.values = []
    def push(self, val):
        self.values.append(val)
    def pop(self):
        self.values.pop()

class MinStack:
    def __init__(self):
        self.values = []
        self.min_value = None
        self.reserve_stack = Stack2()

    def push(self, val: int) -> None:
        if not self.values:
            self.min_value = val
        else:
            if self.min_value > val:
                self.min_value = val
        self.values.append(val)
        self.reserve_stack.push(self.min_value)

    def pop(self) -> None:
        self.values.pop()
        self.reserve_stack.pop()
        if not self.values:
            self.min_value = None
        else:
            self.min_value = self.reserve_stack.values[-1]

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.reserve_stack.values[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()