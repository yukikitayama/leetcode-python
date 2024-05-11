"""
Heap keeps multiple overlapping scenarios to keep track of current cumulative profit so far?

sort by start time in ascending
min heap
  [(end_time, cumulative profit)]
  keep previous, don't overwrite, add current end time and cumulative profit
After iteration, find max cumulative profit from min heap

[(3, 50, 0)]
[(3, 50, 0), (4, 10, 1)]
[(3, 50, 0), (4, 10, 1), (5, 90, )]
[(3, 50, 0), (4, 10, 1), (5, 90, ), (6, 120)]

curr start: 5, profit: 30
[(3, 10), (4, 20), (5, 40), (5, 50)]
"""

from typing import List
import heapq


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        data = []
        for i in range(len(startTime)):
            data.append([startTime[i], endTime[i], profit[i]])
        data.sort()

        min_heap = []
        max_so_far = 0

        for i in range(len(data)):

            while min_heap and min_heap[0][0] <= data[i][0]:
                prev_end, prev_profit = heapq.heappop(min_heap)

                max_so_far = max(max_so_far, prev_profit)

            heapq.heappush(min_heap, (data[i][1], data[i][2] + max_so_far))

            # print(min_heap, max_so_far)

        return max([cum_profit for end, cum_profit in min_heap])