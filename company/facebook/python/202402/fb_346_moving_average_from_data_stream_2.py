import collections


class MovingAverage:

    def __init__(self, size: int):
        self.queue = collections.deque()
        self.sum_ = 0
        self.count = 0
        self.size = size

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.sum_ += val
        self.count += 1

        if len(self.queue) > self.size:
            old_num = self.queue.popleft()
            self.count -= 1
            self.sum_ -= old_num

        return self.sum_ / self.count

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)