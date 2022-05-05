class MyStack:
    def __init__(self):
        self.queue = []
        self.top_element = None

    def push(self, x: int) -> None:
        self.top_element = x
        self.queue.append(x)
        n = len(self.queue)
        while n > 1:
            self.queue.append(self.queue.pop(0))
            n -= 1

    def pop(self) -> int:
        ans = self.queue.pop(0)
        if self.queue:
            self.top_element = self.queue[0]
        else:
            self.top_element = None
        return ans

    def top(self) -> int:
        return self.top_element

    def empty(self) -> bool:
        return len(self.queue) == 0


class MyStack1:
    def __init__(self):
        self.last = None
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.last = x

    def pop(self) -> int:
        popped = []
        n = len(self.queue)
        for i in range(n):
            if i != (n - 1):
                self.last = self.queue.pop(0)
                popped.append(self.last)
            else:
                ans = self.queue.pop(0)
        self.queue = popped
        return ans

    def top(self) -> int:
        return self.last

    def empty(self) -> bool:
        return len(self.queue) == 0


if __name__ == '__main__':
    obj = MyStack()
    print(obj.push(1))
    print(obj.push(2))
    # print(obj.top())
    # print(obj.pop())
    print(obj.pop())
    print(obj.top())
    print(obj.empty())
