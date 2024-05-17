"""
BFS from thief cell
"""

from typing import List
import collections
import heapq


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        # Find cells which have thieves
        queue = collections.deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    grid[r][c] = 0
                else:
                    # Pre-mark as unvisited for the following BFS
                    grid[r][c] = -1

        # Compute the minimum distance to the nearest thief for each cell
        while queue:

            for _ in range(len(queue)):

                curr_r, curr_c = queue.popleft()

                for offset_r, offset_c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

                    next_r = curr_r + offset_r
                    next_c = curr_c + offset_c

                    if 0 <= next_r < len(grid) and 0 <= next_c < len(grid[0]):
                        if grid[next_r][next_c] == -1:
                            grid[next_r][next_c] = grid[curr_r][curr_c] + 1
                            queue.append((next_r, next_c))

        # for row in grid:
        #     print(row)

        # Dijkstra's algorithm to choose a path with a large safeness
        # Along that, compute the minimum safeness so far in the path
        max_heap = []
        heapq.heappush(max_heap, (-grid[0][0], 0, 0))
        grid[0][0] = -1

        while max_heap:

            curr_min_safe, curr_r, curr_c = heapq.heappop(max_heap)

            # print(curr_min_safe, curr_r, curr_c)

            if curr_r == len(grid) - 1 and curr_c == len(grid[0]) - 1:
                # - because we multipled -1 to make max heap
                return -curr_min_safe

            for offset_r, offset_c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

                next_r = curr_r + offset_r
                next_c = curr_c + offset_c

                if 0 <= next_r < len(grid) and 0 <= next_c < len(grid[0]):
                    if grid[next_r][next_c] != -1:
                        # print("  ", next_r, next_c)
                        # curr_min_safe: -3 (actually 3), grid next: 2,
                        real_curr_min = curr_min_safe * -1
                        next_safe = min(real_curr_min, grid[next_r][next_c])
                        heapq.heappush(max_heap, (-next_safe, next_r, next_c))
                        grid[next_r][next_c] = -1

        # Not necessary because constraints say at least one thief
        return -1