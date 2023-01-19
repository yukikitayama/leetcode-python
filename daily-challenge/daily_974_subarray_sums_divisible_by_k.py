"""
- Prefix sum or sliding window
"""


from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        n = len(nums)

        prefix_mod = 0
        ans = 0

        mod_groups = [0] * k
        mod_groups[0] = 1

        for num in nums:
            prefix_mod = (prefix_mod + num % k + k) % k
            ans += mod_groups[prefix_mod]
            mod_groups[prefix_mod] += 1

        return ans


