from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])

        left = 0
        right = 1_000_000

        def can_reach_destination(mid):
            visited = [[False] * col for _ in range(row)]
            queue = [(0, 0)]
            while queue:
                x, y = queue.pop(0)

                if x == row - 1 and y == col - 1:
                    return True

                visited[x][y] = True

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    adjacent_x = x + dx
                    adjacent_y = y + dy

                    if 0 <= adjacent_x < row and 0 <= adjacent_y < col and not visited[adjacent_x][adjacent_y]:
                        curr_diff = abs(heights[adjacent_x][adjacent_y] - heights[x][y])
                        if curr_diff <= mid:
                            visited[adjacent_x][adjacent_y] = True
                            queue.append((adjacent_x, adjacent_y))

        while left < right:
            mid = (left + right) // 2

            if can_reach_destination(mid):
                right = mid
            else:
                left = mid + 1

        return left


heights = [[1,2,2],[3,8,2],[5,3,5]]
print(Solution().minimumEffortPath(heights))
