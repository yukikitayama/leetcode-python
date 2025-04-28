from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        cur_sum = 0
        for right in range(len(nums)):

            cur_sum += nums[right]

            while left <= right and cur_sum * (right - left + 1) >= k:
                cur_sum -= nums[left]
                left += 1

            # Here score is < k
            ans += (right - left + 1)

        return ans