"""
4 * 7 = 28

One island 4
Adding one more island adds 4, but subtract by the number of border shares

Find how many neighbors the current cell has
  add 4 - the neighbors num to answer
    Can I find the number of neighbors on the go?
      BFS, when check all direction, count neighbors, and add to queue
  Add neighbors to the next recursion

Nested for loop
  when current cell is 1,
    compute sum of neighbors
    add 4 - neighbors to answer
"""

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def count_neighbors(r, c):
            count = 0
            for offset_r, offset_c in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                neighbor_r = r + offset_r
                neighbor_c = c + offset_c
                if 0 <= neighbor_r < len(grid) and 0 <= neighbor_c < len(grid[0]) and grid[neighbor_r][neighbor_c] == 1:
                    count += 1
            return count

        ans = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    neighbors = count_neighbors(r, c)
                    ans += (4 - neighbors)

        return ans
