from typing import List
import collections


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        counter = collections.Counter([0])
        ans = 0
        prefix = 0
        for i in range(len(nums)):
            prefix += 1 if nums[i] % modulo == k else 0

            ans += counter[(prefix - k + modulo) % modulo]

            counter[prefix % modulo] += 1

        return ans