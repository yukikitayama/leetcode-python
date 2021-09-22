from typing import List
import pprint


class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        n = len(stations)
        deltas = [float(stations[i + 1] - stations[i]) for i in range(n - 1)]

        count = [1] * (n - 1)

        for _ in range(k):

            # Find interval with largest part
            best = 0
            for i, x in enumerate(deltas):
                # distance between stations / (number of new stations added - 1)
                curr_distance = x / count[i]
                # largest delta so far /
                deltas[best] / count[best]


stations = [23,24,36,39,46,56,57,65,84,98]
k = 1
print(Solution().minmaxGasDist(stations, k))
