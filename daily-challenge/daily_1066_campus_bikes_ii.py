from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        memo = [-1] * 1024

        def find_distance(worker, bike):
            return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])

        def minimum_distance_sum(workers, bikes, worker_index, mask):
            if worker_index >= len(workers):
                return 0

            if memo[mask] != -1:
                return memo[mask]

            smallest_distance_sum = float('inf')
            for bike_index in range(len(bikes)):

                # If mask is not equal to (1 << bikeIndex), it returns 0
                # Meaning mask is available
                if mask & (1 << bike_index) == 0:
                    smallest_distance_sum = min(
                        smallest_distance_sum,
                        find_distance(
                            workers[worker_index],
                            bikes[bike_index]
                        ) + minimum_distance_sum(
                            workers,
                            bikes,
                            worker_index + 1,
                            mask | (1 << bike_index)
                        )
                    )

            memo[mask] = smallest_distance_sum
            return memo[mask]

        return minimum_distance_sum(workers, bikes, 0, 0)


workers = [[0,0],[2,1]]
bikes = [[1,2],[3,3]]
workers = [[0,0],[1,1],[2,0]]
bikes = [[1,0],[2,2],[2,1]]
print(Solution().assignBikes(workers, bikes))

