from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_ = sum(nums[:k])
        ave = sum_ / k

        ans = ave

        for i in range(1, len(nums) - k + 1):

            sum_ = sum_ - nums[i - 1] + nums[i + k - 1]
            ave = sum_ / k

            if ave > ans:
                ans = ave

        return ans
