from typing import List
import heapq


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:

        # Edge case, left and down
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        # [(time, row, col), ...]
        min_heap = []
        heapq.heappush(min_heap, (grid[0][0], 0, 0))
        visited = set()

        while min_heap:

            t, r, c = heapq.heappop(min_heap)

            if (r, c) == (len(grid) - 1, len(grid[0]) - 1):
                return t

            if (r, c) in visited:
                continue
            visited.add((r, c))

            for offset_r, offset_c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_r = r + offset_r
                next_c = c + offset_c

                if 0 <= next_r < len(grid) and 0 <= next_c < len(grid[0]) and (next_r, next_c) not in visited:
                    waste = 1 if (grid[next_r][next_c] - t) % 2 == 0 else 0
                    next_t = max(
                        grid[next_r][next_c] + waste,
                        t + 1
                    )
                    heapq.heappush(min_heap, (next_t, next_r, next_c))

        return -1