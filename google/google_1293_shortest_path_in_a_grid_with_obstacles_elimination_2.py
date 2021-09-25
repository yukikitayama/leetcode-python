from typing import List
# from collections import deque
import heapq


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        target = (rows - 1, cols - 1)

        def manhattan_distance(row, col):
            return target[0] - row + target[1] - col

        state = (0, 0, k)
        # To return minimum number of steps, put the current steps to the queue
        queue = [(manhattan_distance(0, 0), 0, state)]
        heapq.heapify(queue)
        seen = set(state)

        while queue:

            # deque.pop() does not work, because it pops from the end, which is stack, not queue
            curr_total_cost, steps, (curr_row, curr_col, curr_k) = heapq.heappop(queue)

            #
            remaining_steps = curr_total_cost - steps
            if remaining_steps <= curr_k:
                return curr_total_cost

            # Try all the four directions
            for next_row, next_col in [
                (curr_row - 1, curr_col),
                (curr_row, curr_col + 1),
                (curr_row + 1, curr_col),
                (curr_row, curr_col - 1)
            ]:

                # Check boundary
                if 0 <= next_row < rows and 0 <= next_col < cols:

                    # Update k
                    next_k = curr_k - grid[next_row][next_col]
                    next_state = (next_row, next_col, next_k)

                    if next_k >= 0 and next_state not in seen:
                        seen.add(next_state)
                        # Estimated total cost = cost so far + cost to destination
                        next_estimation = (steps + 1) + manhattan_distance(next_row, next_col)
                        queue.append((next_estimation, steps + 1, next_state))

        return -1


"""
A star

State: (row, col, k)
DFS <- X. BFS to find the shortest path
min_so_far

Time: n cells, k states, O(nk), Space, O(2nk) = O(nk)
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


