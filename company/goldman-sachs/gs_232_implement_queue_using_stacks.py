
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.front = None

    # Time is O(1)
    def push(self, x: int) -> None:
        if len(self.stack1) == 0:
            self.front = x
        self.stack1.append(x)

    # Time is amortized O(1), but in the worst case O(n)
    def pop(self) -> int:
        if len(self.stack2) == 0:
            while self.stack1:
                popped = self.stack1.pop()
                self.stack2.append(popped)
        return self.stack2.pop()

    def peek(self) -> int:
        if len(self.stack2) != 0:
            return self.stack2[-1]
        return self.front

    def empty(self) -> bool:
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return True
        else:
            return False


class MyQueue1:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop(0)

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        if len(self.queue) > 0:
            return False
        else:
            return True


if __name__ == '__main__':

    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    print(obj.peek())
    print(obj.pop())
    print(obj.empty())
