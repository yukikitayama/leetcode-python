class MinStack:
    def __init__(self):
        # a list of (val, current min)
        self.stack = []

    def push(self, val: int) -> None:
        # O(1) to push
        if not self.stack:
            self.stack.append((val, val))

        # O(1) to get the end element in the stack and append
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))

    def pop(self) -> None:
        # O(1) to remove the end element
        self.stack.pop()

    def top(self) -> int:
        # O(1) to access the end element
        return self.stack[-1][0]

    def getMin(self) -> int:
        # O(1) to access the end element
        return self.stack[-1][1]
