from typing import List
import bisect


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        sorted_distinct_nums = sorted(set(nums))
        right_idx = 0
        for left_idx in range(len(nums)):
            while right_idx < len(sorted_distinct_nums) and nums[right_idx] < nums[left_idx] + n:
                right_idx += 1

            ans = min(
                ans,
                n - (right_idx - left_idx)
            )

        return ans

    def minOperations1(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n

        sorted_distinct_nums = sorted(list(set(nums)))

        for left_index in range(len(sorted_distinct_nums)):
            left_num = sorted_distinct_nums[left_index]
            right_num = left_num + n - 1

            right_index = bisect.bisect_right(sorted_distinct_nums, right_num)

            ans = min(
                ans,
                n - (right_index - left_index)
            )

        return ans