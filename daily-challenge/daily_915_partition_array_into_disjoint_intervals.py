from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        N = len(nums)
        maxleft = [None] * N
        minright = [None] * N

        m = nums[0]
        for i in range(N):
            m = max(m, nums[i])
            maxleft[i] = m

        m = nums[-1]
        for i in range(N - 1, -1, -1):
            m = min(m, nums[i])
            minright[i] = m

        for i in range(1, N):
            if maxleft[i - 1] <= minright[i]:
                return i