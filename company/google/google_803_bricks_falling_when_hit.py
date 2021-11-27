from typing import List


class DSU:
    def __init__(self, R, C):
        # Convert grid to array
        self.par = [i for i in range(R * C + 1)]
        self.rnk = [0] * (R * C + 1)
        # Number of indices in the set
        self.sz = [1] * (R * C + 1)

    def find(self, x):
        if self.par[x] != x:
            # Update the connected index with the leader
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)

        # If x and y are already connected, nothing needs to be done
        if xr == yr:
            return

        # We assume x has a higher ranking, but if y has higher, we use y
        if self.rnk[xr] < self.rnk[yr]:
            xr, yr = yr, xr

        # If the ranking is not updated yet, just use x
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1

        # This does actual union operations
        # Set leader index in the same set
        self.par[yr] = xr
        # Store the number of indices in the set to the leader
        self.sz[xr] += self.sz[yr]

    def size(self, x):
        # Find the x's leader and leader has the number of indices in the set
        return self.sz[self.find(x)]

    # ?
    def top(self):
        # len(self.sz) - 1 is the number of cells in the grid
        return self.size(len(self.sz) - 1) - 1


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        R, C = len(grid), len(grid[0])

        # R: 2, C: 2,
        # r: 0, c: 0, index(r, c): 0 * 2 + 0 = 0
        # r: 0, c: 1, index(r, c): 0 * 2 + 1 = 1
        # r: 1, c: 0, index(r, c): 1 * 2 + 0 = 2
        # r: 1, c: 1, index(r, c): 1 * 2 + 1 = 3
        # Convert index (row, col) in grid to index i in array
        def index(r, c):
            return r * C + c

        def neighbors(r, c):
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        A = [row[:] for row in grid]
        for i, j in hits:
            A[i][j] = 0

        dsu = DSU(R, C)
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                if val:
                    i = index(r, c)
                    # If the current cell is at the top
                    if r == 0:
                        # Why R*C?
                        dsu.union(i, R*C)

                    # If the current cell is not at the top, and it's brick
                    if r and A[r - 1][c]:
                        # ?
                        dsu.union(i, index(r - 1, c))

                    # If the current cell is not the first column and it's brick
                    if c and A[r][c - 1]:
                        dsu.union(i, index(r, c - 1))

        ans = []
        for r, c in reversed(hits):
            # ?
            pre_roof = dsu.top()

            # If it hits non brick cell in the grid, nothing fells
            if grid[r][c] == 0:
                ans.append(0)

            else:
                i = index(r, c)

                # ?
                for nr, nc in neighbors(r, c):
                    if A[nr][nc]:
                        dsu.union(i, index(nr, nc))

                # ?
                if r == 0:
                    dsu.union(i, R*C)

                # ?
                A[r][c] = 1

                # ?
                ans.append(max(0, dsu.top() - pre_roof - 1))

        return ans[::-1]


grid = [[1,0,0,0],[1,1,1,0]]
hits = [[1,0]]
grid = [[1,0,0,0],[1,1,0,0]]
hits = [[1,1],[1,0]]
print(Solution().hitBricks(grid, hits))

