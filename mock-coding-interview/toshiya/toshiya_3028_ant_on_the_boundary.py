from typing import List


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:

        curr = 0
        ans = 0

        for num in nums:

            curr += num

            if curr == 0:
                ans += 1

        return ans