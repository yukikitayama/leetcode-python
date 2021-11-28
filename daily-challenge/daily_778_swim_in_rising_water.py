import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)

        seen = {(0, 0)}
        # (elevation, row, column)
        pq = [(grid[0][0], 0, 0)]
        ans = 0

        while pq:

            d, r, c = heapq.heappop(pq)
            ans = max(ans, d)

            # Destination
            if r == c == N - 1:
                return ans

            # Top, down left, right
            for cr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):

                # If a new place is in the boundary and have not visited yet
                if 0 <= cr < N and 0 <= cc < N and (cr, cc) not in seen:
                    heapq.heappush(pq, (grid[cr][cc], cr, cc))
                    seen.add((cr, cc))