"""
- Sliding window
"""


from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_ = 0
        for i in range(k):
            sum_ += nums[i]

        ans = sum_

        for i in range(k, len(nums)):
            # Subtract least recent
            sum_ -= nums[i - k]

            # Add recent
            sum_ += nums[i]

            ans = max(ans, sum_)

        return ans / k


if __name__ == '__main__':
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    print(Solution().findMaxAverage(nums, k))
