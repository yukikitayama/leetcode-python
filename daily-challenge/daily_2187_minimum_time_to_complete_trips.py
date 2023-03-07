from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        def time_enough(given_time):

            actual_trips = 0

            for t in time:
                actual_trips += given_time // t

            # Enough is true
            return actual_trips >= totalTrips

        left = 1
        right = max(time) * totalTrips

        while left < right:

            mid = (left + right) // 2

            if time_enough(mid):
                right = mid

            else:
                left = mid + 1

        return left




