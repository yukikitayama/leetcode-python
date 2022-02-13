class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = [0] * size
        self.head = 0
        self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        tail = (self.head + 1) % self.size

        # e.g. size: 3, queue: [0, 0, 0], head: 0, count: 0, window_sum: 0
        # val: 1, count: 1, tail: 1, window_sum: 1, head: 1, queue: [0, 1, 0]
        # val: 2, count: 2, tail: 2, window_sum: 1 - 0 + 2 = 3, head: 2, queue: [0, 1, 2]
        # val: 3, count: 3, tail: 0, window_sum: 3 - 0 + 3 = 6, head: 0, queue: [3, 1, 2]
        # val: 4, count: 4, tail: 1, window_sum: 6 - 1 + 4 = 9, head: 1, queue: [3, 4, 2]
        self.window_sum = self.window_sum - self.queue[tail] + val

        # Overwrite tail value with head value if queue is full
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val

        # Calculate moving average
        return self.window_sum / min(self.size, self.count)

