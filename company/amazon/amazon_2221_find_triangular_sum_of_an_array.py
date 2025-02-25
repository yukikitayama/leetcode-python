from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:

        for i in range(len(nums), 0, -1):
            for j in range(1, i):
                nums[j - 1] += nums[j]
                nums[j - 1] %= 10

        return nums[0]

    def triangularSum1(self, nums: List[int]) -> int:
        curr = nums.copy()
        while len(curr) > 1:
            next_ = []
            for i in range(1, len(curr)):
                next_.append((curr[i - 1] + curr[i]) % 10)
            curr = next_

            # print(next_)

        return curr[0]