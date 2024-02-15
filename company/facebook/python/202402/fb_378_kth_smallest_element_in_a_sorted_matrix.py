"""
Always square

Naive
  Iterate from left top to right bottom, return kth cell

Math
  First identity row, then identify column
  k // col gives row, k % col gives col
    8 // 3 = 2
    8 % 3 = 2, 2th element

[
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
From top-left, Identify the anti-diagonal which includes kth number
  Heap
    Put negative numbers to min heap
    When size is k, return heap top

"""

from typing import List
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        # Limit search space
        n = len(matrix)
        row = min(n, k)

        # Initialize min heap
        min_heap = []
        heapq.heapify(min_heap)
        for r in range(row):
            heapq.heappush(min_heap, (matrix[r][0], r, 0))

        while k:

            curr_num, curr_row, curr_col = heapq.heappop(min_heap)

            # If current row still has next column to go
            if curr_col < n - 1:
                heapq.heappush(min_heap, (matrix[curr_row][curr_col + 1], curr_row, curr_col + 1))

            k -= 1

        return curr_num

