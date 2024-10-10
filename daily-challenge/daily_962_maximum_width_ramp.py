from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        indices = [i for i in range(len(nums))]
        indices.sort(key=lambda i: (nums[i], i))

        min_index = indices[0]
        ans = 0
        for i in indices[1:]:
            ans = max(ans, i - min_index)
            min_index = min(min_index, i)

        return ans

    def maxWidthRamp1(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] <= nums[j]:
                    ans = max(ans, j - i)

        return ans