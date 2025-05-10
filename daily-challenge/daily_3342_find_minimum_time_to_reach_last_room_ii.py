from typing import List
import heapq


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        distances = [[float("inf")] * len(moveTime[0]) for _ in range(len(moveTime))]
        distances[0][0] = 0
        visited = [[False] * len(moveTime[0]) for _ in range(len(moveTime))]

        min_heap = []
        # [(distance, row, col)]
        heapq.heappush(min_heap, (0, 0, 0))

        while min_heap:

            d, r, c = heapq.heappop(min_heap)

            if visited[r][c]:
                continue

            if r == len(moveTime) - 1 and c == len(moveTime[0]) - 1:
                break

            visited[r][c] = True

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < len(moveTime) and 0 <= nc < len(moveTime[0]):

                    # Moving between adjacent rooms takes one second for one move and two seconds for the next, alternating between the two.
                    # r: 0, c: 0, (r + c) % 2: 0
                    # r: 0, c: 1, (r + c) % 2: 1
                    nd = max(d, moveTime[nr][nc]) + 1 + (r + c) % 2
                    if nd < distances[nr][nc]:
                        distances[nr][nc] = nd
                        heapq.heappush(min_heap, (nd, nr, nc))

        return distances[-1][-1]