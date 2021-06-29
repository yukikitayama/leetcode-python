class Solution:
    def __init__(self):
        self.grid = None
        self.seen = None

    def maxAreaOfIsland(self, grid):
        self.grid = grid
        self.seen = set()
        answer = max(self.area(r, c) for r in range(len(self.grid)) for c in range(len(self.grid[0])))
        return answer

    def area(self, r, c):
        # Return 0 if we are out of bound, already visited, and no island
        if not (0 <= r < len(self.grid) and
                0 <= c < len(self.grid[0]) and
                (r, c) not in self.seen and
                self.grid[r][c]):
            return 0

        self.seen.add((r, c))
        # Visit all four directions if possible
        return 1 + self.area(r + 1, c) + self.area(r - 1, c) + self.area(r, c - 1) + self.area(r, c + 1)


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
sol = Solution()
answer = sol.maxAreaOfIsland(grid)
print(f'Answer: {answer}')
