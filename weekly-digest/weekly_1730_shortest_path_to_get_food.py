from typing import List
from collections import deque


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        # Get parameters
        rows = len(grid)
        cols = len(grid[0])

        # Find the start cell
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '*':
                    start_row = row
                    start_col = col

        # Initialization for Breadth First Search
        state = (start_row, start_col)
        steps = 0
        queue = deque([(state, steps)])
        visited = set(state)

        # Start BFS traverse
        while queue:

            # Get the current state and steps
            (curr_row, curr_col), steps = queue.popleft()

            # If it found a pizza, return the number of steps so far.
            # This steps is guaranteed to be the minimum steps because we use BFS
            if grid[curr_row][curr_col] == '#':
                return steps

            # We haven’t found a pizza yet, so go to another cell to find it
            for next_row, next_col in [
                (curr_row + 1, curr_col),
                (curr_row - 1, curr_col),
                (curr_row, curr_col + 1),
                (curr_row, curr_col - 1)
            ]:

                # We can go if the next cell is in the grid, a free space, not visited yet, and either a free space or pizza place
                if 0 <= next_row < rows \
                        and 0 <= next_col < cols \
                        and grid[next_row][next_col] in ['O', '#'] \
                        and (next_row, next_col) not in visited:
                    next_state = (next_row, next_col)
                    # Append the next_state to queue and visit to allow BFS to happen
                    queue.append((next_state, steps + 1))
                    visited.add(next_state)

        # Otherwise, it wasn’t able to find a pizza, meaning no parth to find the pizza so return -1
        return -1


"""
Time complexity
- Let n be the number of cells in the grid. O(n) to find the start cell and O(n) to traverse all the cell in BFS, O(n + n) = O(2n) = O(n)
Space complexity
- O(n) for queue and visited set, so O(n + n) = O(2n) = O(n)
In New York City, Koronet Piazza is good at 2848 Broadway, New York, NY 10025
"""