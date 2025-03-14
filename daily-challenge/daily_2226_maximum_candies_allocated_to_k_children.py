from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        def can_allocate_candies(num_candies):
            if num_candies == 0:
                return False
            res = 0
            for candy in candies:
                res += candy // num_candies
            return res >= k

        right = max(candies)
        left = 0
        ans = left
        while left <= right:
            mid = (left + right + 1) // 2

            if can_allocate_candies(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
