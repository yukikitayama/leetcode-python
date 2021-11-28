from typing import List
from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        target = (rows - 1, cols - 1)

        # If we have lots of quotas, we can eliminate a lot, and the shortest distance will be
        # Manhattan distance.
        # e.g. rows: 3, cols: 3, Manhattan distance is, from upper left start, go down 2 steps,
        # and go right 2 steps to reach lower right end, so it's not exactly the sum of number of
        # rows and columns. You need to subtract 1 and 1 from each row and column.
        if k >= rows + cols - 2:
            return rows + cols - 2

        # State: (row, col, remaining quota to eliminate obstacles)
        # 0, 0 for upper left start point
        state = (0, 0, k)

        # Queue: (steps taken from the upper left start point, state)
        queue = deque([(0, state)])

        # Visited set to keep track of to avoid being the same state
        seen = set(state)

        while queue:
            steps, (row, col, k) = queue.popleft()

            # If we reach the lower right end point, return steps
            if (row, col) == target:
                return steps

            # Explore four directions by right, down, left, up
            for new_row, new_col in [(row, col + 1), (row + 1, col), (row, col - 1), (row - 1, col)]:

                # Check within the grid
                if (0 <= new_row < rows) and (0 <= new_col < cols):

                    # I think this is the most important line of code
                    # Just visit the next location regardless of empty or having obstacle
                    # If the next location is empty, k is not affected because subtracting 0
                    # But if the next location is obstacle, subtract 1 from k
                    # So whatever the state, just visit, but keep track of the remaining quotas of eliminations
                    new_eliminations = k - grid[new_row][new_col]
                    new_state = (new_row, new_col, new_eliminations)

                    # If qualified, go to the next state, otherwise go back to next item in the for loop
                    if new_eliminations >= 0 and new_state not in seen:
                        seen.add(new_state)
                        queue.append((steps + 1, new_state))

        # If the return statement in while didn't work, it means it couldn't find a path
        return -1


"""
Time complexity
Let n be the number of cells in the grid, and k be the quota to eliminate obstacles
O(n) in the worst case, and we have k variety in each cell in the grid, so O(nk)

Space complexity
queue and seen set consumes O(nk + nk) = O(nk), because each row col location has k variety
"""


grid = [
 [0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]
]
k = 1
grid = [
 [0,1,1],
 [1,1,1],
 [1,0,0]
]
k = 1
print(Solution().shortestPath(grid, k))
