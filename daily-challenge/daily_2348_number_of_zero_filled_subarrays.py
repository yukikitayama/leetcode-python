from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0

        curr = 0

        for num in nums:

            if num == 0:
                curr += 1

            else:
                curr = 0

            ans += curr

        return ans

