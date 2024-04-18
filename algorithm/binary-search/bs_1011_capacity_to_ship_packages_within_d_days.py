"""
cannot change the order of weights
partition weights array into days subarrays

if weights length <= days
  min weight capacity is max(weights)
if weights length > days
  sum of some elements in weights
left = max(weights)
right = sum(weights)
"""

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        # Function to check if current weight can ship all the packages within days
        def can_ship(w):
            d = 1
            curr_weight = 0
            for i in range(len(weights)):
                curr_weight += weights[i]
                if curr_weight > w:
                    curr_weight = weights[i]
                    d += 1
            if d <= days:
                return True
            else:
                return False

        # Binary search to find the min capable weights
        left = max(weights)
        right = sum(weights)
        while left <= right:
            # Weight
            mid = (left + right) // 2

            # Need to explore smaller weight
            if can_ship(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

