"""
Greedy by min heap

T: nlogn
S: n

edge case is only stick
"""

from typing import List
import heapq


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:

        if len(sticks) == 1:
            return 0

        heap = []
        heapq.heapify(heap)

        for stick in sticks:
            heapq.heappush(heap, stick)

        ans = 0

        while len(heap) > 1:

            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            connected = first + second
            ans += connected

            heapq.heappush(heap, connected)

        return ans


if __name__ == "__main__":
    sticks = [2, 4, 3]
    sticks = [1, 8, 3, 5]
    print(Solution().connectSticks(sticks))
