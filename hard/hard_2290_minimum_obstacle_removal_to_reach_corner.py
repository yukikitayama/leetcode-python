from typing import List
import collections
import heapq


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        min_obstacles = [[float("inf")] * len(grid[0]) for _ in range(len(grid))]
        min_obstacles[0][0] = 0
        queue = collections.deque([(0, 0, 0)])

        while queue:

            o, r, c = queue.popleft()

            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return o

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and min_obstacles[nr][nc] == float("inf"):

                    if grid[nr][nc] == 1:
                        min_obstacles[nr][nc] = o + 1
                        queue.append((o + 1, nr, nc))

                    else:
                        min_obstacles[nr][nc] = o
                        queue.appendleft((o, nr, nc))

        return min_obstacles[len(grid) - 1][len(grid[0]) - 1]

    def minimumObstacles1(self, grid: List[List[int]]) -> int:
        min_obstacles = [[float("inf")] * len(grid[0]) for _ in range(len(grid))]
        min_obstacles[0][0] = 0
        pq = [(0, 0, 0)]

        while pq:

            o, r, c = heapq.heappop(pq)

            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return o

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    no = o + grid[nr][nc]
                    if no < min_obstacles[nr][nc]:
                        min_obstacles[nr][nc] = no
                        heapq.heappush(pq, (no, nr, nc))

        return min_obstacles[len(grid) - 1][len(grid[0]) - 1]