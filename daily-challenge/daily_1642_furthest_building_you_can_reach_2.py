"""
- Stack?
- Greedy
- Simulation
"""


from typing import List
import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        heapq.heapify(heap)

        for i in range(len(heights) - 1):

            climb = heights[i + 1] - heights[i]

            # If negative, current building is higher than the next building
            # so no need to climb to use ladders nor bricks
            if climb <= 0:
                continue

            # Add climb (ladder) to min heap
            heapq.heappush(heap, climb)

            # If we haven't gone over the number of ladders, nothing else to do
            if len(heap) <= ladders:
                continue

            # Get smallest ladder from min heap
            ladder = heapq.heappop(heap)
            # Replace the climb to which a ladder was used with bricks
            bricks -= ladder

            if bricks < 0:
                return i

        return len(heights) - 1


if __name__ == '__main__':
    heights = [4, 2, 7, 6, 9, 14, 12]
    bricks = 5
    ladders = 1
    print(Solution().furthestBuilding(heights, bricks, ladders))
