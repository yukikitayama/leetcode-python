"""
min heap

n: 4
m: 5

1st: 5 (m)
2nd: 4 (m - 1)
3rd: 3
4th: 2 (m - 3 = m - n + 1, +1 because 4th person hasn't selected yet)


"""

from typing import List
import functools


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:

        ans = float("inf")

        def compute_distance(point_a, point_b):
            return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])

        visited = [False] * len(bikes)

        def recursion(worker_index, curr_distance_sum):

            nonlocal ans

            if worker_index >= len(workers):
                ans = min(ans, curr_distance_sum)
                return

            # Little time optimization
            if curr_distance_sum >= ans:
                return

            for b in range(len(bikes)):

                if not visited[b]:
                    visited[b] = True
                    d = compute_distance(workers[worker_index], bikes[b])
                    recursion(worker_index + 1, curr_distance_sum + d)
                    visited[b] = False

        recursion(0, 0)

        return ans


    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:

        def compute_distance(point_a, point_b):
            return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])

        @functools.lru_cache(maxsize=None)
        def dp(worker_index, mask):

            if worker_index >= len(workers):
                return 0

            ans = float("inf")

            for bike_index in range(len(bikes)):

                if mask & (1 << bike_index) == 0:
                    d = compute_distance(workers[worker_index], bikes[bike_index])
                    new_mask = mask | (1 << bike_index)
                    ans = min(ans, d + dp(worker_index + 1, new_mask))

            return ans

        return dp(0, 0)


if __name__ == "__main__":
    workers = [[0, 0], [2, 1]]
    bikes = [[1, 2], [3, 3]]
    # 6
    workers = [[0, 0], [1, 1], [2, 0]]
    bikes = [[1, 0], [2, 2], [2, 1]]
    # 4
    print(Solution().assignBikes(workers, bikes))
