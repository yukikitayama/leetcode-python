"""
- Constraints says grid is small but number could be very high
- So BFS + priority queue is better than BFS + binary search
"""


from typing import List
import collections
import heapq


class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        """
        BFS + Priority Queue, this is better when grid is smaller and grid contains high values
        because high values will spend more time for binary search
        :param grid:
        :return:
        """
        R = len(grid)
        C = len(grid[0])

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        heap = []
        ans = grid[0][0]

        # Multiply - because we wanna make it max heap
        # heap: (value, row, col)
        heapq.heappush(heap, (-grid[0][0], 0, 0))

        visited = [[False] * C for _ in range(R)]
        visited[0][0] = True

        # BFS + Priority Queue
        while heap:
            cur_val, cur_row, cur_col = heapq.heappop(heap)

            ans = min(ans, grid[cur_row][cur_col])

            if cur_row == R - 1 and cur_col == C - 1:
                break

            for d_row, d_col in dirs:
                new_row = cur_row + d_row
                new_col = cur_col + d_col

                if 0 <= new_row < R and 0 <= new_col < C and not visited[new_row][new_col]:
                    visited[new_row][new_col] = True
                    heapq.heappush(heap, (-grid[new_row][new_col], new_row, new_col))

        return ans


class Solution2:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        """
        Binary search the current score, for each score, BFS
        Time is O(MNlogK).logK because binary search to iterate the score
        :param grid:
        :return:
        """
        R = len(grid)
        C = len(grid[0])

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def path_exists(cur_score):

            visited = [[False] * C for _ in range(R)]
            visited[0][0] = True

            dq = collections.deque([(0, 0)])

            while dq:

                cur_row, cur_col = dq.popleft()

                if cur_row == R - 1 and cur_col == C - 1:
                    return True

                for d_row, d_col in dirs:
                    new_row = cur_row + d_row
                    new_col = cur_col + d_col

                    if not (0 <= new_row < R and 0 <= new_col < C):
                        continue

                    if grid[new_row][new_col] >= cur_score and not visited[new_row][new_col]:
                        visited[new_row][new_col] = True
                        dq.append((new_row, new_col))

            return False

        left = 0
        right = min(grid[0][0], grid[R - 1][C - 1])

        while left <= right:

            mid = left + (right - left) // 2
            if path_exists(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right


class Solution1:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        """
        For each score, BFS. Decrement score from high to small.
        Let k be the largest possible value
        Time O(NMK)
        :param grid:
        :return:
        """
        R = len(grid)
        C = len(grid[0])

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def path_exists(cur_score):

            visited = [[False] * C for _ in range(R)]
            visited[0][0] = True

            dq = collections.deque([(0, 0)])

            while dq:

                cur_row, cur_col = dq.popleft()

                if cur_row == R - 1 and cur_col == C - 1:
                    return True

                for d_row, d_col in dirs:
                    new_row = cur_row + d_row
                    new_col = cur_col + d_col

                    if not (0 <= new_row < R and 0 <= new_col < C):
                        continue

                    if grid[new_row][new_col] >= cur_score and not visited[new_row][new_col]:
                        visited[new_row][new_col] = True
                        dq.append((new_row, new_col))

            return False

        cur_score = min(grid[0][0], grid[R - 1][C - 1])

        while cur_score >= 0:
            if path_exists(cur_score):
                return cur_score
            else:
                cur_score -= 1


if __name__ == '__main__':
    grid = [[5, 4, 5], [1, 2, 6], [7, 4, 6]]
    # 4
    print(Solution().maximumMinimumPath(grid))
