import collections


class MyStack:

    def __init__(self):
        self.queue = collections.deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        size = len(self.queue)
        while size > 1:
            popped = self.queue.popleft()
            self.queue.append(popped)
            size -= 1

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


if __name__ == '__main__':
    obj = MyStack()
    print(obj.push(1))
    print(obj.push(2))
    print(obj.top())
    print(obj.pop())
    print(obj.empty())
