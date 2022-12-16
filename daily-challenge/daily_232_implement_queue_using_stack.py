class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        if not self.stack1:
            self.stack1.append(x)
            return

        while self.stack1:
            self.stack2.append(self.stack1.pop())

        self.stack2.append(x)

        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        return self.stack1.pop()

    def peek(self) -> int:
        return self.stack1[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0


if __name__ == '__main__':
    obj = MyQueue()
    print(obj.push(1))
    print(obj.pop())
    print(obj.empty())
