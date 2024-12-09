from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        max_reach = [0] * len(nums)
        end = 0
        for start in range(len(nums)):
            end = max(end, start)
            while end < len(nums) - 1 and nums[end] % 2 != nums[end + 1] % 2:
                end += 1
            max_reach[start] = end

        ans = []
        for s, e in queries:
            res = e <= max_reach[s]
            ans.append(res)

        return ans