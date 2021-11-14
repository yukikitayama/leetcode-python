"""
- Union find
"""


from typing import List


class UnionFind:
    def __init__(self, grid):
        self.count = 0
        self.m = len(grid)
        self.n = len(grid[0])
        self.parent = [0] * (self.m * self.n)
        for row in range(self.m):
            for col in range(self.n):
                if grid[row][col] == '1':
                    # Why * n?
                    # row is the base to add col
                    # For each row, we need to have base for each col to add col
                    # so multiply n, not m.
                    self.parent[row * self.n + col] = row * self.n + col
                    self.count += 1
        self.rank = [0] * (self.m * self.n)

        # print(f'count: {self.count}')
        # print(f'len(parent): {len(self.parent)}, parent: {self.parent}')

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        # Already connected
        if xr == yr:
            return False
        elif self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        elif self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        else:
            self.parent[yr] = xr
            self.rank[xr] += 1
        self.count -= 1
        return True

    def get_count(self):
        return self.count


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        nc = len(grid[0])
        ans = 0
        uf = UnionFind(grid)
        for row in range(nr):
            for col in range(nc):
                if grid[row][col] == '1':
                    grid[row][col] = '0'
                    if row - 1 >= 0 and grid[row - 1][col] == '1':
                        uf.union(row * nc + col, (row - 1) * nc + col)
                    if row + 1 < nr and grid[row + 1][col] == '1':
                        uf.union(row * nc + col, (row + 1) * nc + col)
                    if col - 1 >= 0 and grid[row][col - 1] == '1':
                        uf.union(row * nc + col, row * nc + col - 1)
                    if col + 1 < nc and grid[row][col + 1] == '1':
                        uf.union(row * nc + col, row * nc + col + 1)

        return uf.get_count()


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(Solution().numIslands(grid))


