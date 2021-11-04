class MaxStack:
    def __init__(self):
        # (current element, max_so_far)
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
        else:
            max_so_far = self.stack[-1][1]
            self.stack.append((x, max(x, max_so_far)))

        # print(f'  in push, self.stack: {self.stack}')

    def pop(self) -> int:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        tmp = []
        while self.stack[-1][0] != self.stack[-1][1]:
            popped = self.pop()
            tmp.append(popped)
        popped = self.pop()

        for item in tmp[::-1]:
            self.push(item)

        # print(f'  in popMax, self.stack: {self.stack}')

        return popped


# obj = MaxStack()
# obj.push(5)
# obj.push(1)
# obj.push(5)
# print(obj.top())
# print(obj.popMax())
# print(obj.top())
# print(obj.peekMax())
# print(obj.pop())

obj = MaxStack()
obj.push(5)
obj.push(1)
print(obj.popMax())
print(obj.peekMax())
