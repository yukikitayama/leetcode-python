"""
Stack
Heap
"""

import bisect


class RangeModule:

    def __init__(self):
        # Sorted pairs of start and end, always even number of elements
        self.track = []

    def addRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)

        subtrack = []
        if start % 2 == 0:
            subtrack.append(left)
        if end % 2 == 0:
            subtrack.append(right)
        self.track[start:end] = subtrack

        # print(f"addRange, track: {self.track}, subtrack: {subtrack}, start: {start}, end: {end}")

    def queryRange(self, left: int, right: int) -> bool:
        start = bisect.bisect_right(self.track, left)
        end = bisect.bisect_left(self.track, right)

        # print(f"track: {self.track}, start: {start}, end: {end}")

        # == checks left and right are in the same pair of range
        # % 2 == 1 checks left and right are inside the start and end pair
        return start == end and start % 2 == 1

    def removeRange(self, left: int, right: int) -> None:
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)

        subtrack = []
        if start % 2 == 1:
            subtrack.append(left)
        if end % 2 == 1:
            subtrack.append(right)

        self.track[start:end] = subtrack

        # print(f"removeRange, track: {self.track}, subtrack: {subtrack}, start: {start}, end: {end}")

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)