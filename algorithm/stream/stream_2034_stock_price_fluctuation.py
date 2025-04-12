"""
Constructor
  hashmap
    k: t, v: p
  latest_timestamp
update
  update hashmap
  update latest timestamp
current
  get value of the latest t
maximum
  iterate hashmap

Heap?
"""

import collections
import heapq


class StockPrice:

    def __init__(self):
        self.t_to_p = collections.defaultdict(int)
        self.min_heap = []
        self.max_heap = []
        self.latest_t = 0

    def update(self, timestamp: int, price: int) -> None:
        self.t_to_p[timestamp] = price

        if timestamp > self.latest_t:
            self.latest_t = timestamp

        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        return self.t_to_p[self.latest_t]

    def maximum(self) -> int:
        # max_heap[0][0] is -1 * max price
        # max_heap[0][1] is timestamp pf max price
        while self.max_heap and (-1 * self.max_heap[0][0]) != self.t_to_p[self.max_heap[0][1]]:
            heapq.heappop(self.max_heap)
        return -self.max_heap[0][0]

    def minimum(self) -> int:
        while self.min_heap and (self.min_heap[0][0]) != self.t_to_p[self.min_heap[0][1]]:
            heapq.heappop(self.min_heap)
        return self.min_heap[0][0]


class StockPrice1:

    def __init__(self):
        self.t_to_p = collections.defaultdict(int)
        self.latest_t = 0

    def update(self, timestamp: int, price: int) -> None:
        self.t_to_p[timestamp] = price
        if timestamp > self.latest_t:
            self.latest_t = timestamp

    def current(self) -> int:
        return self.t_to_p[self.latest_t]

    def maximum(self) -> int:
        return max(self.t_to_p.values())

    def minimum(self) -> int:
        return min(self.t_to_p.values())

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()