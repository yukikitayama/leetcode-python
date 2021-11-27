"""
Implementation
- Iterative approach
"""


from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in seen:
                    area = 0
                    stack = [(row, col)]
                    seen.add((row, col))

                    while stack:
                        curr_row, curr_col = stack.pop()
                        area += 1

                        for next_row, next_col in [
                            (curr_row + 1, curr_col),
                            (curr_row - 1, curr_col),
                            (curr_row, curr_col + 1),
                            (curr_row, curr_col - 1)
                        ]:
                            if 0 <= next_row < len(grid) \
                                    and 0 <= next_col < len(grid[0]) \
                                    and grid[next_row][next_col] \
                                    and (next_row, next_col) not in seen:
                                stack.append((next_row, next_col))
                                seen.add((next_row, next_col))

                    ans = max(ans, area)

        return ans


grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
print(Solution().maxAreaOfIsland(grid))
