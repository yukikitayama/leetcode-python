from typing import List
import pprint


class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:

        def possible(D):
            return sum(int((stations[i + 1] - stations[i]) / D) for i in range(len(stations) - 1)) <= k

        lo = 0
        hi = 10**8
        while hi - lo > 1e-6:
            mi = (lo + hi) / 2.0

            if possible(mi):
                hi = mi
            else:
                lo = mi

        return lo


stations = [23,24,36,39,46,56,57,65,84,98]
k = 1
print(Solution().minmaxGasDist(stations, k))
