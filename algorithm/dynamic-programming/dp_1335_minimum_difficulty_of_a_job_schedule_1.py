from typing import List
import functools


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        # It needs to do at least one job per day
        if n < d:
            return -1

        hardest_job_remaining = [0] * n
        hardest_job = 0
        for i in range(n - 1, -1, -1):
            hardest_job = max(hardest_job, jobDifficulty[i])
            hardest_job_remaining[i] = hardest_job

        print(f'jobDifficulty: {jobDifficulty}')
        print(f'hardest_job_remaining: {hardest_job_remaining}')

        @functools.lru_cache(maxsize=None)
        def dp(i, day):
            if day == d:
                return hardest_job_remaining[i]

            best = float('inf')
            hardest = 0
            # -(d - day) because it needs to leave (d - day) jobs to achieve
            # at least one task per day
            for j in range(i, n - (d - day)):
                hardest = max(hardest, jobDifficulty[j])
                best = min(best, hardest + dp(j + 1, day + 1))

            return best

        return dp(0, 1)


jobDifficulty = [6,5,4,3,2,1]
d = 2
jobDifficulty = [7,1,7,1,7,1]
d = 3
print(Solution().minDifficulty(jobDifficulty, d))



