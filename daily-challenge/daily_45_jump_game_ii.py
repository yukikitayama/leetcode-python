from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        ans = 0
        n = len(nums)

        end = 0
        far = 0

        for i in range(n - 1):

            far = max(far, i + nums[i])

            if i == end:
                ans += 1
                end = far

        return ans


