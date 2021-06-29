from typing import List


class Solution:
    def __init__(self):
        self.grid = None
        self.visited = None

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        # Set: {(row, column), ()....}
        self.visited = set()

        answer = 0

        for row in range(len(grid)):
            for column in range(len(grid[0])):
                area = self.get_area(row, column)
                answer = max(answer, area)

        return answer

    def get_area(self, row: int, column: int) -> int:

        if not (0 <= row < len(self.grid) and
                0 <= column < len(self.grid[0]) and
                self.grid[row][column] == 1 and
                (row, column) not in self.visited):
            return 0

        self.visited.add((row, column))

        # top, right, down, left
        return 1 + \
               self.get_area(row - 1, column) + \
               self.get_area(row, column + 1) + \
               self.get_area(row + 1, column) + \
               self.get_area(row, column - 1)

# grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
grid = [[0,0,0,0,0,0,0,0]]
print(f'Answer: {Solution().maxAreaOfIsland(grid)}')
