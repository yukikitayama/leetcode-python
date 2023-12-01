from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:

        nums.sort()

        left = 0
        right = len(nums) - 1

        ans = -1

        while left < right:
            sum_ = nums[left] + nums[right]

            if sum_ < k:
                ans = max(ans, sum_)
                left += 1

            elif sum_ >= k:
                right -= 1

        return ans


if __name__ == "__main__":
    nums = [34, 23, 1, 24, 75, 33, 54, 8]
    k = 60
    print(Solution().twoSumLessThanK(nums, k))
