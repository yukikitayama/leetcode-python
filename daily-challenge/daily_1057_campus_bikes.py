from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:

        def find_distance(w, b):
            return abs(w[0] - b[0]) + abs(w[1] - b[1])

        pairs = []

        for w_i, w_l in enumerate(workers):
            for b_i, b_l in enumerate(bikes):
                d = find_distance(w_l, b_l)
                pairs.append((d, w_i, b_i))

        pairs.sort()

        available_bikes = [True] * len(bikes)
        ans = [-1] * len(workers)
        assigned_count = 0

        for d, w_i, b_i in pairs:

            if ans[w_i] == -1 and available_bikes[b_i]:
                available_bikes[b_i] = False
                ans[w_i] = b_i
                assigned_count += 1

                if assigned_count == len(workers):
                    return ans

        return ans


if __name__ == "__main__":
    workers = [[0, 0], [2, 1]]
    bikes = [[1, 2], [3, 3]]
    print(Solution().assignBikes(workers, bikes))
