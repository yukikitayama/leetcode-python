class MaxStack:
    def __init__(self):
        # A list of (current value, max so far)
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, max(x, self.stack[-1][1])))

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:

        # print(f'stack: {self.stack}')

        return self.stack[-1][1]

    def popMax(self) -> int:

        # print(f'stack: {self.stack}')

        m = self.stack[-1][1]
        b = []
        while self.stack[-1][0] != m:
            b.append(self.pop())

        self.pop()

        for num in b[::-1]:
            self.push(num)

        return m


# obj = MaxStack()
# obj.push(5)
# obj.push(1)
# obj.push(5)
# print(obj.top())
# print(obj.popMax())
# print(obj.top())
# print(obj.peekMax())
# print(obj.pop())
# print(obj.top())

# Expected: [null, null, null, 5, 1]
obj = MaxStack()
obj.push(5)
obj.push(1)
print(obj.popMax())
print(obj.peekMax())
