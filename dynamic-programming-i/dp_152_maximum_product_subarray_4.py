"""
- Keep max_so_far, used to accumulate max product from subarrays
- Keep min_so_far, used if current num is negative, and min_so_far is also negative
- max_so_far is max(current num, max_so_far, min_so_far)
  - current num is used if previous num was 0 or negative, and current num is positive
  - max_so_far is used if current num is also positive, and we wanna make it bigger
  - min_so_far is ued if curent num is negative, and min_so_far is negative, and these
    multiplication exceeds max_so_far
"""


from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        max_so_far = nums[0]
        min_so_far = nums[0]

        for num in nums[1:]:
            # Q: Why not just a single max_so_far in max()?
            #  A: Because
            prev_max_so_far = max_so_far
            max_so_far = max(num, max_so_far * num, min_so_far * num)
            min_so_far = min(num, prev_max_so_far * num, min_so_far * num)

            ans = max(ans, max_so_far)

        return ans

nums = [2,3,-2,4]
nums = [-2,0,-1]
print(Solution().maxProduct(nums))
