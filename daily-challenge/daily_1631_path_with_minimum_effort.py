from typing import List
import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])

        difference_matrix = [[float('inf')] * col for _ in range(row)]

        # Start from top left
        difference_matrix[0][0] = 0

        # Difference matrix will be updated before visiting
        # Heap will contain multiple same cells with different differences
        visited = [[False] * col for _ in range(row)]

        # Min heap
        # Heap: [(difference, x, y), ...]
        heap = [(0, 0, 0)]

        while heap:

            difference, x, y = heapq.heappop(heap)

            visited[x][y] = True

            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:

                adjacent_x = x + dx
                adjacent_y = y + dy

                if 0 <= adjacent_x < row and 0 <= adjacent_y < col and not visited[adjacent_x][adjacent_y]:
                    current_difference = abs(heights[adjacent_x][adjacent_y] - heights[x][y])

                    # difference_matrix[x][y] is the max difference so far in a path
                    # this is not comparing with inf
                    max_difference = max(current_difference, difference_matrix[x][y])

                    # If the newly found max difference so far (max_difference) is smaller than
                    # the recorded max difference (difference_matrix[adjacent_x][adjacent_y]),
                    # then we found smaller path so we update the difference_matrix and
                    # push it to min heap
                    if difference_matrix[adjacent_x][adjacent_y] > max_difference:
                        difference_matrix[adjacent_x][adjacent_y] = max_difference

                        heapq.heappush(heap, (max_difference, adjacent_x, adjacent_y))

        return int(difference_matrix[-1][-1])


class Solution1:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])

        max_so_far = float('inf')

        def dfs(x, y, max_difference):

            nonlocal max_so_far

            # Terminate recursion
            if x == row - 1 and y == col - 1:
                max_so_far = min(max_so_far, max_difference)
                return max_difference

            # Save current height to temporary variable
            # to later backtrack
            # Also used to compute height difference between current cell and neighbors
            current_height = heights[x][y]

            # Mark as visited
            heights[x][y] = 0

            # Be returned
            ans = float('inf')

            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                adjacent_x = x + dx
                adjacent_y = y + dy

                # If in the grid and if not visited yet
                if 0 <= adjacent_x < row and 0 <= adjacent_y < col and heights[adjacent_x][adjacent_y] != 0:
                    current_difference = abs(heights[adjacent_x][adjacent_y] - current_height)

                    # Update the max difference recorded so far in a path
                    max_current_difference = max(max_difference, current_difference)

                    if max_current_difference < max_so_far:
                        result = dfs(adjacent_x, adjacent_y, max_current_difference)

                        ans = min(ans, result)

            # Backtrack
            heights[x][y] = current_height

            return ans

        return dfs(0, 0, 0)


if __name__ == '__main__':
    heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
    # 2
    # heights = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
    # 1
    print(Solution().minimumEffortPath(heights))
