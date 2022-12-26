from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        dp = [False] * len(nums)
        dp[0] = True
        max_so_far = nums[0]

        for i in range(len(nums)):

            if i <= max_so_far:
                dp[i] = True
                max_so_far = max(max_so_far, i + nums[i])

        # print(dp)

        return dp[-1]


if __name__ == '__main__':
    nums = [2,3,1,1,4]
    nums = [3, 2, 1, 0, 4]
    print(Solution().canJump(nums))


