"""
we begin by treating the edges of the grid as the initial boundary since water cannot spill beyond them.
From there, we move inward, processing cells in a manner that respects the relationship between a cell’s height and the boundary
"""

from typing import List
import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        R = len(heightMap)
        C = len(heightMap[0])
        visited = [[False] * C for _ in range(R)]
        # [(height, row, col), ...]
        min_heap = []

        # Leftmost column and rightmost column
        for r in range(R):
            # Left
            heapq.heappush(min_heap, (heightMap[r][0], r, 0))
            visited[r][0] = True
            # Right
            heapq.heappush(min_heap, (heightMap[r][C - 1], r, C - 1))
            visited[r][C - 1] = True

        # Top row and bottom row
        for c in range(C):
            # Top
            heapq.heappush(min_heap, (heightMap[0][c], 0, c))
            visited[0][c] = True
            # Bottom
            heapq.heappush(min_heap, (heightMap[R - 1][c], R - 1, c))
            visited[R - 1][c] = True

        ans = 0

        while min_heap:

            curr_height, curr_row, curr_col = heapq.heappop(min_heap)

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                neighbor_row = curr_row + dr
                neighbor_col = curr_col + dc

                if 0 <= neighbor_row < R and 0 <= neighbor_col < C:
                    if not visited[neighbor_row][neighbor_col]:

                        neighbor_height = heightMap[neighbor_row][neighbor_col]
                        if neighbor_height < curr_height:
                            ans += curr_height - neighbor_height

                        heapq.heappush(min_heap, (max(curr_height, neighbor_height), neighbor_row, neighbor_col))
                        visited[neighbor_row][neighbor_col] = True

        return ans