"""
- Place rocks from the bags which are close to full capacity
"""


from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:

        rest = [c - r for c, r in zip(capacity, rocks)]

        rest.sort()

        ans = 0

        for r in rest:
            if additionalRocks >= r:
                additionalRocks -= r
                ans += 1
            else:
                break

        return ans


if __name__ == '__main__':
    capacity = [2, 3, 4, 5]
    rocks = [1, 2, 4, 4]
    additionalRocks = 2

    # capacity = [10, 2, 2]
    # rocks = [2, 2, 0]
    # additionalRocks = 100

    print(Solution().maximumBags(capacity, rocks, additionalRocks))

