"""
Find max
sum each diff
"""


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ans = 0
        max_num = max(nums)
        for num in nums:
            ans += max_num - num
        return ans