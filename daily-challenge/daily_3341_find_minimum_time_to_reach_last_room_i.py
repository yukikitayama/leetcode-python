"""
[
    [0,4],
    [4,4]
]

[0,1],
[1,2]
"""

from typing import List
import heapq


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        d = [[float("inf")] * m for _ in range(n)]
        # Visited
        v = [[0] * m for _ in range(n)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        d[0][0] = 0
        q = []
        # [(distance, row, col)]
        heapq.heappush(q, (0, 0, 0))

        while q:
            distance, row, col = heapq.heappop(q)

            # If already visited, ignore
            if v[row][col]:
                continue

            v[row][col] = 1

            for dr, dc in dirs:
                nr = row + dr
                nc = col + dc

                if not (0 <= nr < n and 0 <= nc < m):
                    continue

                new_dist = max(d[row][col], moveTime[nr][nc]) + 1

                if new_dist < d[nr][nc]:
                    d[nr][nc] = new_dist
                    heapq.heappush(q, (new_dist, nr, nc))

        return d[n - 1][m - 1]