"""
if curr start < prev end
  append to stack
if curr start >= prev end
  pop stack top
  append curr to stack

sort intervals by start time

eg
[[0, 10], [5, 15], [11, 20]]
  2nd meeting cannot end before 3rd meeting
  but 1st meeting can end before 3rd meeting

efficiently access previous end times
hashmap
  k: meeting roo,
  v: end time
But needs to scan all keys every time

Heap
  min heap
    (end time)
  if curr start < heap top end, append
  if curr start > heap top end, pop

Return heap size
"""

from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        min_heap = []
        heapq.heapify(min_heap)

        for i in range(len(intervals)):

            if min_heap and intervals[i][0] >= min_heap[0]:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, intervals[i][1])

        return len(min_heap)
