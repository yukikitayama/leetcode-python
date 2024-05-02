from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def compute_num_subarray(max_sum_allowed):
            curr_sum = 0
            splits = 0

            for num in nums:

                if curr_sum + num <= max_sum_allowed:
                    curr_sum += num

                else:
                    curr_sum = num
                    splits += 1

            # To have m subarrays, you should have m - 1 walls (splits) to partition them
            return splits + 1

        left = max(nums)
        right = sum(nums)

        while left <= right:
            mid = (left + right) // 2

            num_subarray = compute_num_subarray(mid)

            if num_subarray <= k:
                ans = mid
                # We wanna minimize the sum
                right = mid - 1

            # Otherwise, current sum (mid) isn't valid, so we need to try a bigger sum
            else:
                left = mid + 1

        return ans