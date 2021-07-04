from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0

        for right in range(len(nums)):
            # When nums[right]: 0, reduce k by 1
            k -= 1 - nums[right]

            # Negative k denotes no more flips available
            if k < 0:
                # When nums[left]: 0, add k by 1
                k += 1 - nums[left]
                left += 1

        return right - left + 1


nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(Solution().longestOnes(nums, k))
