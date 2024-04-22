"""
Binary search to find min speed
  left: 1
  right: hour
  compute sum of hours by ceil(dist / current mid speed)
  if sum is smaller than hour
    too fast speed, right = mid - 1
  if sum is bigger than hour
    too slow speed, left = mid + 1
  if sum is equal to hour
    there could be slower speed, right = mid - 1
"""

from typing import List
import math

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        left = 1
        right = 10 ** 7
        # ans is needed because left could be 10**7 if impossible,
        # and we cannot return the left
        ans = -1
        while left <= right:
            mid = (left + right) // 2

            total_hour = 0.0
            for i in range(len(dist)):
                if i != len(dist) - 1:
                    total_hour += math.ceil(dist[i] / mid)
                else:
                    total_hour += dist[i] / mid

            # print(left, mid, right, total_hour)

            if total_hour <= hour:
                right = mid - 1
                ans = mid
            elif total_hour > hour:
                left = mid + 1

        return ans