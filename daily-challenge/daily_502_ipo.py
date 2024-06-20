"""
max heap
  contain projects whose capital is greater than or equal to current capital

e.g.
  k: 1
  w: 2
  profits: [1, 2, 3]
  capital: [1, 1, 2]
  expexted: 5
"""

from typing import List
import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        data = []
        for i in range(len(profits)):
            data.append([capital[i], profits[i], i])
        data.sort(key=lambda x: (x[0], -x[1]))

        # print(data)

        ans = 0
        curr_capital = w
        i = 0

        max_heap = []

        for _ in range(k):

            while i < len(data) and data[i][0] <= curr_capital:
                heapq.heappush(max_heap, (-data[i][1]))
                i += 1

            if max_heap:
                curr_capital += -1 * heapq.heappop(max_heap)

        return curr_capital
