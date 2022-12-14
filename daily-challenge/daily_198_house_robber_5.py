from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0

        n = len(nums)

        prev = nums[0]
        prev_prev = 0

        for i in range(1, n):

            curr = max(prev, prev_prev + nums[i])

            prev_prev = prev
            prev = curr

        return prev


if __name__ == '__main__':
    nums = [2,1,1,2]
    print(Solution().rob(nums))
