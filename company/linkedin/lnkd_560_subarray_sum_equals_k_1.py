"""
- two pointers?

- Make a prefix sum
  - iterate start and end pointer
"""


from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix = [0] * (len(nums) + 1)
        prefix[0] = 0
        for i in range(1, len(nums) + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]

        # print(f'prefix: {prefix}')

        ans = 0
        for start in range(len(prefix)):
            for end in range(start + 1, len(prefix)):
                end_prefix = prefix[end]
                start_prefix = prefix[start]
                summed = end_prefix - start_prefix
                if summed == k:
                    ans += 1

        return ans


nums = [1,1,1]
k = 2
nums = [1,2,3]
k = 3
print(Solution().subarraySum(nums, k))



