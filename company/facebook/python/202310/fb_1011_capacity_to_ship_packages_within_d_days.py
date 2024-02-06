"""
- Binary search and for loop each
  - Time O(NlogN)
"""


from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:

            # print(f'left: {left}, right: {right}')

            mid = left + (right - left) // 2

            # Each binary search requires to test the current capacity can
            # ship all the packages in d days
            curr = 0
            d = 1
            for weight in weights:

                # If current total weight exceeds current capacity mid
                if curr + weight > mid:
                    # Ship it
                    d += 1
                    # Reset current weight
                    curr = 0

                curr += weight

            # If current days exceeds the required days,
            # capacity was too small, so need to move left to right
            # to allow it to have more capacity
            if d > days:
                left = mid + 1
            else:
                right = mid

            # print(f'  mid: {mid}, d: {d}')

        # print(f'Last, left: {left}, right: {right}')

        return left


if __name__ == '__main__':
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days = 5
    print(Solution().shipWithDays(weights, days))
