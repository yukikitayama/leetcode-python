"""
[
    [1,2],
    [3,3]
]

Min heap
[(num, row_index, column_index)]
  row same
  col += 1

[(5, 0, 1), (10, 1, 0), (12, 2, 0),]

T: O(N**2)
S: O(N)
"""

from typing import List
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        for row in matrix:
            print(row)

        min_heap = []
        heapq.heapify(min_heap)

        # Initial
        for r in range(len(matrix)):
            heapq.heappush(min_heap, (matrix[r][0], r, 0))

        while k:
            num, r, c = heapq.heappop(min_heap)

            k -= 1

            if k == 0:
                return num

            if c + 1 < len(matrix):
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))

