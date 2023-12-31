"""
Cut array into d pieces

dp because sub-problem affects next and optimize as minimum
"""

from typing import List
import functools


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        n = len(jobDifficulty)

        if n < d:
            return -1

        @functools.lru_cache(maxsize=None)
        def min_diff(i, days_remaining):

            # Base case
            if days_remaining == 1:
                return max(jobDifficulty[i:])

            ans = float("inf")

            daily_max_job_diff = 0

            for j in range(i, n - days_remaining + 1):

                daily_max_job_diff = max(daily_max_job_diff, jobDifficulty[j])

                ans = min(ans, daily_max_job_diff + min_diff(j + 1, days_remaining - 1))

            return ans

        return min_diff(0, d)


if __name__ == "__main__":
    jobDifficulty = [6, 5, 4, 3, 2, 1]
    # jobDifficulty = [1, 3, 2, 5, 4, 3]
    d = 2
    print(Solution().minDifficulty(jobDifficulty, d))
