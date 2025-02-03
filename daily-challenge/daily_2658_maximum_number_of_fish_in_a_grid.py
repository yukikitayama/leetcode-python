"""
BFS
  running sum
"""

from typing import List
import collections


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ans = 0

        def bfs(r, c):
            res = 0
            # [(row, col), ...]
            queue = collections.deque([(r, c)])
            while queue:
                for _ in range(len(queue)):
                    curr_r, curr_c = queue.popleft()
                    res += grid[curr_r][curr_c]
                    grid[curr_r][curr_c] = 0

                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        next_r = curr_r + dr
                        next_c = curr_c + dc
                        if 0 <= next_r < len(grid) and 0 <= next_c < len(grid[0]):
                            if grid[next_r][next_c] > 0:
                                queue.append((next_r, next_c))

            return res

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > 0:
                    res = bfs(r, c)
                    ans = max(ans, res)
                    # print(r, c, res)

        return ans