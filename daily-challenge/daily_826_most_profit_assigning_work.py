"""
Sort worker array
sort job data by difficulty ascending
iterate worker array
  while difficulty is <= worker element
    append profit to max heap by profit
  increment answer by top of max heap
"""

from typing import List
import heapq


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = [[d, p] for d, p in zip(difficulty, profit)]
        jobs.sort()
        worker.sort()

        # print(jobs)
        # print(worker)

        max_heap = []
        p_j = 0
        ans = 0

        for p_w in range(len(worker)):

            while p_j < len(jobs) and jobs[p_j][0] <= worker[p_w]:
                heapq.heappush(max_heap, -jobs[p_j][1])
                p_j += 1

            if max_heap:
                ans += -max_heap[0]

        return ans