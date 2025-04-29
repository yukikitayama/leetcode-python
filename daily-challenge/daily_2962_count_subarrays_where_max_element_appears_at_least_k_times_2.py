from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        counter = 0
        ans = 0
        left = 0
        for right in range(len(nums)):

            if nums[right] == max_num:
                counter += 1

            # Shrink
            while left <= right and counter == k:
                if nums[left] == max_num:
                    counter -= 1
                left += 1

            # [1, 2, 1], k: 1
            ans += left

        return ans