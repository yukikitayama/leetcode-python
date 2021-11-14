"""
- Similar to 1286
"""


from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # [] because Empty is also a subset of nums
        ans = [[]]

        for num in nums:
            ans += [curr + [num] for curr in ans]
            print(f'ans: {ans}, num: {num}')

        return ans


nums = [1, 2, 3]
print(Solution().subsets(nums))

