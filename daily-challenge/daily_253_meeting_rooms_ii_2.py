from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        min_heap = []
        heapq.heapify(min_heap)

        ans = 0

        for i in range(len(intervals)):

            while min_heap and min_heap[0] <= intervals[i][0]:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, intervals[i][1])

            ans = max(ans, len(min_heap))

        return ans