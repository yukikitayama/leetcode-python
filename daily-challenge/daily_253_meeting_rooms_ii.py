"""
- Sort by end in ascending order
- Iterate by index
- Time O(nlogn)
"""


from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])

        # Heap is min heap containing end time
        # top element is the earliest ending meeting
        heap = []
        heapq.heappush(heap, intervals[0][1])

        for i in range(1, len(intervals)):

            # If current meeting starts after the earliest ending meeting
            # remove the meeting in the heap
            if intervals[i][0] >= heap[0]:
                heapq.heappop(heap)

            # Assign a new meeting room for the current meeting
            heapq.heappush(heap, intervals[i][1])

        return len(heap)


if __name__ == '__main__':
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(Solution().minMeetingRooms(intervals))
