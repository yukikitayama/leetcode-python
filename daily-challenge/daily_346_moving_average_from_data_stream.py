import collections


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = collections.deque()

    def next(self, val: int) -> float:
        self.queue.append(val)

        if len(self.queue) > self.size:
            self.queue.popleft()

        return sum(self.queue) / len(self.queue)


if __name__ == "__main__":
    obj = MovingAverage(3)
    print(obj.next(1))
    print(obj.next(10))
    print(obj.next(3))
    print(obj.next(5))

