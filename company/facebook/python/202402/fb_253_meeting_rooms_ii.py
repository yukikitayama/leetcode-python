"""
count the number of overlap
stack
  if stack is empty, append
  if current start is earlier than stack top end
    append current interval to stack
  if current start is later than stack top end
    pop from stack

sort intervals by first element in ascending
track current number of rooms occupied
track max so far
"""

from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        min_heap = []
        heapq.heapify(min_heap)

        ans = 0

        intervals.sort()

        for i in range(len(intervals)):

            interval = intervals[i]

            while min_heap and min_heap[0][0] <= interval[0]:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, (interval[1], interval[0], i))

            ans = max(ans, len(min_heap))

        return ans
