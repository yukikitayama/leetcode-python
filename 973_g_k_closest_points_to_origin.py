from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)

        for (x, y) in points:
            # Negative allow us to make max heap, meaning top of the heap is the largest
            distance = -(x * x + y * y)

            if len(heap) == k:
                # heappushpop pushes item and pop the top of the heap
                # Here len(heap): k + 1 but immediately pop the farther item from the origin
                heapq.heappushpop(heap, (distance, x, y))
                # print(f'Heap: {heap}')

            else:
                # heappush can push tuple, ordered by the first element
                heapq.heappush(heap, (distance, x, y))
                # print(f'Heap: {heap}')

        return [[x, y] for (_, x, y) in heap]


"""
Time complexity
Let k be the size of heap, and n be the length of points
O(logk) to push and pop the heap, and O(n) to iterate all the points,
so O(nlogk)

Space complexity
O(k) for heap
"""



# points = [[1, 3], [-2, 2]]
# k = 1
points = [[3, 3], [5, -1], [-2, 4]]
k = 2
print(Solution().kClosest(points, k))
