"""
- DFS
- Save local coordinates of an island into set
  - local coordinates are calculated by current row - starting row and current col - starting col
  - Current island is a set of row and col tuples
  - We keep tack of a set of unique islands, which is collections of current islands
    - But in Python it's not allow to have a set of sets, so it's
      a set of frozensets.
"""


from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            # not grid[row][col] means see in grid is 0
            if (row, col) in seen or not grid[row][col]:
                return
            seen.add((row, col))
            # Local position put to set
            current_island.add((row - row_origin, col - col_origin))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)


        seen = set()
        unique_islands = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                current_island = set()
                row_origin = row
                col_origin = col
                dfs(row, col)
                if current_island:
                    # In Python elements in a set must be hashable
                    # Immutable objects are hashable, and mutable objects are not hashable
                    # Python set is mutable, but frozenset make it immutable object
                    unique_islands.add(frozenset(current_island))

                    # print(f'unique_islands: {unique_islands}')
                    # print(f'current_island: {current_island}')
                    # print()

        return len(unique_islands)


grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
print(Solution().numDistinctIslands(grid))


