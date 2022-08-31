"""
- if diagonal, find cells which has less or equal in both direction
- if left off-diagonal,
"""


from typing import List
import collections


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pacific_queue = collections.deque()
        atlantic_queue = collections.deque()

        for i in range(m):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, n - 1))

        for i in range(n):
            pacific_queue.append((0, i))
            atlantic_queue.append((m - 1, i))

        def bfs(queue):

            reachable = set()

            while queue:
                row, col = queue.popleft()

                reachable.add((row, col))

                for offset_row, offset_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    next_row = row + offset_row
                    next_col = col + offset_col

                    if (
                        0 <= next_row < m
                        and 0 <= next_col < n
                        and (next_row, next_col) not in reachable
                        and heights[next_row][next_col] >= heights[row][col]
                    ):
                        queue.append((next_row, next_col))

            return reachable

        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)

        ans = []
        for element in pacific_reachable.intersection(atlantic_reachable):
            ans.append(list(element))

        return ans


if __name__ == '__main__':
    heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    print(Solution().pacificAtlantic(heights))
