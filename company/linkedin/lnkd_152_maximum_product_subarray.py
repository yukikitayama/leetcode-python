"""
nums: [2, 3, -2, 4]
i: 0, max_so_far: 2, min_so_far: 2
i: 1, max_so_far: 6, min_so_far: 2
i: 2, max_so_far: 6, min_so_far: -12
"""


from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        min_so_far = nums[0]
        ans = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]

            tmp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = tmp_max
            ans = max(ans, max_so_far)

            print(f'  curr: {curr}, max_so_far: {max_so_far}, min_so_far: {min_so_far}, ans: {ans}')

        return ans


nums = [2,3,-2,4]
print(Solution().maxProduct(nums))
