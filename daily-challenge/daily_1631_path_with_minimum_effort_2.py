from typing import List
import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])

        difference_matrix = [[float('inf')] * col for _ in range(row)]
        difference_matrix[0][0] = 0
        visited = [[False] * col for _ in range(row)]
        # (difference, x, y)
        queue = [(0, 0, 0)]
        # Min heap
        heapq.heapify(queue)

        while queue:

            difference, x, y = heapq.heappop(queue)
            visited[x][y] = True

            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:

                adjacent_x = x + dx
                adjacent_y = y + dy

                # Boundary and not visited
                if 0 <= adjacent_x < row and 0 <= adjacent_y < col and not visited[adjacent_x][adjacent_y]:

                    current_difference = abs(heights[adjacent_x][adjacent_y] - heights[x][y])

                    # Do max to keep track of difference you observed so far over the multiple iterations
                    # Each path has the max so far, and at the end, find the minimum difference path among them
                    # In this problem, we need to output minimum efforts, but max is just used for getting efforts
                    # of each path
                    max_difference = max(current_difference, difference_matrix[x][y])

                    # if difference_matrix[adjacent_x][adjacent_y] (which was previously calculated)
                    # is bigger than the current max_difference, we found a smaller effor path, so update
                    # difference_matrix[adjacent_x][adjacent_y]
                    if difference_matrix[adjacent_x][adjacent_y] > max_difference:
                        difference_matrix[adjacent_x][adjacent_y] = max_difference
                        heapq.heappush(queue, (max_difference, adjacent_x, adjacent_y))

        return difference_matrix[row - 1][col - 1]


"""
Time complexity
Let m be the number of rows and n be the number of columns
O(nm) to iterate all the cells in the grid, and O(log(nm)) to sort the queue to make priority queue work
so O(nmlog(nm))

Space complexity
O(nm) for priority queue, and O(nm) to keep track of visited matrix, so
O(nm + nm) = O(2nm) = O(nm)
"""