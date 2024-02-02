from typing import List
import functools


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        # Edge case
        if len(jobDifficulty) < d:
            return -1

        # Precompute max difficulty
        # It sees future to pre-find the max difficulty job at time i
        hardest_job_remaining = [0] * len(jobDifficulty)
        hardest_job = 0
        for i in range(len(jobDifficulty) - 1, -1, -1):
            hardest_job = max(hardest_job, jobDifficulty[i])
            hardest_job_remaining[i] = hardest_job

        # print(hardest_job_remaining)

        # Top-down
        @functools.lru_cache(maxsize=None)
        def dp(i, day):

            # Base case
            if day == d:
                return hardest_job_remaining[i]

            hardest = 0
            ans = float("inf")

            # -(d - day) to leave jobs at least one for each data
            for j in range(i, len(jobDifficulty) - (d - day)):
                hardest = max(hardest, jobDifficulty[j])
                ans = min(ans, hardest + dp(j + 1, day + 1))

            return ans

        return dp(0, 1)


if __name__ == "__main__":
    jobDifficulty = [6, 5, 4, 3, 2, 1]
    # jobDifficulty = [3, 5, 9, 3, 2, 7]
    d = 2
    print(Solution().minDifficulty(jobDifficulty, d))
