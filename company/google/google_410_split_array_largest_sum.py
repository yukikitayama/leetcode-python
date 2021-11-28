from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def split(nums, largest_sum):
            pieces = 1
            tmp_sum = 0
            for num in nums:
                if tmp_sum + num > largest_sum:
                    tmp_sum = num
                    pieces += 1
                else:
                    tmp_sum += num
            return pieces

        low = max(nums)
        high = sum(nums)
        while low < high:
            mid = low + (high - low) / 2
            pieces = split(nums, mid)
            if pieces > m:
                low = mid + 1
            else:
                high = mid
        return low