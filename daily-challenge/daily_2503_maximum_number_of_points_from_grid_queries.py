from typing import List


import heapq


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        ans = [0] * len(queries)
        sorted_queries = sorted([(v, i) for i, v in enumerate(queries)])
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        min_heap = []
        # [(cell value, row, col), ...]
        heapq.heappush(min_heap, (grid[0][0], 0, 0))
        visited[0][0] = True
        total_points = 0

        for query_value, query_index in sorted_queries:

            while min_heap and min_heap[0][0] < query_value:

                v, r, c = heapq.heappop(min_heap)

                total_points += 1

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and not visited[nr][nc]:
                        heapq.heappush(min_heap, (grid[nr][nc], nr, nc))
                        visited[nr][nc] = True

            ans[query_index] = total_points

        return ans
