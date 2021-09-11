from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # True if length of intervals is 0, empty list
        if not intervals:
            return 0

        # Make heap data structure to do priority queue in Python
        free_rooms = []
        heapq.heapify(free_rooms)
        # Sort by starting time to do sequentially for loop
        intervals.sort(key=lambda x: x[0])
        # Push the first meeting ending time for loop initialization
        heapq.heappush(free_rooms, intervals[0][1])

        for i in intervals[1:]:
            # Python heapq implements min heap so top of the binary tree is the min
            # True if earliest ending time is smaller than the current starting time, we can use this meeting room
            # It needs to be <= because it can still schedule if ending time is equal to starting time in this question
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)

            # Push current ending time anyway regardless of popping or not
            heapq.heappush(free_rooms, i[1])

        return len(free_rooms)


"""
Time complexity
Let n be the number of intervals.
O(nlogn) to sort intervals. Insert and pop from heap is O(logn)
so O(nlogn + logn) = O(nlogn)

Space complexity
O(n) to make heap
"""


intervals = [[0,30],[5,10],[15,20]]
intervals = [[7,10],[2,4]]
intervals = [[1, 2], [2, 3]]
print(Solution().minMeetingRooms(intervals))
