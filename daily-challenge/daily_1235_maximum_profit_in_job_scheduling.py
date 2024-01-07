"""
dp

dp[i] stands the max profit at i time
top-down dp

job index of start time sorted
- 0
  - skip
    - skip
    - schedule
  - schedule

"""

from typing import List
import functools
import bisect


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [(s, e, p) for s, e, p in zip(startTime, endTime, profit)]
        jobs.sort()
        sorted_start_times = [job[0] for job in jobs]

        # print(jobs)
        # print(sorted_start_times)

        @functools.lru_cache(maxsize=None)
        def dp(curr):

            # Base case of DP
            if curr == len(profit):
                return 0

            # sorted_start_index: [10, 20], end_time: 15, bisect_left returns 1
            next_start_index = bisect.bisect_left(sorted_start_times, jobs[curr][1])

            max_profit = max(
                # Skip current job
                dp(curr + 1),
                # Or take current job and take the next non-conflicting job
                jobs[curr][2] + dp(next_start_index)
            )

            return max_profit

        return dp(0)


if __name__ == "__main__":
    startTime = [1, 2, 3, 3]
    endTime = [3, 4, 5, 6]
    profit = [50, 10, 40, 70]
    # 120
    # startTime = [1, 2, 3, 4, 6]
    # endTime = [3, 5, 10, 6, 9]
    # profit = [20, 20, 100, 70, 60]
    # 150
    print(Solution().jobScheduling(startTime, endTime, profit))

