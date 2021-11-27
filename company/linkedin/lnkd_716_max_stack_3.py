class MaxStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
        else:
            max_so_far = self.stack[-1][1]
            max_so_far = max(max_so_far, x)
            self.stack.append((x, max_so_far))

        # print(f'  stack: {self.stack}')

    def pop(self) -> int:
        x, max_so_far = self.stack.pop()
        return x

    def top(self) -> int:
        return self.stack[-1][0]

    def peekMax(self) -> int:
        return self.stack[-1][1]

    def popMax(self) -> int:
        tmp = []
        while self.stack and self.stack[-1][1] != self.stack[-1][0]:
            popped = self.stack.pop()
            tmp.append(popped)
        popped = self.stack.pop()

        for p in tmp[::-1]:
            self.push(p[0])

        return popped[0]


obj = MaxStack()
obj.push(5)
obj.push(1)
obj.push(5)
print(obj.top())
print(obj.popMax())
print(obj.top())
print(obj.peekMax())
print(obj.pop())
print(obj.top())
# obj.push(5)
# obj.push(1)
# print(obj.popMax())
# print(obj.peekMax())
