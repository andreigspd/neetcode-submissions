class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix_stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.prefix_stack.append(min(val, self.prefix_stack[-1]) if self.prefix_stack else val)
    def pop(self) -> None:
        self.stack.pop()
        self.prefix_stack.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix_stack[-1]
