"""
lower rank should repair more
"""

from typing import List
import collections
import math


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        min_rank = min(ranks)
        max_rank = max(ranks)
        counter = collections.Counter(ranks)
        low = 1
        high = min_rank * cars * cars

        while low < high:
            mid = (low + high) // 2
            cars_repaired = 0
            for rank in counter.keys():
                cars_repaired += counter[rank] * int(math.sqrt(mid // rank))

            if cars_repaired >= cars:
                high = mid
            else:
                low = mid + 1

        return low