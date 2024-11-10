from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = float("inf")
        start = end = 0
        bit_counts = [0] * 32

        def update_bit_counts(num, delta):
            for i in range(32):
                if num & (1 << i):
                    bit_counts[i] += delta

        def convert_bits_to_num():
            res = 0
            for i in range(32):
                if bit_counts[i]:
                    res |= 1 << i
            return res

        while end < len(nums):

            update_bit_counts(nums[end], 1)

            # If need shrink
            while start <= end and convert_bits_to_num() >= k:
                ans = min(ans, end - start + 1)
                update_bit_counts(nums[start], -1)
                start += 1

            end += 1

        return -1 if ans == float("inf") else ans
